### 250724
# mysql slave 복구 자동화 시나리오
### 아래와 같은 워크플로우로 해야 한다.
1. table lock job
2. mysqldump. dump 파일을 slave에서도 쓸 수 있도록 scp를 하는 등으로 전달.
    ```
    mysqldump -uroot -proot --databases $(mysql -uroot -proot -Nse "SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('mysql','performance_schema','information_schema','sys')") > /data/mysql/tgf/backup/test.sql
    ```
4. mysql slave pod (또는 container) 실행
5. dump한 거 import
6. slave 설정
    - mysql master에서 relay bin 값 등 조회해서 가져오기
    - mysql slave 설정
7. table lock 해제
