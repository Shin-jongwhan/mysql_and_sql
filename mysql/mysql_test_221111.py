import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='localhost', user='root', password='root',
                       db='world')
 
cur = con.cursor()
sql = "show tables;"
cur.execute(sql)
 
rows = cur.fetchall()
print(rows)

con.close()