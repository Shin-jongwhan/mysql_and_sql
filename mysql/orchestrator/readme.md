### 250213
# MySQL orchestrator
### MySQL 고가용성 서버 운영을 위한 소프트웨어이다.
#### 나는 master-slave MySQL 서버의 고가용성(자동 복구)을 지원하기 위해 사용하기로 하였다.
#### MHA (master high availability)라는 툴도 있었지만, GUI을 지원하지 않고 사용 편의성 또한 orchestrator가 더 좋다고 하여 이걸로 결정하였다.
#### 다만 둘 다 최근 버전인 MySQL 9 버전과의 호환성을 보장할 수 없다고 한다.
### <br/><br/><br/>

## docker container
### 나는 docker container를 이용해보기로 하였다.
### orchestrator의 기본 포트는 3000이다.
```
docker run -d --name orchestrator -p 3000:3000 openarkcode/orchestrator
```
### <br/>

### 일단 브라우저에서 접속은 잘 된다. 그런데 아직 등록된 토폴로지(mysql 서버들)가 없다.
```
# 브라우저에 입력하여 접속
[domain / ip]:3000
```
#### ![image](https://github.com/user-attachments/assets/e57806fe-e1e1-428a-b6a8-a9d48faeb3fc)
### <br/>

### mysql에서 계정을 만들자. 각 mysql 서버 모두에 만들어줘야 한다.
```
CREATE USER 'orchestrator'@'localhost' IDENTIFIED BY 'orchestrator';
GRANT SUPER, PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'orchestrator'@'%';
FLUSH PRIVILEGES;
```
### <br/>

