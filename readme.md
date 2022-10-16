# [프로그래머스](https://school.programmers.co.kr)

## 주의 사항
### 오라클과 MySQL 은 문법이 다르니 MySQL 선택해서 하기.
#### ![image](https://user-images.githubusercontent.com/62974484/195275760-70f88dce-5274-4986-8ab9-38ab4de29d78.png)

### <br/><br/><br/>

## 1
### 3월에 태어난 여성 회원 목록 출력하기
#### MEMBER_PROFILE 테이블에서 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문을 작성해주세요. 이때 전화번호가 NULL인 경우는 출력대상에서 제외시켜 주시고, 결과는 회원ID를 기준으로 오름차순 정렬해주세요.
#### ![image](https://user-images.githubusercontent.com/62974484/195250851-2888a8ef-e219-4881-9048-22ea56c712cf.png)
```
-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH FROM MEMBER_PROFILE
    WHERE MONTH(DATE_OF_BIRTH) = "3"
    AND TLNO IS NOT NULL
    AND GENDER = "W"
    ORDER BY MEMBER_ID
```

### <br/><br/><br/>

## 2
### 모든 레코드 조회하기
#### 동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.
#### ![image](https://user-images.githubusercontent.com/62974484/195251824-81cb0546-3ca6-4aa4-9613-5f807146eee9.png)
#### 
```
-- 코드를 입력하세요
-- SELECT * FROM ANIMAL_INS;
-- 컬럼 정보 조회
-- DESC ANIMAL_INS;
SELECT * FROM ANIMAL_INS
    ORDER BY ANIMAL_ID;
```

### <br/><br/><br/>

## 3
### 역순 정렬하기
#### 동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 ANIMAL_ID 역순으로 보여주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.
#### ![image](https://user-images.githubusercontent.com/62974484/195252290-f531ff2b-0a63-4d8d-a241-135694166356.png)
```
-- 코드를 입력하세요
SELECT NAME, DATETIME FROM ANIMAL_INS
    ORDER BY ANIMAL_ID DESC;
```

### <br/><br/><br/>

## 4
### 아픈 동물 찾기
#### 동물 보호소에 들어온 동물 중 아픈 동물의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
#### ![image](https://user-images.githubusercontent.com/62974484/195252648-9625f133-3823-4a77-b6b2-f34be1dcd43a.png)
```
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
    WHERE INTAKE_CONDITION = "Sick"
    ORDER BY ANIMAL_ID;
```

### <br/><br/><br/>

## 5
### 어린 동물 찾기
#### 동물 보호소에 들어온 동물 중 젊은 동물의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
#### ![image](https://user-images.githubusercontent.com/62974484/195253253-9ee16e03-d4b3-44bf-a88b-a6e76decf9f2.png)
```
-- 코드를 입력하세요
-- SELECT * FROM ANIMAL_INS;

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
    WHERE INTAKE_CONDITION != "Aged"
    ORDER BY ANIMAL_ID;
```

### <br/><br/><br/>

## 6
### 동물의 아이디와 이름
#### 동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.
```
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
    ORDER BY ANIMAL_ID;
```

### <br/><br/><br/>

## 7 
### 여러 기준으로 정렬하기
#### 동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.
#### ![image](https://user-images.githubusercontent.com/62974484/195254075-6714108c-c1f5-4c68-b09e-44a743b70d2a.png)
```
-- 코드를 입력하세요
-- ORDER BY 를 여러 개 쓸 때는 각 기준을 , 로 구분해서 쓴다. 가장 오른쪽부터 먼저 정렬 후에 가장 왼쪽을 마지막에 정렬한다.
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
    ORDER BY NAME, DATETIME DESC;
```

### <br/><br/><br/>

## 8 
### 상위 n개 레코드
#### 동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.
#### 
```
-- 코드를 입력하세요
-- LIMIT 은 맨 마지막에 쓴다. FROM ~ ORDER BY 이 중간에 쓰면 에러 난다.
-- LIMIT 10, 5; 와 같이 쓰면 10번째부터 5개 행을 가져온다.
SELECT NAME FROM ANIMAL_INS 
    ORDER BY DATETIME
    LIMIT 1;
```

### <br/><br/><br/>

## 9
### 가격이 제일 비싼 식품의 정보 출력하기
#### FOOD_PRODUCT 테이블에서 가격이 제일 비싼 식품의 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 조회하는 SQL문을 작성해주세요.
#### ![image](https://user-images.githubusercontent.com/62974484/195255189-1f6b279d-2236-4373-96ce-83204c3c0f2c.png)
```
-- 코드를 입력하세요
SELECT * FROM FOOD_PRODUCT
    ORDER BY PRICE DESC
    LIMIT 1;
```

