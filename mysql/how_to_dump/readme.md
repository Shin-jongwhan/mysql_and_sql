### 240108
## 다른 서버로 dump 방법
### dump 하기 전에 먼저 db 에 변경 사항이 적용이 안 되도록 lock
```
flush tables with read lock;
```
### <br/> 

### db dump
```
mysqldump -u [user] -p [db] > [file_name].sql
```
### <br/>

### dump.sql 을 dump 할 서버로 복사
```
scp [file_name].sql jhshin@[server]:[path]
```
### <br/>

### dump 할 서버에서 mysql 들어가서 db 를 만든다. 만약 이미 database가 있으면 drop 하고 수행
#### drop database
```
drop database [db]
```
#### create database
```
create database [db]
```
### <br/>

### import 
#### * dump 할 때는 보통 root 를 쓴다.
```
mysql -u [user] -p [db] < [file_name].sql
```
### <br/>

### unlock
```
unlock tables;
```
