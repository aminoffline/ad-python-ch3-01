import mysql.connector

db_name = 'first_assignment'
user = 'Amin'
password = 'Adv@ncePyth0n'
Table_name = 'person'
config ={
    'user':user,
    'password': password,
    'host':'localhost',
    'database':db_name
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

sql = F"SELECT * FROM {Table_name} ORDER BY height DESC ,weight DESC "
cursor.execute(sql)
data = cursor
for i,n,w,h in data:
    print(f"{n} {h} {w} ")