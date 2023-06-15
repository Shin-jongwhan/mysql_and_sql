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

