import pymysql

class DaoMovie:
    def __init__(self):     # 생성자(__init__)
        self.conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', port=3305, charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def insert(self, title, link, image, subtitle, pubdate, director, actor, userrating):
        sql = f"""
            INSERT INTO movie 
                (title, link, image, subtitle, pubdate, director, actor, userrating)
            VALUES
                ('{title}', '{link}', '{image}', '{subtitle}', '{pubdate}', '{director}', '{actor}', '{userrating}')
        """
        cnt = self.curs.execute(sql)    
        
        self.conn.commit()
        
        return cnt
        
    def __del__(self):      # 소멸자(__del__)
        self.curs.close()
        self.conn.close()

if __name__ == '__main__':
    de = DaoMovie()
