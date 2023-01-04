------------------------------------------------------------

# 221113
# mysql 다중 서버 만드는 방법
## mysqld_multi 를 사용하여 만든다.
### mysql 을 설치할 때 같이 설치되는 프로그램이다.
### <br/><br/><br/>

## cnf 파일 설정
### mysqld_multi --example 을 실행하면 예시 파일을 만들어준다.
- socket : 모두 다른 socket 을 가지고 있어야 한다.
- port : mysql 의 기본 포트는 3306 으로 다른 걸 3307 등 다른 걸 써야 한다.
  - 열린 port 확인 방법
    - netstat -tnlp
    - lsof -i
  #### ![image](https://user-images.githubusercontent.com/62974484/201509163-3fb7020b-ccca-4b8b-8ca8-8bcd75a4654a.png)
### <br/>

- pid-file : datadir 안에 넣어주면 된다.
- datadir : 자신의 새로운 db 디렉터리. 빈 폴더를 하나 만들어주고 등록한다.
- language : mysql 을 설치할 때 만들어주는데, 없으면 새로 설치해준다.
- user : 
```
# This is an example of a my.cnf file for mysqld_multi.
# Usually this file is located in home dir ~/.my.cnf or /etc/my.cnf
#
# SOME IMPORTANT NOTES FOLLOW:
#
# 1.COMMON USER
#
#   Make sure that the MySQL user, who is stopping the mysqld services, has
#   the same password to all MySQL servers being accessed by mysqld_multi.
#   This user needs to have the 'Shutdown_priv' -privilege, but for security
#   reasons should have no other privileges. It is advised that you create a
#   common 'multi_admin' user for all MySQL servers being controlled by
#   mysqld_multi. Here is an example how to do it:
#
#   GRANT SHUTDOWN ON *.* TO multi_admin@localhost IDENTIFIED BY 'password'
#
#   You will need to apply the above to all MySQL servers that are being
#   controlled by mysqld_multi. 'multi_admin' will shutdown the servers
#   using 'mysqladmin' -binary, when 'mysqld_multi stop' is being called.
#
# 2.PID-FILE
#
#   If you are using mysqld_safe to start mysqld, make sure that every
#   MySQL server has a separate pid-file. In order to use mysqld_safe
#   via mysqld_multi, you need to use two options:
#
#   mysqld=/path/to/mysqld_safe
#   ledir=/path/to/mysqld-binary/
#
#   ledir (library executable directory), is an option that only mysqld_safe
#   accepts, so you will get an error if you try to pass it to mysqld directly.
#   For this reason you might want to use the above options within [mysqld#]
#   group directly.
#
# 3.DATA DIRECTORY
#
#   It is NOT advised to run many MySQL servers within the same data directory.
#   You can do so, but please make sure to understand and deal with the
#   underlying caveats. In short they are:
#   - Speed penalty
#   - Risk of table/data corruption
#   - Data synchronising problems between the running servers
#   - Heavily media (disk) bound
#   - Relies on the system (external) file locking
#   - Is not applicable with all table types. (Such as InnoDB)
#     Trying so will end up with undesirable results.
#
# 4.TCP/IP Port
#
#   Every server requires one and it must be unique.
#
# 5.[mysqld#] Groups
#
#   In the example below the first and the fifth mysqld group was
#   intentionally left out. You may have 'gaps' in the config file. This
#   gives you more flexibility.
#
# 6.MySQL Server User
#
#   You can pass the user=... option inside [mysqld#] groups. This
#   can be very handy in some cases, but then you need to run mysqld_multi
#   as UNIX root.
#
# 7.A Start-up Manage Script for mysqld_multi
#
#   In the recent MySQL distributions you can find a file called
#   mysqld_multi.server.sh. It is a wrapper for mysqld_multi. This can
#   be used to start and stop multiple servers during boot and shutdown.
#
#   You can place the file in /etc/init.d/mysqld_multi.server.sh and
#   make the needed symbolic links to it from various run levels
#   (as per Linux/Unix standard). You may even replace the
#   /etc/init.d/mysql.server script with it.
#
#   Before using, you must create a my.cnf file either in /TBI/People/tbi/jhshin/miniconda3/my.cnf
#   or /root/.my.cnf and add the [mysqld_multi] and [mysqld#] groups.
#
#   The script can be found from support-files/mysqld_multi.server.sh
#   in MySQL distribution. (Verify the script before using)
#

[mysqld_multi]
mysqld     = /TBI/People/tbi/jhshin/miniconda3/bin/mysqld_safe
mysqladmin = /TBI/People/tbi/jhshin/miniconda3/bin/mysqladmin
user       = multi_admin
password   = my_password

[mysqld2]
socket     = /tmp/mysql.sock2
port       = 3307
pid-file   = /TBI/People/tbi/jhshin/miniconda3/data2/hostname.pid2
datadir    = /TBI/People/tbi/jhshin/miniconda3/data2
language   = /TBI/People/tbi/jhshin/miniconda3/share/mysql/mysql/english
user       = unix_user1

[mysqld3]
mysqld     = /path/to/mysqld_safe
ledir      = /path/to/mysqld-binary/
mysqladmin = /path/to/mysqladmin
socket     = /tmp/mysql.sock3
port       = 3308
pid-file   = /TBI/People/tbi/jhshin/miniconda3/data3/hostname.pid3
datadir    = /TBI/People/tbi/jhshin/miniconda3/data3
language   = /TBI/People/tbi/jhshin/miniconda3/share/mysql/mysql/swedish
user       = unix_user2

[mysqld4]
socket     = /tmp/mysql.sock4
port       = 3309
pid-file   = /TBI/People/tbi/jhshin/miniconda3/data4/hostname.pid4
datadir    = /TBI/People/tbi/jhshin/miniconda3/data4
language   = /TBI/People/tbi/jhshin/miniconda3/share/mysql/mysql/estonia
user       = unix_user3

[mysqld6]
socket     = /tmp/mysql.sock6
port       = 3311
pid-file   = /TBI/People/tbi/jhshin/miniconda3/data6/hostname.pid6
datadir    = /TBI/People/tbi/jhshin/miniconda3/data6
language   = /TBI/People/tbi/jhshin/miniconda3/share/mysql/mysql/japanese
user       = unix_user4
```
### <br/>

