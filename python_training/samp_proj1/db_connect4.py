# Updating the data

import pymysql

db = pymysql.connect("localhost","demo","demo","test")

cursor = db.cursor()

sql = "update pets set age = age + 1 where age > 12"

try:
    cursor.execute(sql)
    db.commit()

except:
    db.rollback()

db.close()