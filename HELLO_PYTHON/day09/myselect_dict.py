import pymysql

conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8')
 
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = """
    SELECT * 
    FROM emp
"""
curs.execute(sql)
 
rows = curs.fetchall()
print(rows)

curs.close()
conn.close()