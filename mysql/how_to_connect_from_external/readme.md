### 240105
## 외부 접속 허용 방법
### 1. database 생성
```
create database test;
```
### <br/>

### 2. 유저 생성
#### 데이터베이스 변경, 유저 생성 및 확인
```
use mysql
reate user 'test'@'%' identified by 'test';
select host, user from user;
```

#### 변경 사항 적용
```
flush privileges;
```

#### 권한 확인, 주기
```
show grants for 'test_user'@'%';
grant all privileges on test.* to test@'%';
show grants for 'test'@'%';
```
### <br/>

### 3. 외부에서 접속해보기
```
mysql -u test -h [ip 주소] -p
```
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql/assets/62974484/fcaeefe6-7d08-4a51-afc4-2761177bcd0c)
