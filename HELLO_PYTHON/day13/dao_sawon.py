import pymysql

class DaoSawon:
    def __init__(self):     # 생성자(__init__)
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def select(self):
        sql = "SELECT * FROM sawon"
        self.curs.execute(sql)
         
        rows = self.curs.fetchall()
        
        return rows
    
    def insert(self, s_name, age, address):
        sql = f"""
            INSERT INTO sawon 
                (s_name, age, address, in_date)
            VALUES
                ('{s_name}', '{age}', '{address}', DATE_FORMAT(NOW(), '%Y%m%d'))
        """
        cnt = self.curs.execute(sql)    
        
        self.conn.commit()
        
        return cnt
    
    def update(self, s_id, s_name, age, address):
        sql = f"""
            UPDATE sawon
            SET s_name = '{s_name}', 
                age = '{age}', 
                address = '{address}'
            WHERE s_id = '{s_id}'
        """
        cnt = self.curs.execute(sql)    
        
        self.conn.commit()
        
        return cnt
    
    def delete(self, s_id):
        sql = f"""
            DELETE FROM sawon 
            WHERE s_id = '{s_id}'
        """
        cnt = self.curs.execute(sql)    
        
        self.conn.commit()
        
        return cnt
        
    def __del__(self):      # 소멸자(__del__)
        self.curs.close()
        self.conn.close()

if __name__ == '__main__':
    de = DaoSawon()
    # de.select()
    # de.insert(e_id, e_name, age, sex, tel)
    # de.update(e_id, e_name, age, sex, tel)
    # de.delete(e_id)