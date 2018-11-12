
import pymysql

db = pymysql.connect("localhost",'demo','demo','test')

cursor = db.cursor()

age = int(input("Enter the age"))

sql = "SELECT * FROM pets WHERE age < %d" % (age)

try:
    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:
        name = row[0]
        owner = row[1]

        print("name=%s, owner=%s" % (name, owner))
except:
    print("Error: Unable to fetch data")

db.close()