-- 코드를 작성해주세요
select h.DEPT_ID, DEPT_NAME_EN, round(avg(sal)) as AVG_SAL from hr_department as h right join hr_employees as e on h.dept_id = e.dept_id group by dept_id order by AVG_SAL desc