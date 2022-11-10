import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='localhost', user='root', password='root',
                       db='test')
 
cur = con.cursor()

# 행 추가
sql = "insert into test (ID, name, age) VALUES (3, 'python', '5');"
cur.execute(sql)
rows = cur.fetchall()
con.commit()        # db 에 반영

sql = "select * from test;"
cur.execute(sql)
rows = cur.fetchall()
print(rows)

con.close()