### <br/><br/><br/>

## 10
### 최댓값 구하기
#### 가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
#### ![image](https://user-images.githubusercontent.com/62974484/195255629-c9fb3af3-2b8c-4ceb-839c-8fae850bf1fb.png)
```
-- 코드를 입력하세요
SELECT DATETIME FROM ANIMAL_INS
    ORDER BY DATETIME DESC
    LIMIT 1;
```

### <br/><br/><br/>

## 11
### 최솟값 구하기
#### 동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
```
-- 코드를 입력하세요
SELECT DATETIME FROM ANIMAL_INS
    ORDER BY DATETIME
    LIMIT 1;
```

### <br/><br/><br/>

## 12 
### 동물 수 구하기
#### 동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.
```
-- 코드를 입력하세요
-- 전체 테이블의 행의 개수를 구할 때는 COUNT(*) 를 이용한다. * 는 테이블의 모든 컬럼 조회.
SELECT COUNT(*) FROM ANIMAL_INS;
```

### <br/><br/><br/>

## 13 
### 중복 제거하기
#### 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.
```
-- 코드를 입력하세요
-- 중복을 제거할 때는 DISTINCT 를 이용한다.
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
    WHERE NAME IS NOT NULL;
```

### <br/><br/><br/>

## 14 
### 식품분류별 가장 비싼 식품의 정보 조회하기
#### FOOD_PRODUCT 테이블에서 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회하는 SQL문을 작성해주세요. 이때 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력시켜 주시고 결과는 식품 가격을 기준으로 내림차순 정렬해주세요.
#### ![image](https://user-images.githubusercontent.com/62974484/195260387-6e2ac9a4-9673-4214-b79a-422907611e06.png)
### 결과
#### ![image](https://user-images.githubusercontent.com/62974484/195263720-2cffcbf8-bd54-40e2-acb5-a6adb5072af9.png)
```
-- 코드를 입력하세요
-- 1
SELECT DISTINCT CATEGORY, PRICE, PRODUCT_NAME FROM FOOD_PRODUCT
    WHERE PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT WHERE CATEGORY = "과자") AND CATEGORY = "과자"
    OR PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT WHERE CATEGORY = "국") AND CATEGORY = "국"
    OR PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT WHERE CATEGORY = "김치") AND CATEGORY = "김치"
    OR PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT WHERE CATEGORY = "식용유") AND CATEGORY = "식용유"
    ORDER BY PRICE DESC

-- 2 : GROUP BY 활용
SELECT DISTINCT CATEGORY, PRICE, PRODUCT_NAME FROM FOOD_PRODUCT
    WHERE PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY)
    AND CATEGORY IN ('과자', '국', '김치', '식용유')
    ORDER BY PRICE DESC;

-- 1, 2 결과는 뭔가 부정확한 것 같다...
```

### <br/><br/><br/>

## 15
### 고양이와 개는 몇 마리 있을까
#### 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.
#### ![image](https://user-images.githubusercontent.com/62974484/195268896-5287059f-4a02-4447-aa21-f99c8efc8515.png)
### 결과
#### ![image](https://user-images.githubusercontent.com/62974484/195268861-f5c23544-d63b-4396-857b-5001daeaa495.png)
```
-- 코드를 입력하세요
-- ORDER BY 를 쓰면 정답이긴 하지만.. 고양이를 개보다 먼저 조회해달라는 말과 일치하지는 않아서.. 애매하다.
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) FROM ANIMAL_INS
    GROUP BY ANIMAL_TYPE
    HAVING ANIMAL_TYPE IN ('Cat', 'Dog')
    ORDER BY ANIMAL_TYPE;
```

### <br/><br/><br/>

## 16
### 동명 동물 수 찾기
#### 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
#### ![image](https://user-images.githubusercontent.com/62974484/195269366-354af286-10ff-4041-bdad-301b7737fbd0.png)
```
-- 코드를 입력하세요
SELECT NAME, COUNT(NAME) FROM ANIMAL_INS
    GROUP BY NAME
    HAVING COUNT(NAME) > 1
    AND NAME IS NOT NULL
    ORDER BY NAME;
```

### <br/><br/><br/>

