import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.13",
  user="saurabh",
  password="saurabh123",
  database = 'mydb',
  port = '3306'
)

class DB:
    def __init__(self):
        self.mycursor= mydb.cursor()  
    
    
    # inserting tha values in the table
    def insertion(self,user_id,name,email,category):
        ins= "INSERT INTO users(user_id,name,email,category) VALUES(%s,%s,%s,%s)"
        val= (user_id,name,email,category)
        self.mycursor.execute(ins,val)
        mydb.commit()
        
    def get_users(self):
        db_query = " select * from users "
        self.mycursor.execute(db_query)
        myresult = self.mycursor.fetchall()
        return myresult
    
    def update_users(self,new_category,user_id):
        sql = 'UPDATE users SET category = %s WHERE user_id = %s'
        self.mycursor.execute(sql, (new_category, user_id))
        mydb.commit()


        
       
