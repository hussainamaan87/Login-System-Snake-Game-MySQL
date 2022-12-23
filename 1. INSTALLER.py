def Create_Database_Airlines():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234')    
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="create database ARD_GAMES"
    cursor.execute(s1)
    print("Database Created")

def connection():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='ARD_GAMES')
    if mycon.is_connected():
        print("Successfully Connected to Database")
    else:
        print("Connection Not Established")
        print("Reason for Error")
        print("1. Mysql Connector not installed or not updated")
        print("2. User name or password for MySql is invalid")
        print("3. Hardware Requirements Missing")
        print("Ending the Program")

def user_accounts_table():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='ARD_GAMES')
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="create table user_accounts(fname varchar(100),lname varchar(100),email varchar(100) primary key,user_name varchar(100) ,pass1 varchar(50), pass2 varchar(50), phno varchar(15),dob varchar(50),gender varchar(50),age varchar(4))"
    cursor.execute(s1)
    print("Airlines user table created")

def good_to_go():
    print("You are all set... go to ACCOUNT CREATION")

Create_Database_Airlines()
connection()
user_accounts_table()
good_to_go()


