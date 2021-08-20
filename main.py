from Database import  cursor, Insert_Table

Table_name = 'person'
keys = ['name','weight','height']
l = open('data.txt','r')
list = l.readlines()
l.close()
for i in list:
    j = i.split(sep=' ')
    j[2] = j[2].replace("\n","")
    val = [j[0],int(j[1]),int(j[2])]
    Insert_Table(Table_name,keys,val)

sql = F"SELECT * FROM {Table_name} ORDER BY height DESC ,weight DESC "
cursor.execute(sql)
data = cursor
d = open('ordered data.txt','w')
for i,n,w,h in data:
    d.write(f"{n} {h} {w} \n")
    print(f"{n} {h} {w} ")
d.close()