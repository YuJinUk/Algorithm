-- 코드를 입력하세요
SELECT a.APNT_NO, p.PT_NAME, a.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD
from appointment a
join patient p
on a.pt_no = p.pt_no
join doctor d
on d.dr_id = a.mddr_id
where a.MCDP_CD = 'CS' and a.APNT_CNCL_YN = 'N' and date_format(a.APNT_YMD, '%Y-%m-%d') = '2022-04-13'
order by a.APNT_YMD