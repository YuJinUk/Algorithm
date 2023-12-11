-- 코드를 입력하세요
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, p.price * sum(o.amount) as TOTAL_SALES
from food_order o
join food_product p
on p.product_id = o.product_id
where month(o.produce_date) = 05
group by o.product_id
order by TOTAL_SALES desc, PRODUCT_ID asc