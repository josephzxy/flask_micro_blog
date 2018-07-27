drop database if exists flask_blog_db;

create database flask_blog_db;
use flask_blog_db;

grant 
all privileges
on flask_blog_db.* 
to 'flask'@'localhost' identified by 'flask';

