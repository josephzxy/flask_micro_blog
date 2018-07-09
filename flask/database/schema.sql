drop database if exists flask_blog_db;

create database flask_blog_db;
use flask_blog_db;

grant 
index, create, select, update, insert, delete,
REFERENCES 
on flask_blog_db.* 
to 'flask'@'localhost' identified by 'flask';

