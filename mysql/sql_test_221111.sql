show tables;
show databases;
-- create database test;
use test;
/* create table test (
    ID int not null,
    name varchar(20) not null,
    age int not null,
    address char(50),
    salary decimal (18, 2),
    PRIMARY key(ID)
);
*/
desc test;
insert into test (ID, name, age) VALUES (1, 'jonghwan', '29');
-- OR
insert into test VALUES (2, 'jonghwan', '29', NULL, NULL);
select * from test;