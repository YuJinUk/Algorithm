-- 코드를 입력하세요
SELECT f.flavor
from first_half f
join july j
on j.flavor = f.flavor
group by f.flavor
order by sum(j.total_order)+ f.total_order desc
limit 3