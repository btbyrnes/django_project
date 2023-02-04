select user from mysql.user;

drop user 'admindjango'@'localhost';

create user 'admindjango'@'localhost' identified by 'employee@123!';

grant create, select, insert, update, delete, drop on *.* to 'admindjango'@'localhost';

flush privileges;