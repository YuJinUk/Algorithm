-- 코드를 입력하세요
SELECT year(sales_date) as YEAR,month(sales_date) as MONTH, GENDER, count(distinct(USER_INFO.user_id)) as USERS
from USER_INFO
join ONLINE_SALE on USER_INFO.USER_ID = ONLINE_SALE.USER_ID
where gender is not null
group by year(sales_date),month(sales_date), GENDER
order by year(sales_date) asc, month(sales_date) asc, GENDER asc;