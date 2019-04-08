-- SQLite
select *
from students
inner join teams
on students.tid = teams.id;

select * FROM students;

select * from teams;

delete from teams where id = 'TeamB'