## 17
### 입양 시각 구하기(1)
#### 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
### DATETIME 을 년, 월, 일, 시, 분, 초 추출 방법
```
-- SELECT YEAR(DATETIME), MONTH(DATETIME), DAY(DATETIME), HOUR(DATETIME), MINUTE(DATETIME), SECOND(DATETIME) FROM ANIMAL_OUTS 
SELECT HOUR(DATETIME), COUNT(*) FROM ANIMAL_OUTS
```
#### 
```
-- 코드를 입력하세요
    WHERE HOUR(DATETIME) BETWEEN 9 AND 19
    GROUP BY HOUR(DATETIME)
    ORDER BY HOUR(DATETIME);
```

### <br/><br/><br/>

## 18
### 입양 시각 구하기(2)
#### 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
### recursive 문의 구조 (while 이라고 생각하면 편함)
```
with recursive [테이블명] as (
    초기 SQL (select [컬럼명] ...) -- 여기서 [컬럼명] 은 [테이블명] 에 할당됨
    union all (or union) -- union 은 union distict 의 줄임말로 중복 결과를 제거해줌
    반복 조건 SQL (반복을 멈출 where 포함)
)
select [컬럼명] from [테이블명]
```
### recursive 로 0부터 23까지 작성 (= for i in rnage(0, 24) : print(i))
```
with recursive cte as (
    select 0 as HOUR
    union
    select HOUR + 1 from cte
    where HOUR < 23
)
select HOUR from cte
```
#### ![image](https://user-images.githubusercontent.com/62974484/195640158-b97938fa-a0cf-41d0-a99b-81aeecb1ebb1.png)
...
#### ![image](https://user-images.githubusercontent.com/62974484/195640217-436cb647-744c-4e67-8d9d-0af57a5ec27a.png)
### LEFT JOIN, ifnull() 을 통하여 0 값을 넣어준다.
```
with recursive cte as (
    select 0 as HOUR
    union
    select HOUR + 1 from cte
    where HOUR < 23
)
select A.HOUR, ifnull(B.count, 0) as COUNT from cte A
LEFT JOIN (
    select hour(DATETIME) as hour, count(ANIMAL_ID) as count
        from ANIMAL_OUTS 
        group by hour(DATETIME)
) B
on A.HOUR = B.hour
```
#### ![image](https://user-images.githubusercontent.com/62974484/195653332-6e042840-c9d9-4d83-b60d-c25186611826.png)

### <br/><br/><br/>

## 19
### 가격대 별 상품 개수 구하기
#### PRODUCT 테이블에서 만원 단위의 가격대 별로 상품 개수를 출력하는 SQL 문을 작성해주세요. 이때 컬럼명은 각각 컬럼명은 PRICE_GROUP, PRODUCTS로 지정해주시고 가격대 정보는 각 구간의 최소금액(10,000원 이상 ~ 20,000 미만인 구간인 경우 10,000)으로 표시해주세요. 결과는 가격대를 기준으로 오름차순 정렬해주세요.
```
SELECT truncate(PRICE, -4) as PRICE_GROUP, count(PRODUCT_CODE) as PRODUCTS FROM PRODUCT 
    GROUP BY PRICE_GROUP
    ORDER BY PRICE_GROUP
```
### 결과
#### ![image](https://user-images.githubusercontent.com/62974484/195982646-38365dd2-a3ee-4882-9326-85981d07f35d.png)

### <br/><br/><br/>

## 20
### 경기도에 위치한 식품창고 목록 출력하기
#### FOOD_WAREHOUSE 테이블에서 경기도에 위치한 창고의 ID, 이름, 주소, 냉동시설 여부를 조회하는 SQL문을 작성해주세요. 이때 냉동시설 여부가 NULL인 경우, 'N'으로 출력시켜 주시고 결과는 창고 ID를 기준으로 오름차순 정렬해주세요.
### 문자 포함 여부는 where ~ LIKE 를 사용한다.
- 'str%' 은 맨 앞 글자가 str 인 경우
- '%str' 은 맨 뒤 글자가 str 인 경우
- '%str%' 은 str을 포함하는 경우
```
-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, ifnull(FREEZER_YN, 'N') as FREEZER_YN FROM FOOD_WAREHOUSE 
    WHERE ADDRESS LIKE '%경기도%'
    ORDER BY WAREHOUSE_ID
```
### 결과
#### ![image](https://user-images.githubusercontent.com/62974484/195983000-6284f004-f965-446a-9a10-f885f396bf1a.png)

### <br/><br/><br/>

## 21
### IS NULL
#### 동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
```
-- 코드를 입력하세요
SELECT ANIMAL_ID FROM ANIMAL_INS 
    WHERE NAME is null
    ORDER BY ANIMAL_ID
```

