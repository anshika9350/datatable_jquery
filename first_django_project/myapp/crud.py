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
        
    def read(self):
      reads = "select * from users"
      self.mycursor.execute(reads)
      results = self.mycursor.fetchall()
      
      return results
