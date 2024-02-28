-- 코드를 입력하세요
with recursive time as (
select 0 as hour
    union all
    select hour + 1 from time where hour < 23
)

SELECT t.hour, count(animal_id) from animal_outs as o right join time as t on t.hour = hour(o.datetime)
group by 1
order by 1