### <br/><br/><br/>

## 22
### 이름이 있는 동물의 아이디(IS NOT NULL)
#### 동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
```
-- 코드를 입력하세요
SELECT ANIMAL_ID FROM ANIMAL_INS
    WHERE NAME is not null
    ORDER BY ANIMAL_ID
```

### <br/><br/><br/>

## 23
### NULL 처리하기
#### 입양 게시판에 동물 정보를 게시하려 합니다. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.
```
SELECT ANIMAL_TYPE, ifnull(NAME, 'No name') as NAME, SEX_UPON_INTAKE FROM ANIMAL_INS 
    ORDER BY ANIMAL_ID
```

### <br/><br/><br/>

## 24
### 나이 정보가 없는 회원 수 구하기
#### USER_INFO 테이블에서 나이 정보가 없는 회원이 몇 명인지 출력하는 SQL문을 작성해주세요. 이때 컬럼명은 USERS로 지정해주세요.
```
-- 코드를 입력하세요
SELECT count(USER_ID) as USERS FROM USER_INFO 
    WHERE AGE is null
```

### <br/><br/><br/>

## 25 어렵다..
### 그룹별 조건에 맞는 식당 목록 출력하기
#### MEMBER_PROFILE와 REST_REVIEW 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL문을 작성해주세요. 회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력되도록 작성해주시고, 결과는 리뷰 작성일을 기준으로 오름차순 정렬해주세요.
```
-- 정답 1
with A as (
    SELECT MEMBER_ID, COUNT(REVIEW_TEXT) as count FROM REST_REVIEW
        GROUP BY MEMBER_ID
        ORDER BY COUNT(REVIEW_TEXT) desc
        LIMIT 1
)
SELECT B.MEMBER_NAME, C.REVIEW_TEXT, date_format(C.REVIEW_DATE, '%Y-%m-%d') as date FROM A, MEMBER_PROFILE B, REST_REVIEW C
    WHERE C.MEMBER_ID = A.MEMBER_ID
    AND C.MEMBER_ID = B.MEMBER_ID
    ORDER BY date
```
```
-- 정답 2 (다른 사람 한 것 참고)
SELECT A.MEMBER_NAME, B.REVIEW_TEXT, date_format(B.REVIEW_DATE, '%Y-%m-%d')  as REVIEW_DATE
    FROM MEMBER_PROFILE  A, REST_REVIEW B
    WHERE A.MEMBER_ID = B.MEMBER_ID
    AND B.MEMBER_ID = (
        SELECT MEMBER_ID FROM REST_REVIEW
            GROUP BY MEMBER_ID
            ORDER BY count(MEMBER_ID) desc
            LIMIT 1
    )
    ORDER BY REVIEW_DATE
```
### 결과
#### ![image](https://user-images.githubusercontent.com/62974484/196000171-f4c76757-73a0-446d-8484-bcc66357c23d.png)

### <br/><br/><br/>

## 26
### 즐겨찾기가 가장 많은 식당 정보 출력하기
#### REST_INFO 테이블에서 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회하는 SQL문을 작성해주세요. 이때 결과는 음식 종류를 기준으로 내림차순 정렬해주세요.
```
-- 코드를 입력하세요
-- DESC REST_INFO

/* 데이터 확인 1
select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES FROM REST_INFO
    order by FAVORITES desc, FOOD_TYPE
*/

/* 데이터 확인 2
SELECT A.FOOD_TYPE, max(A.FAVORITES) FROM (
    SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES FROM REST_INFO
        group by FOOD_TYPE
        order by FOOD_TYPE desc, FAVORITES desc
) A
    group by A.FOOD_TYPE
*/
```

```
-- 정답
SELECT A.FOOD_TYPE, B.REST_ID, B.REST_NAME, A.FAVORITES FROM (
    SELECT FOOD_TYPE, REST_ID, REST_NAME, max(FAVORITES) as FAVORITES FROM REST_INFO
        group by FOOD_TYPE
        order by FOOD_TYPE desc, FAVORITES desc
) A
left join (select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES from REST_INFO) B
    on A.FOOD_TYPE = B.FOOD_TYPE and A.FAVORITES = B.FAVORITES
```
### 결과
#### ![image](https://user-images.githubusercontent.com/62974484/196025231-433404c5-1780-4709-99f3-fead4e33440a.png)

### <br/><br/><br/>

