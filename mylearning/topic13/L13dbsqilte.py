import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
##if you not have database use this to create---->>>>  c.execute('''CREATE TABLE users ( id int auto_increment primary key,name varchar,password varchar)''')
def add_user(username,userpass):
    c.execute ("INSERT INTO users (name, password) VALUES ('%s','%s')"%(username,userpass))
    conn.commit()
name = input("Enter login: ")
passd = input("Enter password: ")
print()
print("Users' list:\n")
add_user(name,passd)
c.execute('SELECT * FROM users')
row = c.fetchone()
while row is not None:
    print("id: " + str(row[0]) + " Login: " + row[1] + " | Password: " + row[2])
    row = c.fetchone()
c.close()
conn.close()
