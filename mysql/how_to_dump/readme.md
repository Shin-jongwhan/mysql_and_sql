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
