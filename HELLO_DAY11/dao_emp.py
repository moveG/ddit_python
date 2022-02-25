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
    
    def insert(self, e_id, e_name, age, sex, tel):
        sql = f"""
            INSERT INTO emp 
                (e_id, e_name, age, sex, tel)
            VALUES
                ('{e_id}', '{e_name}', '{age}', '{sex}', '{tel}')
        """
        cnt = self.curs.execute(sql)    
        
        self.conn.commit()
        
        return cnt
    
    def update(self, e_id, e_name, age, sex, tel):
        sql = f"""
            UPDATE emp 
            SET e_name = '{e_name}', 
                age = '{age}', 
                sex = '{sex}', 
                tel = '{tel}' 
            WHERE e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)    
        
        self.conn.commit()
        
        return cnt
    
    def delete(self, e_id):
        sql = f"""
            DELETE FROM emp 
            WHERE e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)    
        
        self.conn.commit()
        
        return cnt
        
    def __del__(self):      # 소멸자(__del__)
        self.curs.close()
        self.conn.close()

if __name__ == '__main__':
    de = DaoEmp()
    # de.select()
    # de.insert(e_id, e_name, age, sex, tel)
    # de.update(e_id, e_name, age, sex, tel)
    # de.delete(e_id)