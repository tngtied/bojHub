-- 코드를 입력하세요
SELECT i.animal_id, i.name
from ANIMAL_INS as i inner join animal_outs as o on i.animal_id = o.animal_id
order by timestampdiff(day, i.datetime, o.datetime) desc
limit 2;