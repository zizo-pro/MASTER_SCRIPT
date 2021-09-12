from sqlite3 import connect

db = connect("login.db")

cr = db.cursor()

username = input("please enter username : ")
password = input("please enter password : ")

cr.execute("select * from login")
data = cr.fetchone()
usr = data[0]
passw = data[1]

if username == usr and password == passw :
    print("logged in succesfully")

else:
    print("wrong credentials")