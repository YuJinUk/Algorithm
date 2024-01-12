-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE LIKE '%INTACT%'
AND
B.SEX_UPON_OUTCOME NOT LIKE '%INTACT%'
ORDER BY A.ANIMAL_ID














# SELECT i.animal_id as ANIMAL_ID, i.animal_type as ANIMAL_TYPE, i.NAME
# from animal_ins i
# join animal_outs o
# on i.animal_id = o.animal_id
# where i.sex_upon_intake like 'intact %' and o.sex_upon_outcome not like 'intact %'