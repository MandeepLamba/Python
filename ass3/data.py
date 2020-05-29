import mysql.connector

name1= 'mandeep'
email=  'mandeeplamba225@gmail.com'
gender= 1
country= 'India'
prog= 1

# try:
myconn = mysql.connector.connect(host = "localhost",user='root',database='python')
file = open("Exyz.txt",'w')
cur = myconn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Student (name TEXT(15),email VARCHAR(20),gender INT(1),country TEXT(10),prog INT(2))')
cur.execute('INSERT INTO Student VALUES(%s,%s,%s,%s,%s)',params=(name1, email, gender, country, prog))
# for i in cur:
#     file.write(str(i)+'\n')
print(cur.rowcount,'rows saved to file.')
# except Exception as e:
#     print(e)
#     myconn.rollback()
myconn.commit()
myconn.close()