### my.cnf 저장 경로
#### which mysqld_multi 로 위치 찾은 다음 vi 로 켜서 어디에 저장해야 하는지 본다.
#### /TBI/People/tbi/jhshin/miniconda3/etc/my.cnf
#### ![image](https://user-images.githubusercontent.com/62974484/201509326-a026bd78-a18e-4b79-9095-b05648c5e86a.png)
### <br/><br/><br/>


## mysqld_multi 실행
### 2와 같이 숫자를 써주면 \[mysqld2\] 가 실행된다.
### 숫자를 안 써주면 모든 mysqld 가 실행된다.
### user 와 password 를 써준다. 
### 권장사항으로 처음 시작할 때는 --verbose 옵션을 넣어주고 어떤 내용들이 있는지 꼭 확인한다.
```
$ mysqld_multi --user=jhshin --password=jhshin --verbose start 2
```
### <br/>

### 실행이 잘 되면 datadir 에 파일들이 생긴다.
### 그리고 mysqld 가 잘 실행되고 있는 것을 체크한다.
#### ![image](https://user-images.githubusercontent.com/62974484/201509455-2fae97f0-8eb7-4f64-a273-1a023a3f8322.png)
#### ![image](https://user-images.githubusercontent.com/62974484/201509484-fa82a97a-cc30-4988-8cce-01342f0f21b5.png)
### <br/>

### 첫 실행 시 꼭 root 의 초기 비밀번호를 확인한다 !
#### ![image](https://user-images.githubusercontent.com/62974484/201509538-b1afb817-d22a-4330-a39c-2f6c02d50408.png)
### <br/><br/><br/>


## 접속
### $ mysql -uroot -S /tmp/mysql.sock2 -p 를 입력하고 초기 비밀번호를 입력한다.
### 정상 접속됐을 때는 아래와 같이 나온다.
#### ![image](https://user-images.githubusercontent.com/62974484/201509613-ccdb4f2d-b4b1-4f1b-be17-4b928f21c4d4.png)
### <br/>

### root 초기 비밀번호 변경
```
-- 초기 비밀번호 변경
mysql> alter user 'root'@'localhost' identified with mysql_native_password by 'new_password_you_want';

-- 외부 접속 시 IP 및 비밀번호 설정 
mysql> create user 'root'@'192.168.0.100' identified with mysql_native_password by 'new_password_you_want';

-- 외부 접속을 모두 허용
mysql> create user 'root'@'%' identified with mysql_native_password by 'root';
-- 또는
mysql> grant all privileges on *.* to 'root'@'%' identified by 'root';

-- 권한 변경 사항 적용
mysql> flush privileges;
```
### <br/><br/><br/>

## 다른 서버에서 접속 확인
```
import pymysql.cursors

def main() :
    # Connect to the database
    # host_name or ip 는 실행 중인 서버를 넣는다.
    connection = pymysql.connect(host='host_name or ip',
            port=3307,
            user='root',
            password='root',
            database='mysql',
            cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    sql = "show tables;"
    cursor.execute(sql)
    result = cursor.fetchall()

    print(result)

main()
```
#### ![image](https://user-images.githubusercontent.com/62974484/201509847-642e4b90-d1fd-4bc6-89c2-b713d41f27bd.png)
### <br/><br/><br/>

### DB, table 생성, 삭제
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

### 행 추가(insert), 행 삭제(delete), 행 정보 수정(update)
```
# 행 추가(insert)
> insert into test (name) values ("test");

# 행 삭제(delete)
> delete from test where name="test";

# 행 정보 수정(where 절 안 들어가면 다 수정되니 주의)
> update test set name="test2" where name="test";
```






------------------------------------------------------------
