import mysql.connector

db_name = 'first_assignment'      #Data base name
user = 'Amin'                     #username in mysql
password = 'Adv@ncePyth0n'        #password
Table_name = 'person'             #name of table with our data in it
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
d = open('ordered data.txt','w')
for i,n,w,h in data:
    d.write(f"{n} {h} {w} \n")
    print(f"{n} {h} {w} ")
d.close()