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

#### 230715
## with 예시
### 특정 값을 하나의 쿼리로 가져오는 것이 복잡할 경우 여러 쿼리를 연결하여 사용하는 구문이다.
### join 과는 다른 느낌
```
with A as (select count(*) as sample_num from rawdata_info where rawdata_info.analysis_idx_fk = 82), 
	B as (select analysis.* from analysis 
		right join analysis_log on analysis.idx = analysis_log.analysis_idx_fk group by analysis.idx) 
select * from A, B;
```
### <br/><br/><br/>


## case, when 예시
### case when 으로 조건을 걸어 좀 더 다양한 구문을 완성시킬 수 있다.
```
with
    A as (select * from analysis A left join (select count(sample_name) as sample_num, analysis_idx_fk from rawdata_info group by analysis_idx_fk) B on A.idx = B.analysis_idx_fk)
select                                                                                                                   A.project, A.workid, A.sample_num, analysis_log.analysis_name, analysis_log.scheduled_anal_name, analysis_log.progress, A.post_name from analysis_log, A
where
    (case
        when (select count(*) from analysis_log al where al.analysis_idx_fk = A.idx and al.progress = 'pending') = (select count(*) from analysis_log al where al.analysis_idx_fk = A.idx) then 0
        when (select count(*) from analysis_log al where al.analysis_idx_fk = A.idx and al.progress = 'in_progress') = 1 then (select al.analysis_priority from analysis_log al where al.analysis_idx_fk = A.idx and al.progress = 'in_progress')
        when (select count(*) from analysis_log al where al.analysis_idx_fk = A.idx and al.progress = 'error') = 1 then (select al.analysis_priority from analysis_log al where al.analysis_idx_fk = A.idx and al.progress = 'error')
        when (select count(*) from analysis_log al where al.analysis_idx_fk = A.idx and al.progress = 'complete') = (select count(*) from analysis_log al where al.analysis_idx_fk = A.idx) then (select al.analysis_priority from analysis_log al where al.analysis_idx_fk = A.idx and al.analysis_priority = (select max(analysis_priority) from analysis_log where analysis_log.analysis_idx_fk = A.idx))
        when (select count(*) from analysis_log al where al.analysis_idx_fk = A.idx and al.progress = 'complete') != (select count(*) from analysis_log al where al.analysis_idx_fk = A.idx) 
        	AND (select count(*) from analysis_log al where al.analysis_idx_fk = A.idx and al.progress = 'complete') >= 1 
        	then (select al.analysis_priority from analysis_log al where al.analysis_idx_fk = A.idx and al.analysis_priority = (select max(analysis_priority) from analysis_log where analysis_log.progress = 'complete' AND analysis_log.analysis_idx_fk = A.idx))
        else NULL end) = analysis_log.analysis_priority
    and analysis_log.analysis_idx_fk = A.idx;
```
### <br/><br/><br/>

## 다른 db 의 테이블에서 값 가져오기
### dev 서버를 publish 서버로 그대로 테이블 값을 옮긴다거나 할 때가 있다. 그럴 때 사용한다.
### join 을 활용한다.
```
update rine_reference A join workflow_dev.rine_reference B on A.reference_name = B.reference_name set A.backup_file = B.backup_file, A.backup_server = "bidev2" where A.reference_name = B.reference_name;
```
