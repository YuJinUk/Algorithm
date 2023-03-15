-- 코드를 입력하세요
select member_name, review_text, date_format(review_date, '%Y-%m-%d') as review_date
from rest_review
inner join (
    select member_id as join1_member_id, count(*) as count
    from rest_review
    group by member_id
    order by count desc
    limit 1
) join1 on rest_review.member_id = join1.join1_member_id
inner join (
    select member_id as join2_member_id, member_name
    from member_profile
) join2 on rest_review.member_id = join2.join2_member_id
order by review_date asc, review_text asc