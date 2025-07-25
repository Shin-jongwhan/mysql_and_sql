### 250724
# mysql slave 복구 자동화 시나리오
### 아래와 같은 워크플로우로 해야 한다.
1. table lock
2. mysqldump. dump 파일을 slave에서도 쓸 수 있도록 scp를 하는 등으로 전달.
    ```
    mysqldump -uroot -proot --databases $(mysql -uroot -proot -Nse "SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('mysql','performance_schema','information_schema','sys')") > /data/mysql/tgf/backup/test.sql
    ```
4. mysql slave에 접속 -> dump한 거 import
5. slave 설정
    - mysql master에서 relay bin 값 등 조회해서 가져오기
    - mysql slave 설정
6. table lock 해제
### <br/>

### 조건
- 모든 db에 접근할 수 있는, 복구할 수 있는 계정이 세팅되어 있어야 함
- slave용 계정이 master, slave 모든 node에 생성되어 있어야 함. 아래 예시의 경우 repl이라는 계정으로 들어가있다.
### <br/>

### kubernetes에서 자동으로 복구하게 CronJob으로 모니터링 해서 더 고도화된 자동화 워크플로우를 구성할 수도 있다.
#### slave_setup.sh
```bash
#!/bin/bash

# 1. 백업 파일 이름에 사용할 날짜/시간 변수 만들기
backup_date=$(date +"%Y%m%d%H%M%S")

# 2. MySQL 접속 정보 변수로 저장(옵션)
MYSQL_HOST=$1
MYSQL_USER=$2
MYSQL_PW=$3
MYSQL_USER_SLAVE=$4
MYSQL_PW_SLAVE=$5

# 3. Lock + sleep (예: 60초 동안 lock 유지)
mysql -h "$MYSQL_HOST" -u "$MYSQL_USER" -p"$MYSQL_PW" <<EOF &
flush tables with read lock;
SELECT SLEEP(3600);
EOF

LOCK_PID=$!

# 4. mysqldump로 dump 파일 생성
backup_sql=/data/mysql/backup/${backup_date}_backup.sql
mysqldump -h "$MYSQL_HOST" -u "$MYSQL_USER" -p"$MYSQL_PW" \
  --databases $(mysql -h "$MYSQL_HOST" -u "$MYSQL_USER" -p"$MYSQL_PW" -Nse \
    "SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('performance_schema','information_schema','sys')") \
  > $backup_sql

# 쿼리 결과를 한 줄로 출력받기
read binlog_file binlog_pos <<< $(mysql -h "$MYSQL_HOST" -u "$MYSQL_USER" -p"$MYSQL_PW" -Nse "SHOW BINARY LOG STATUS;" | awk '{print $1, $2}')

echo "Binlog File: $binlog_file"
echo "Binlog Position: $binlog_pos"

if [[ -f "$backup_sql" ]]; then
    echo "Backup file found: $backup_sql"
    mysql -h "$MYSQL_HOST" -u "$MYSQL_USER" -p"$MYSQL_PW" < "$backup_sql"
    echo "Import completed successfully."
else
    echo "Backup file does not exist: $backup_sql"
fi

mysql -u "$MYSQL_USER_SLAVE" -p"$MYSQL_PW_SLAVE" <<EOF
    stop replica;
    reset replica;
    CHANGE REPLICATION SOURCE TO SOURCE_HOST="$MYSQL_HOST", SOURCE_LOG_FILE='$binlog_file', SOURCE_LOG_POS=$binlog_pos, SOURCE_SSL=1;
    START REPLICA USER='repl' PASSWORD='repl_pass';
EOF

# 3. 필요하다면 lock 세션을 강제로 종료(=lock 해제)
kill $LOCK_PID

```
### <br/>
