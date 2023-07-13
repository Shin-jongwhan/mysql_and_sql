# 필요한 SQL 정리하는 곳
### <br/><br/><br/>

## foreign key 등록하는 방법, select 구문을 사용하여 insert 하는 방법
### foreign key 는 테이블 간 연결을 하기 위해서 사용한다.
### 다음과 같이 테이블을 구성한다고 해보자.
```
CREATE TABLE test (
    idx             INT NOT NULL AUTO_INCREMENT,
    name            VARCHAR(20) not null,
    PRIMARY KEY(idx)
);


CREATE TABLE test2 (
    idx             INT NOT NULL,
    score           INT,
    PRIMARY         KEY(idx),
    FOREIGN         KEY(idx) REFERENCES test(idx) ON UPDATE CASCADE
);
```
### 그리고 test 테이블에는 다음과 같이 데이터가 있다.
```
select * from test;
```
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql_test/assets/62974484/408ebb50-a2f3-4764-9e5a-dcb6be08a365)
### <br/>

### 원하는 foreign key 값을 입력하려면 select 구문을 같이 사용한다.
```
insert into test2 (idx, score) select idx, 90 from test where name = 'test';
```
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql_test/assets/62974484/8562587f-1c73-4ee5-9ca9-1bb6bd2ee1aa)
### <br/><br/><br/>

## DB, table 생성, 삭제
```
# db 생성
mysql> create database test character set UTF8;

# table 생성
mysql> CREATE TABLE test (
    idx             INT NOT NULL AUTO_INCREMENT,
    name            VARCHAR(20) not null,
    PRIMARY KEY(idx)
);

# database 삭제
mysql> drop database \[데이터베이스 명\];

# table 삭제
mysql> use test;    -- 이용할 db
mysql> drop table \[테이블 명\];
```
### <br/><br/><br/>

## 데이터 조회
```
# 테이블 컬럼 등 구조 조회
> desc \[테이블 명\]

# 자료 조회
> select * from \[테이블 명\]
```
### <br/><br/><br/>

## 행 추가(insert), 행 삭제(delete), 행 정보 수정(update)
```
# 행 추가(insert)
> insert into test (name) values ("test");

# 행 삭제(delete)
> delete from test where name="test";

# 행 정보 수정(where 절 안 들어가면 다 수정되니 주의)
> update test set name="test2" where name="test";
```
#### ![image](https://user-images.githubusercontent.com/62974484/210611950-f980b84f-84c2-4539-8973-318f9873a9ef.png)
### <br/><br/><br/>

## foreign key 체크 해제
### foreign key constrant fails 로 인해 값이 안 넣어진다면 0 으로 설정하면 값을 넣을 수 있다.
```
# 체크 해제
SET foreign_key_checks = 0;

# 체크 설정
SET foreign_key_checks = 1;
```
### <br/><br/><br/>

## 테이블 컬럼 수정
```
# 컬럼 추가
ALTER TABLE dbo.emp ADD email VARCHAR(25)

# 컬럼 수정
## 타입 수정 (modify 를 써도 되고, alter column 을 써도 된다)
## alter column
ALTER TABLE [table 명] ALTER COLUMN [컬럼 명] VARCHAR(100)
## modify
alter table rawdata_info modify total_balse bigint unsigned;

## foreign key 등록
alter table analysis_log add foreign key(analysis_idx_fk) references analysis(idx) on update cascade;
```
### <br/><br/><br/>

## 시간 차이 구하기
### 8.0 버전으로, 공식 홈페이지 문서를 참고한다.
#### https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_timediff
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql_test/assets/62974484/16264bb6-c3f3-4fe2-bb8f-f31ca31e49dc)
```
SELECT TIMESTAMPDIFF(MINUTE, NOW(), '2023-07-10 00:00:00.1') AS DateDiff;
```
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql_test/assets/62974484/42a0f583-a01d-40b7-855f-129b3fcc46e8)
### <br/><br/><br/>


