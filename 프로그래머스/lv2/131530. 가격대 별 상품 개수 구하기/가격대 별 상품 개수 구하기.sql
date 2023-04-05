-- 코드를 입력하세요
set @price := -10000 ;

SELECT (@price := @price + 10000) as PRICE_GROUP, 
(select count(*) from PRODUCT where price < @price +10000 and price >= @price) as PRODUCTS
from PRODUCT
group by PRICE_GROUP
having PRODUCTS > 0
order by PRICE_GROUP;