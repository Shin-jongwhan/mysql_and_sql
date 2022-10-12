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
