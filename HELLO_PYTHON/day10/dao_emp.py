import pymysql

class DaoEmp:
    def __init__(self):     # 생성자(__init__)
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def select(self):
        sql = "SELECT * FROM emp"
        self.curs.execute(sql)
         
        rows = self.curs.fetchall()
        
        return rows
        
    def __del__(self):      # 소멸자(__del__)
        self.curs.close()
        self.conn.close()

if __name__ == '__main__':
    de = DaoEmp()
    list = de.select()
    print(list)