## 27
### 년, 월, 성별 별 상품 구매 회원 수 구하기
#### USER_INFO 테이블과 ONLINE_SALE 테이블에서 년, 월, 성별 별로 상품을 구매한 회원수를 집계하는 SQL문을 작성해주세요. 결과는 년, 월, 성별을 기준으로 오름차순 정렬해주세요. 이때, 성별 정보가 없는 경우 결과에서 제외해주세요.
#### 회원수는 같은 년, 월, 성별에 중복해서 구매한 회원수가 있어서 distinct A.USER_ID 로 해줘야 중복 결과를 삭제할 수 있다.
```
select year(A.SALES_DATE) as year, month(A.SALES_DATE) as month, B.GENDER, count(distinct A.USER_ID) as USERS from ONLINE_SALE A
left join (
    select * from USER_INFO
) B
    on A.USER_ID = B.USER_ID
    where B.GENDER is not null
    group by month, year, B.GENDER
    order by month, year, B.GENDER
```
### 결과
#### ![image](https://user-images.githubusercontent.com/62974484/196039560-373932ab-f3d6-4473-83ac-a21f30e18151.png)

### <br/><br/><br/>

## 28 
### 없어진 기록 찾기
#### ANIMAL_OUTS 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. ANIMAL_OUTS 테이블 구조는 다음과 같으며, ANIMAL_ID, ANIMAL_TYPE, DATETIME, NAME, SEX_UPON_OUTCOME는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다. ANIMAL_OUTS 테이블의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID의 외래 키입니다.
### 입양 기록은 있는데, 보호소 기록은 없는 것 확인
```
SELECT * from ANIMAL_INS A
right join (
    select * from ANIMAL_OUTS
) B
    on A.ANIMAL_ID = B.ANIMAL_ID
    where A.ANIMAL_ID is null
    order by B.ANIMAL_ID
```
#### ![image](https://user-images.githubusercontent.com/62974484/196040513-65faa75f-6c53-4f09-bd80-33bbead54cb1.png)
```
SELECT B.ANIMAL_ID, B.NAME from ANIMAL_INS A
right join (
    select * from ANIMAL_OUTS
) B
    on A.ANIMAL_ID = B.ANIMAL_ID
    where A.ANIMAL_ID is null
    order by B.ANIMAL_ID
```
### 결과
#### ![image](https://user-images.githubusercontent.com/62974484/196040548-76beefee-f9a5-4319-b7cb-8448d443e1f6.png)

### <br/><br/><br/>

## 28 
### 있었는데요 없었습니다
#### 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.
### 사전 확인
```
SELECT * from ANIMAL_INS A -- 보호소 정보
left join (
    select * from ANIMAL_OUTS -- 입양 정보
) B
    on A.ANIMAL_ID = B.ANIMAL_ID
    where B.ANIMAL_ID is not null
    and A.DATETIME > B.DATETIME
    order by A.DATETIME
```
#### ![image](https://user-images.githubusercontent.com/62974484/196041237-7d823623-4136-40b7-8f10-c2aca59ba734.png)
### 정답
```
SELECT A.ANIMAL_ID, B.NAME from ANIMAL_INS A -- 보호소 정보
left join (
    select * from ANIMAL_OUTS -- 입양 정보
) B
    on A.ANIMAL_ID = B.ANIMAL_ID
    where B.ANIMAL_ID is not null
    and A.DATETIME > B.DATETIME
    order by A.DATETIME
```
### 결과
#### ![image](https://user-images.githubusercontent.com/62974484/196041262-6ae77edf-ebd2-4759-9789-54ad88e122bb.png)

### <br/><br/><br/>

## 30
### 오랜 기간 보호한 동물(1)
#### 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.
```
SELECT A.NAME, A.DATETIME from ANIMAL_INS A -- 보호소 정보
left join (
    select * from ANIMAL_OUTS -- 입양 정보
) B
    on A.ANIMAL_ID = B.ANIMAL_ID
    where B.ANIMAL_ID is null
    order by A.DATETIME
    limit 3
```
### 결과
#### ![image](https://user-images.githubusercontent.com/62974484/196041450-8307cc6f-1dd7-4141-a6bc-036bd880314d.png)

### <br/><br/><br/>

## 31
### 가장 비싼 상품 구하기
#### PRODUCT 테이블에서 판매 중인 상품 중 가장 높은 판매가를 출력하는 SQL문을 작성해주세요. 이때 컬럼명은 MAX_PRICE로 지정해주세요.
```
-- 코드를 입력하세요
select price from PRODUCT 
    order by price desc
    limit 1
```
