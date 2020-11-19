import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='sarthak', passwd='sarthak',database='home')

mycursor = mydb.cursor()

mycursor.execute("select * from student where name = 'sarthak';")

result = mycursor.fetchall()

for i in result:
    print(i)