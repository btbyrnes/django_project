import os

print("MYSQL_DATABASE ", os.environ.get('MYSQL_DATABASE', 'mysql-db'))
print("MYSQL_USER ", os.environ.get('MYSQL_USER', 'mysql-user'))
print("MYSQL_PASSWORD ", os.environ.get('MYSQL_PASSWORD', 'mysql-password'))
print("MYSQL_DATABASE_HOST ", os.environ.get('MYSQL_DATABASE_HOST'))
print("MYSQL_DATABASE_PORT ", os.environ.get('MYSQL_DATABASE_PORT', 3306))

# test a change