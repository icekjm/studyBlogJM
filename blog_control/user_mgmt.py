from flask_login import UserMixin
from db_model.mysql import comn_mysqldb

class User(UserMixin):
    
    def __init__(self, user_id, user_email, blog_id):
        self.id = user_id
        self.user_email = user_email
        self.blog_id = blog_id
        
    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get(user_id):
         mysql_db = comn_mysqldb()
         db_cursor = mysql_db.cursor()
         sql = "SELECT * FROM user_info WHERE USER_ID = '"+str(user_id)+"'"
         db_cursor.execute(sql)
         user = db_cursor.fetchone()
         if not user:
             return None
         
         
             
         
    
         
    