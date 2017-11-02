drop table if exists userTable;
create table userTable(
	id integer primary key autoincrement , 
	username string not null , 
	password string not null
);