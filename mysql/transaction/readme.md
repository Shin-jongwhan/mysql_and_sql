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

## 사용 방법 (SQL)
- transaction 시작
  ```
  START TRANSACTION;
  ```
- 제출된 쿼리 반영 (commit)
  ```
  COMMIT;
  ```
- 제출된 쿼리에 문제가 있을 경우 반영 취소
  ```
  ROLLBACK;
  ```
### <br/><br/><br/>

## 사용 방법 (python)
### 파이썬의 pymysql 의 경우 execute(), commit(), rollback() 이 있다.
### execute 만 사용하는 경우 auto-commit 이 되지 않는다.
### mysqlclient 에서 사용하는 경우에도 똑같이 이용한다.
### <br/>
### 다만, mysqlclient 는 insert 한 쿼리의 index 를 제공하는 함수가 없고, 마지막으로 추가된 index 를 얻는 건 있다.
### pymysql 은 insert_id() 라는 함수를 제공한다.
### foreign key 정보를 얻어야 할 때 유용하다.
### ex)
```
def insert_sql(self, sTable, blAutocommit = True, **kwargs) :
      # Usage
      # ex)
      # analysis_info
      # insert_sql("analysis_info", **{'analysis_name' : "test", 'sample_info_file' : "test", 'server' : 'test', 'anal_data_dir' : "test", 'progress' : "pending"})
      #
      # insert_sql("analysis", **{'project' : "TBD230052", 'workid' : 17766, 'species' : "Human", 'library_kit' : "SureSelect XT Human All Exon V5 Kit", 'ftp_server' : "ftp.theragenbio.com", 'ftp_id' : "SNU_JSM", 'ftp_pw' : "dfkwhywhj23N!", 'requested_throughput' : 10, 'requested_read_length' : "NULL"})
      sColumns = ", ".join(list(kwargs.keys()))
      sValues = ""
      for i in list(kwargs.values()) :
          print(i, type(i))
          s = self.sql_text_type(i)
          if sValues == "" :
              sValues = "{0}".format(s)
          else :
              sValues += ", {0}".format(s)
      #sValues = ", ".join(list(map(lambda x : "\"{0}\"".format(x), list(kwargs.values()))))
      sql = """insert into {0}
          ({1})
          values
          ({2});
      """.format(sTable, sColumns, sValues)

      print(sql)
      self.cursor_bidev2.execute(sql)
      result = self.cursor_bidev2.fetchall()
      nRow_idx = self.connection_bidev2.insert_id()

      if blAutocommit == True :
          self.connection_bidev2.commit()
      print(result)

      return nRow_idx
```
