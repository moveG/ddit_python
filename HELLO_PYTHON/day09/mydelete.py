import pymysql

conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8')
 
curs = conn.cursor()

sql = """
    DELETE FROM emp 
    WHERE e_id = %s
"""

cnt = curs.execute(sql, '4')
print("cnt", cnt)

conn.commit()

curs.close()
conn.close()