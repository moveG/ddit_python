import pymysql

conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8')
 
curs = conn.cursor()

sql = """
    INSERT INTO emp 
        (e_id, e_name, age, sex, tel)
    VALUES
        (%s, %s, %s, %s, %s)
"""

cnt = curs.execute(sql, ('7', '7', '7', '7', '7'))
print("cnt", cnt)

conn.commit()

curs.close()
conn.close()