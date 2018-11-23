# DB connectivity in python (crl + alt+ H -> to display python source code)

import pymysql # To connect to mysql db

# connection(), cursor(), execute(), fetchone(),close()

con_obj =  pymysql.connect('localhost','demo','demo','test') # hostname, username, passwd, dbname

curso = con_obj.cursor()


print(curso.execute("SELECT * from myapp_publisher"))
#cursor.execute('insert books values (%s,%s,%s,%s)',('Py9099','Programming With Python',100,50))
#curso.execute("INSERT INTO myapp_publisher VALUES(%s,%s,%s,%s,%s,%s)",('apress','23th walmart st.','California','LA','US','http://www.apress.com'))

# data = curso.fetchone()
# print("See the data:",data)
#
# data1 = curso.fetchall()
# print("See all the data:",data1)

con_obj.commit()

curso.close()

'''Notes: only if select cmd is executed, fetching can be done, but for insert command, call commit to commit the changes to db'''