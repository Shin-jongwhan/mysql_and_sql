### 240105
## database 이중화
### 참고 블로그 / 웹사이트
#### https://jane096.github.io/project/mysql-master-slave-replication/
#### https://velog.io/@mooh2jj/%EC%84%9C%EB%B2%84-%EB%B6%84%EC%82%B0-%EC%B2%98%EB%A6%AC-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-MySQL%EC%9D%84-MasterSlave%EB%A1%9C-%EC%9D%B4%EC%A4%91%ED%99%94%ED%95%98%EA%B8%B0
### <br/><br/><br/>

## 사용 이유
### 1. 쓰기 기능은 메인 서버에서 실행, 읽기 기능은 분산된 서버에서 수행하도록 함
### 2. 복제. database 의 안정성을 높인다.
### 3. 장애 극복. 특정 서버가 에러가 났을 때 다른 서버에서 기능하도록 하여 안정성을 높인다. 만약 master 가 에러가 났다면, slave 를 master 로 승격한다. 하지만 이러한 경우 slave 로 완벽하게 복제가 일어나지 않았다면 그 중간에 빈 시간 동안의 데이터 소실이 있을 수 있다.
### <br/><br/><br/>

## replication 작동 방식
### master 는 slave 로 비동기 방식으로 복제를 한다.
### 아래 그림과 같이 흘러가는데 master, slave 들이 각각 log 에 변경 사항을 기록한다.
### slave SQL thread 에서 변경 사항을 최종 적용한다.
### ![image](https://github.com/Shin-jongwhan/mysql_and_sql/assets/62974484/9de59d7e-aaf4-4af7-b11e-5f75231c699a)
### <br/>

## binary-log
### 블로그 글 발췌
#### binarylog는 binlog라고도 부르고 있습니다.
#### MySQL에서 발생하는 모든 내역을 기록하는 Log File이고, 이것은 기본적으로 비활성화되어 있는데, conf 파일에서 수정해서 이를 활성화 시켜주어야 합니다.
### <br/>

## db dump
### 먼저 slave mysql 서버에 dump 를 해줘야 한다. 안 그러면 master mysql 서버에서 slave 쪽이랑 설정값이 달라진다.
### dump 는 아래 정리 글을 참고한다.
### https://github.com/Shin-jongwhan/mysql_and_sql/tree/main/mysql/how_to_dump
### <br/>

## master - my.cnf 설정
### 먼저 mysqld kill 해주고 한다.
```
service mysql stop
# 안 되면 ps -ef | grep mysql 한 후
kill -9 [pid]
```

```
[mysqld]
#port=3307
datadir=/data/mysql_docker
log-bin=/data/mysql_docker/mysql-bin.log
server-id = 1
expire_logs_days = 10
max_binlog_size = 100M

[mysqldump]
default-character-set = utf8

[mysql]
default-character-set = utf8
```
### <br/>

## master mysql 에서 slave mysql 서버를 등록
```
# 계정 생성
CREATE USER 'slave_1'@'ip_address' IDENTIFIED BY 'test';

# 권한 설정
GRANT REPLICATION SLAVE ON *.* TO 'slave_1'@'ip_address';
```

### 설정 확인
### 여기서 File, Position 정보값은 기억해야 한다. slave 에 넣어줘야 함.
```
# mysql 8 버전
SHOW MASTER STATUS \G
```
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql/assets/62974484/fd9f5a6f-bd84-411b-ba7a-232455038500)
```
# mysql 9 버전
SELECT * FROM performance_schema.log_status;
```
#### <img width="942" height="174" alt="image" src="https://github.com/user-attachments/assets/145c4c7d-c4ca-41b2-8f14-856e5d1a5113" />
### <br/>

## slave mysql 서버 설정
### 1. my.cnf 
### server-id = 2 와 같이 master 에서 사용한 1 번은 제외하여 다른 번호를 부여한다.
```
[mysqld]
#port=3307
datadir=/data/mysql
server-id = 2

[mysqldump]
default-character-set = utf8

[mysql]
default-character-set = utf8
```
### <br/>

### 2. slave mysql 에 접속하여 master mysql 의 정보를 입력해준다.
### * SOURCE_LOG_POS 는 계속 변한다. 주기는 잘 모르겠지만 설정값에 따라 변하는데 약 1분마다 변한다. 계속 체크해주면서 등록해줘야 한다.
- SOURCE_HOST : master mysql ip
- SOURCE_LOG_FILE : master mysql 에서 얻은 master FILE
- SOURCE_LOG_POS : master mysql 에서 얻은 master POSITION
```
CHANGE REPLICATION SOURCE TO SOURCE_HOST='ip', SOURCE_LOG_FILE='mysql-bin.000003', SOURCE_LOG_POS=1265, SOURCE_SSL=1;
START REPLICA USER='repl' PASSWORD='1234';
```
### <br/>

### 3. 연결 확인
#### mysql 8 버전
```
SHOW REPLICA STATUS \G;
```
#### mysql 9 버전
```
SHOW BINARY LOG STATUS;
```
### 아래와 같이 master mysql 과 설정값이 같아야 한다.
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql/assets/62974484/6f9818bc-a390-4c03-ab7c-33f5df293694)
### <br/>

### 다음과 같이 Replica_IO_Running, Replica_SQL_Running 에 yes 가 뜨면 잘 작동하고 있는 것이다.
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql/assets/62974484/d0f8f259-4006-4bf4-9f58-58ea5cc6f01e)
### <br/><br/><br/>

## master / slave 재등록시 에러났을 때
#### mysql 8 버전
```
stop slave;
reset slave;
start slave;
```
#### mysql 9 버전
```
stop replica;
reset replica;
start replica;
```
### <br/><br/><br/>

## ❗주의 사항
### * slave = slave mysql server, master = master mysql server 로 줄임
- slave 에서 작업하면 안 된다. master 에 반영이 안 된다. 
- slave 가 꺼졌는데 master 에서 먼가 변화가 있었고, 그 상태로 slave 를 연결하면 에러난다. slave 작업시에는 master 에서 table lock 을 걸고, 그 다음 dump 한 후, 다시 slave 로 연결한다.
### <br/><br/><br/>




