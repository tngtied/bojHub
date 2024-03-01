-- 코드를 입력하세요

(select animal_type, count(animal_id) from animal_ins where animal_type = "Cat") union all (select animal_type, count(animal_id) from animal_ins where animal_type = "Dog") 