-- 코드를 입력하세요
SELECT car_id FROM CAR_RENTAL_COMPANY_CAR
where car_id in (SELECT car_id FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as A
                where A.start_date between '2022-10-01' and '2022-10-31')
                and car_type = '세단'
order by car_id desc