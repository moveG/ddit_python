import pymysql

conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8')
 
curs = conn.cursor()

sql = """
    UPDATE emp 
    SET e_name = %s, 
        age = %s, 
        sex = %s, 
        tel = %s 
    WHERE e_id = %s
"""

cnt = curs.execute(sql, ('8', '8', '8', '8', '7'))
print("cnt", cnt)

conn.commit()

curs.close()
conn.close()