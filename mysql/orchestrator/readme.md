### 250213
# MySQL orchestrator
### MySQL 고가용성 서버 운영을 위한 소프트웨어이다.
#### 나는 master-slave MySQL 서버의 고가용성(자동 복구)을 지원하기 위해 사용하기로 하였다.
#### MHA (master high availability)라는 툴도 있었지만, GUI을 지원하지 않고 사용 편의성 또한 orchestrator가 더 좋다고 하여 이걸로 결정하였다.
#### 다만 둘 다 최근 버전인 MySQL 9 버전과의 호환성을 보장할 수 없다고 한다.
#### [MySQL-고가용성-운영을-위한-Orchestrator-설치](https://sungwookkang.com/entry/MySQL-%EA%B3%A0%EA%B0%80%EC%9A%A9%EC%84%B1-%EC%9A%B4%EC%98%81%EC%9D%84-%EC%9C%84%ED%95%9C-Orchestrator-%EC%84%A4%EC%B9%98)
### <br/><br/><br/>

## orchestrator docker container 세팅
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

### <br/><br/><br/>

## 설정
### mysql에서 계정을 만들자. 각 mysql 서버 모두에 만들어줘야 한다.
```
CREATE USER 'orchestrator'@'localhost' IDENTIFIED BY 'orchestrator';
GRANT SUPER, PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'orchestrator'@'%';
FLUSH PRIVILEGES;
```
### <br/>

### orchestrator의 config 설정을 위해서 컨테이너를 다시 만들어줘야 한다. 
### orchestrator의 default config는 2가지가 있다. 각 환경에 맞춰서 업로드한 config 파일을 다운로드 해줘서 수정해준다.
#### ex) [orchestrator-sample-sqlite-ori.conf.json](https://github.com/Shin-jongwhan/mysql_and_sql/blob/main/mysql/orchestrator/orchestrator-sample-sqlite-ori.conf.json)
- orchestrator-sample.conf.json
  - orchestrator 전용 별도의 backend MySQL 서버를 이용하여 관리할 때 사용
- orchestrator-sample-sqlite.conf.json
  - 로컬에서 관리하도록 sqlite를 사용
### 기본 설정은 orchestrator-sample-sqlite.conf.json이다. 나는 별도 orchestrator 관리용 MySQL 서버를 구성하지 않을 것이기 때문에 이걸 이용한다.

### <br/>

### config를 바꿔줘야 한다.
### 아래 항목은 없으니 별도로 추가
```
"AutoPseudoGTID": true,
```
### <br/>

### 다음 항목은 mysql에서 생성한 계정으로 수정해준다.
```
"MySQLTopologyUser": "orchestrator",
"MySQLTopologyPassword": "orchestrator"
```
### <br/>

### 다음 항목은 mysql 도메인을 인식하기 위해서 수정해준다.
```
"HostnameResolveMethod": "none",
"MySQLHostnameResolveMethod": ""
```
### <br/>

### 이제 docker를 다시 실행해야 하는데, -v 옵션으로 수정한 config를 연결해준다.
```
# ex)
docker run -d -v /home/jhshin/script/docker/mysql_orchestrator/1.0.0/orchestrator-sample-sqlite.conf.json:/etc/orchestrator.conf.json --name orchestrator -p 3000:3000 openarkcode/orchestrator
```
### <br/>

### 연결 확인
### orchestrator 웹에서 clusters - discover에서 검색해서 submit을 눌러서 연결이 되는지 확인한다. 
#### ![image](https://github.com/user-attachments/assets/3f3f2a85-efd9-4175-9fe5-a1755eb17bfd)
### <br/>

### 연결이 되면 대시보드에 가면 하나 등록이 되어 있을 것이다. 클릭해보면 master - slave가 어떻게 등록이 되어 있는지(토폴로지 상태) 확인할 수 있다.
### clusters - dashboard
#### ![image](https://github.com/user-attachments/assets/ea3dfaab-ad74-4e6d-8b41-6d6f69d3d9d7)
#### ![image](https://github.com/user-attachments/assets/53fc164a-1926-42a7-bc44-3776cda1989c)
### home - status
#### 여기서 hostname은 orchesrator의 container id이다.
#### ![image](https://github.com/user-attachments/assets/f0328f88-c94f-42cc-bcd6-fdf4b5fa65b0)
#### ![image](https://github.com/user-attachments/assets/1ca2e27c-6e87-4b07-8981-420cf53e9572)

### <br/><br/><br/>

## orchestrator 대시보드 설정 및 상태 확인
#### ![image](https://github.com/user-attachments/assets/146d89d7-28a3-457a-8b7f-1155985481a7)
#### ![image](https://github.com/user-attachments/assets/163ab149-65ff-4463-82b5-0a3947f3cb1b)
### <br/>

### 임의로 slave를 꺼보았다. 모니터링이 잘 된다.
#### ![image](https://github.com/user-attachments/assets/3033f5b2-968b-42c2-8726-d2732a47d049)
### <br/>

### 서비스를 다시 켜봤더니 not replicating이라고 나타난다.
#### ![image](https://github.com/user-attachments/assets/c4e56f7c-056a-4c16-8079-d26fd6b4b611)

### <br/>

### slave 설정을 다시 하였다. orchestrator에서도 다시 복구가 된 모습을 확인할 수 있다.
#### 알아보니 모니터링이랑 master slave failover 기능만 있고 복구 기능은 없다고 한다.
#### 그래서 컨테이너 관리는 docker나 container orchestration tool을 이용하는 게 맞다.
#### ![image](https://github.com/user-attachments/assets/3dbb5e4c-8888-482b-8559-abf18e95d5e4)
#### ![image](https://github.com/user-attachments/assets/df09e9ef-827a-4d55-8616-64782d02409a)

