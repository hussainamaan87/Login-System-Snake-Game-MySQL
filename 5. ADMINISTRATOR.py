a=input("ENTER YOUR MYSQL USER ID:")
b=input("ENTER YOUR MYSQL PASSWORD")


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user=a,
  password=b,
  database="ard_games"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user_accounts")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
