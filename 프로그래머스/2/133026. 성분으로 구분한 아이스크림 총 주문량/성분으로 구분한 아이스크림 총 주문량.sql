-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) as TOTAL_ORDER from icecream_info as i right join first_half as f on i.flavor = f.flavor group by ingredient_type order by total_order 