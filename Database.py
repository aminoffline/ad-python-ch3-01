import mysql.connector
from DB_Setup import  DataBase_name

db_name = DataBase_name
config ={
    'user':'Amin',
    'password':'Adv@ncePyth0n',
    'host':'localhost',
    'database':db_name
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

'''def Insert_Table(T_name,*values):
    sql = f'INSERT INTO {T_name} VALUES ({values})'
    cursor.execute(sql)
    db.commit()
'''

#Insert_Table('person','Amin',102,183)
def test(a,*b):
    print(type(a),type(b),len(b))


