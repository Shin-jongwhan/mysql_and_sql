### 240105
## docker 에서 처음으로 mysql 실행 시 에러가 났을 때
### docker hub
#### https://hub.docker.com/repository/docker/shinejh0528/mysql/general
### <br/>

### 1. mysql init 
```
mysqld --initialize
```
### <br/>

### 2. service start
### 이렇게 하면 아직 error 가 발생하지만 datadir 쪽에 데이터는 생성이 되고 있을 것이다.
```
service mysql start
```
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql/assets/62974484/c7a3d630-9f6c-4fcf-b223-391dd9844016)
### <br/>

### 3. 그룹, 권한을 mysql 에게 넘겨주기
```
chown -R mysql:mysql /data/mysql
```
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql/assets/62974484/c4ec5ba6-d47b-486d-a6af-428312bc7d61)
### <br/>

### 4. service start 
```
service mysql start
```
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql/assets/62974484/72937b05-c9b5-4dbd-8844-d3e16caa2971)
### <br/>
