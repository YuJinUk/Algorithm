-- 코드를 입력하세요
SELECT i.animal_id as ANIMAL_ID, i.animal_type as ANIMAL_TYPE, i.NAME
from animal_ins i
join animal_outs o
on i.animal_id = o.animal_id
where i.sex_upon_intake like 'intact %' and o.sex_upon_outcome not like 'intact %'