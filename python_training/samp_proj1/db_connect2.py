
import pymysql

db = pymysql.connect("localhost","demo","demo","test")

cursor = db.cursor()

sql = "INSERT INTO pets(name, owner,age) VALUES ('%s','%s','%d')" %('Mac','Mohan',20)
sql1 = "INSERT INTO pets(name, owner,age) VALUES ('%s','%s','%d')" %('Jim','Karan',24)

try:
    cursor.execute(sql)
    cursor.execute(sql1)

except:
    db.rollback()

else:
    db.commit()

db.close()