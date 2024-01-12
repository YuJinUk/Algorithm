-- 코드를 입력하세요
SELECT A.PRODUCT_ID, B.PRODUCT_NAME, SUM(A.AMOUNT * B.PRICE) AS TOTAL_SALES FROM FOOD_ORDER A
JOIN FOOD_PRODUCT B ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE PRODUCE_DATE LIKE '%2022-05%'
GROUP BY A.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID












# SELECT p.PRODUCT_ID, p.PRODUCT_NAME, p.price * sum(o.amount) as TOTAL_SALES
# from food_order o
# join food_product p
# on p.product_id = o.product_id
# where month(o.produce_date) = 05
# group by o.product_id
# order by TOTAL_SALES desc, PRODUCT_ID asc