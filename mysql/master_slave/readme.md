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
