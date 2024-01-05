### 240105
## database 이중화
### 참고 블로그 / 웹사이트
#### https://jane096.github.io/project/mysql-master-slave-replication/
### <br/><br/><br/>

## 사용 이유
### 1. 쓰기 기능은 메인 서버에서 실행, 읽기 기능은 분산된 서버에서 수행하도록 함
### 2. 복제. database 의 안정성을 높인다.
### 3. 장애 극복. 특정 서버가 에러가 났을 때 다른 서버에서 기능하도록 하여 안정성을 높인다. 만약 master 가 에러가 났다면, slave 를 master 로 승격한다.
### <br/><br/><br/>

