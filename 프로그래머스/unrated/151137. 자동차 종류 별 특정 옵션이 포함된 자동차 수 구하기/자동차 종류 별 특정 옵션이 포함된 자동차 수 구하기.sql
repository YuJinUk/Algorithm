-- 코드를 입력하세요
SELECT CAR_TYPE , count(*) AS CARS FROM CAR_RENTAL_COMPANY_CAR A
WHERE A.OPTIONS LIKE '%시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE