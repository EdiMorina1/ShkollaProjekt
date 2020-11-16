
import sqlite3
from tkinter import *
from drejtori import drejtori

class login:

    def __init__(self):

        self.conn=sqlite3.connect("shkolla")
        self.c = self.conn.cursor()



        signin = Tk()
        signin.geometry('300x400')
        signin.minsize(width=300, height=400)
        signin.maxsize(width=300, height=400)
        loginFoto = PhotoImage(file="C:/Users/nehat/Desktop/logologin.gif")
        Label(signin, image=loginFoto).pack()
        Label(signin, text="Username:").pack( pady=(20,0))
        self.user = Entry(signin)
        self.user.pack( pady=(0,20))
        Label(signin, text="Password:").pack()
        self.pas = Entry(signin, show = "*")
        self.pas.pack()
        self.hyr = Button(signin, text= "SignIn", bg = '#0000ff', fg='#fff', font = ('bold',15), command= self.merr).place(width=100 ,x = 100, y = 300)





        signin.mainloop()

    def merr (self):
        pas  = self.pas.get()
        user = self.user.get()
        print(user, pas)
        sql = "SELECT numriPersonal, password FROM drejtori WHERE numriPersonal =" + user
        print(sql)
        self.c.execute(sql)
        result = self.c.fetchall()
        if(len(result)>0):
            if(pas == result[0][1]):
                drejt = drejtori()
            else:
                print("Passwordi eshte GABIM!!!")

        else:
            print("Ky USER nuk eksiston!!!")






login1 = login()