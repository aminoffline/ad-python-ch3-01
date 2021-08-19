import mysql.connector
from mysql.connector import errorcode

#DataBase_name = input('Name of DataBase: ')
DataBase_name = 'first_assignment'

config ={
    'user':'Amin',
    'password':'Adv@ncePyth0n',
    'host':'localhost',
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

def Create_database(name):
    sql = f'CREATE DATABASE IF NOT EXISTS {name}'
    cursor.execute(sql)

Tables = {}
Tables['Person'] = (
    "CREATE TABLE IF NOT EXISTS `Person` ("
    " `id` INT NOT NULL AUTO_INCREMENT,"
    " `name` VARCHAR (25) NOT NULL,"
    " `weight` INT (3) NOT NULL,"
    " `height` INT (3) NOT NULL,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")



def Create_Tables(Tables):
    cursor.execute(f'USE {DataBase_name}')
    for i in Tables:
        table = Tables[i]
        try:
            print(f"Creating table {i}")
            cursor.execute(table)
        except mysql.connector.Error as err:
            if err == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exist")
            else:
                print(err.msg)

Create_database(DataBase_name)
Create_Tables(Tables)