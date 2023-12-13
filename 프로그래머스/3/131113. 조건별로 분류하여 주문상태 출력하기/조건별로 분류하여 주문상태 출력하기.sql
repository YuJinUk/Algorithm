-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, '%Y-%m-%d') as OUT_DATE,
CASE
WHEN(DATEDIFF('2022-05-01', OUT_DATE)>=0) THEN '출고완료'
WHEN(DATEDIFF('2022-05-01', OUT_DATE)<0) THEN '출고대기'
ELSE '출고미정'
END AS '출고여부'
from food_order
order by order_id asc