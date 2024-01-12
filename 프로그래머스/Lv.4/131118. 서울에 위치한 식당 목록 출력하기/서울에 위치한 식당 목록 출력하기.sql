-- 코드를 입력하세요
SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, ROUND(AVG(B.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO A
JOIN REST_REVIEW B ON A.REST_ID = B.REST_ID
WHERE A.ADDRESS LIKE '서울%'
GROUP BY A.REST_NAME
ORDER BY SCORE DESC, A.FAVORITES DESC
















# SELECT i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, round(avg(r.review_score),2) as score
# from rest_info i
# join rest_review r
# on i.rest_id = r.rest_id
# where i.address like '서울%'
# group by i.rest_name
# order by score desc, i.favorites desc