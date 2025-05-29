create database project_rag_movies_qa;
use project_rag_movies_qa;

drop table comments;
drop table embedded_movies;
drop table movies;
drop table sessions;
drop table theaters;
drop table users;

SET GLOBAL max_allowed_packet = 67108864;  -- 64MB

select * from comments;
select * from embedded_movies;
select * from movies;
select * from sessions;
select * from theaters;
select * from users;