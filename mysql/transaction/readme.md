### 230817
## DB transaction
### transaction 은 insert, delete, update 를 할 때 데이터 무결성을 체크하기 위해서 있는 기능이다.
### 테이블들에 무언가 데이터를 조작해야 할 때, 하나의 묶음으로 성공하게 해야 한다면 transaction 을 사용해야 한다.
### <br/><br/><br/>

## transaction 은 언제 써야 할까
### 연관된 테이블의 정보가 같이 수정되어야 할 때 사용한다.
### 1. table A, table B 가 있고 두 테이블에 값이 insert 가 되어야 하는데 A, B 둘 다 되어야 하는 걸 체크해야 할 때
### 2. 여러 테이블을 update 해야 하는데, 하나의 정보가 바뀌는 것이 아닌 연관된 테이블 정보들이 같이 바뀌어야 할 때
### <br/><br/><br/>

