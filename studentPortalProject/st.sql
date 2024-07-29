create database studentportal;
use studentportal;

create table STUDENT(
	F_name varchar(20),
    id varchar(20)  primary key,
    password varchar(20),
    Branch varchar(20)
);

create table queries(
	Application_id int primary key,
    F_name varchar(20),
    L_name varchar(20),
    Phone varchar(20),
    email varchar(40),
    query varchar(1000)
);
create table Admin(
	id int primary key,
    password varchar(20)
);
/* The below line is used when sql does not allow updating the current schema*/
set sql_safe_updates=0;
insert into STUDENT values("Gagan","497cs220177","214","Computer Science","Raj");
insert into Admin values(897,"IamAdmin");

