### 250213
# MySQL orchestrator
### MySQL 고가용성 서버 운영을 위한 소프트웨어이다.
#### 나는 master-slave MySQL 서버의 고가용성(자동 복구)을 지원하기 위해 사용하기로 하였다.
#### MHA (master high availability)라는 툴도 있었지만, GUI을 지원하지 않고 사용 편의성 또한 orchestrator가 더 좋다고 하여 이걸로 결정하였다.
#### 다만 둘 다 최근 버전인 MySQL 9 버전과의 호환성을 보장할 수 없다고 한다.
#### [MySQL-고가용성-운영을-위한-Orchestrator-설치](https://sungwookkang.com/entry/MySQL-%EA%B3%A0%EA%B0%80%EC%9A%A9%EC%84%B1-%EC%9A%B4%EC%98%81%EC%9D%84-%EC%9C%84%ED%95%9C-Orchestrator-%EC%84%A4%EC%B9%98)
### <br/><br/><br/>

## docker container 세팅
### 나는 docker container를 이용해보기로 하였다.
### orchestrator의 기본 포트는 3000이다.
### <br/>

### container 배포 버전이 있다.
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

### config 설정을 위해서 컨테이너를 다시 만들어줘야 한다. 
### orchestrator의 default config는 2가지가 있다.
- orchestrator-sample.conf.json
  - orchestrator 전용 별도의 backend MySQL 서버를 이용하여 관리할 때 사용
- orchestrator-sample-sqlite.conf.json
  - 로컬에서 관리하도록 sqlite를 사용
### 기본 설정은 orchestrator-sample-sqlite.conf.json이다. 나는 별도 orchestrator 관리용 MySQL 서버를 구성하지 않을 것이기 때문에 이걸 이용한다.
