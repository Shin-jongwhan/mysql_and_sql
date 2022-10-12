# [프로그래머스](https://school.programmers.co.kr)

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

