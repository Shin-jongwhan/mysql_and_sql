### 230717
## DB partitioning
### 테이블을 여러 단위로 나누는 방법이다. MySQL 에서 지원해준다.
### 한 컴퓨터 / 한 DB 내에서 쪼개는 것으로 조회하는 속도를 빠르게 한다.
### 다른 방법으로는 sharding 이라는 방법이 있다.
### sharding 은 여러 서버의 데이터베이스들에 나누어 데이터를 저장하는 방법이다(수평 파티셔닝의 일종이라고 할 수 있다).
#### https://hudi.blog/db-partitioning-and-sharding/
### <br/>

## partitioning 만드는 방법
### range partitioning
#### * 아래와 같이 하면 맨 마지막 파티션에 계속 쌓여서, 특정 value 마다 파티션을 새로 추가해주는 스케줄러를 구성해야 한다.
#### 주로 날짜로 구분하여 많이 쓴다.
```
alter table test partition by range(idx) (
  partition p10 values less than (10),
  partition p20 values less than maxvalue
);
```

### list partitioning
```
alter table test partition by list(mod(idx, 10)) (
  partition p_test_1 values in (0, 1),
  partition p_test_2 values in (2, 3),
  partition p_test_3 values in (4, 5),
  partition p_test_4 values in (6, 7),
  partition p_test_5 values in(8, 9)
);
```
### <br/>

## db partitioning 조회
```
select * from information_schema.partitions where table_name = 'test';
```
### LIST 로 써져 있고, 각각의 파티션에 몇 개의 row 가 들어가 있는지 확인할 수 있다.
#### ![image](https://github.com/Shin-jongwhan/mysql_and_sql/assets/62974484/2f959fbe-6250-4329-bdcc-b24dd0ce4ae7)
### <br/><br/><br/>
