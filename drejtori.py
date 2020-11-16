import sqlite3
from tkinter import *

class drejtori:
    def __init__(self):
        self.conn=sqlite3.connect("shkolla.db")
        self.c = self.conn.cursor()
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        self.butoniNx = Button(self.root,text = "Regjistro nxenesin", command = self.regjistroNxenesin)
        self.butoniNx.place(x = 30, y = 30, width = 110, height = 30)
        self.butoniLenda = Button(self.root, text="Regjistro lenden",command = self.regjistroLendaGui)
        self.butoniLenda.place(x = 30, y = 90, width = 110, height = 30)
        self.butoniProf = Button(self.root, text="Regjistro profesori",command=self.regjistroProfesorin)
        self.butoniProf.place(x = 30, y = 150, width = 110, height = 30)
        self.butoniKlasa = Button(self.root, text="Regjistro klasa",command = self.regjistroKlasenGui)
        self.butoniKlasa.place(x = 30, y = 210, width = 110, height = 30)

        self.root.mainloop()

    def regjistroNxenesin (self):
        self.regjistri = Frame(self.root, bg="#FFF")
        self.regjistri.place(x=180, y=30, height=800, width=400)

        self.lblEmri = Label(self.regjistri, text="EMRI:").place(x=30, y=30)
        self.lblMbiemri = Label(self.regjistri, text="MBIEMRI:").place(x=30, y=80)
        self.lblEmriPrindit = Label(self.regjistri, text="EMRI PRINDIT:").place(x=30, y=130)
        self.lblMbiemriPrindit = Label(self.regjistri, text="MBIEMRI PRINDIT:").place(x=30, y=180)
        self.lblNrTel = Label(self.regjistri, text="TEL:").place(x=30, y=230)
        self.lblIDK = Label(self.regjistri, text="KLASA ID:").place(x=30, y=280)

        self.entEmri = Entry(self.regjistri)
        self.entEmri.place(x=30, y=40+15)
        self.entMbiemri = Entry(self.regjistri)
        self.entMbiemri.place(x=30, y=90+15)
        self.entEmriPrindit = Entry(self.regjistri)
        self.entEmriPrindit.place(x=30, y=140+15)
        self.entMbiemriPrindit = Entry(self.regjistri)
        self.entMbiemriPrindit.place(x=30, y=190+15)
        self.entNrTel = Entry(self.regjistri)
        self.entNrTel.place(x=30, y=240+15)
        self.entIDK = Entry(self.regjistri)
        self.entIDK.place(x=30, y=290+15)

        self.btnSave = Button(self.regjistri, text = "Ruaj", command = self.regjisterDataNX)
        self.btnSave.place(x = 30, y = 400)

    def regjisterDataNX(self):
        tedhenat = [self.entEmri.get(), self.entMbiemri.get(), self.entEmriPrindit.get(), self.entMbiemriPrindit.get(),
            self.entNrTel.get(), self.entIDK.get()]
        self.c.execute("""INSERT INTO nxenesi (emriNxenesi, mbiemriNxenesi, emriPrindit, mbiemriPrindit, telefoni, klasa)
        	values (?,?,?,?,?,?);""",tedhenat)
        self.conn.commit()
        self.regjistri.destroy()
    def regjistroLendaGui(self):

        def regjistroLenden():
            tedhenat = [self.entemriLenda.get()]
            self.c.execute("""INSERT INTO lenda(emriLenda)values(?);""",tedhenat)
            self.conn.commit()
            self.regjistri.destroy()

        self.regjistri = Frame(self.root, bg="#FFF")
        self.regjistri.place(x=180, y=30, height=800, width=400)

        Label(self.regjistri, text = "Emri i lendes").place(x=30, y=30)
        self.entemriLenda = Entry(self.regjistri)
        self.entemriLenda.place(x = 30, y = 100)

        btnSave = Button(self.regjistri, text = 'Ruaj', command = regjistroLenden)
        btnSave.place(x=30, y=300)

    def regjistroProfesorin(self):

        def ruajtedhenatProfi():
            tedhenat=[]
            for i in range(len(listaEntry)):
                tedhenat.append(listaEntry[i].get())

            self.c.execute("""INSERT INTO profesori(emriProfi,mbiemriProfi,idLenda,numriPersonal,email,password) values
                (?,?,?,?,?,?);""", tedhenat)
            self.conn.commit()
            self.regjistri.destroy()






        listaLBL=['Emri i Profesorit','Mbiemri i Profesorit','Id e Lendes','Nr personal','email','pass']
        listaEntry = []

        self.regjistri = Frame(self.root, bg="#FFF")
        self.regjistri.place(x=180, y=30, height=800, width=400)

        x=10
        y=10

        for i in range(len(listaLBL)):
            Label(self.regjistri, text=listaLBL[i]).place(x=x, y=y)
            ent = Entry(self.regjistri)
            ent.place(x=x, y=y+30)
            listaEntry.append(ent)
            y=y+50

        btnSave = Button(self.regjistri, text = 'Ruaj', command = ruajtedhenatProfi)
        btnSave.place(x=30, y=330)

    def regjistroKlasenGui(self):

        def regjistroKlasen():
            tedhenat = []
            for i in range(len(listaEntry)):
                tedhenat.append(listaEntry[i].get())
            self.c.execute("""INSERT INTO klasa(emriKlasa,paralelja,vitishkollor,kujdestari) values(?,?,?,?);""", tedhenat)
            self.conn.commit()
            self.regjistri.destroy()


        self.regjistri = Frame(self.root, bg="#FFF")
        self.regjistri.place(x=180, y=30, height=800, width=400)

        listaLbl = ['klasa','paralelja','viti shkollor','kujdestari']
        listaEntry = []

        x=10
        y=10

        for i in range(len(listaLbl)):
            Label(self.regjistri, text = listaLbl[i]).place(x=x , y=y)
            ent = Entry (self.regjistri)
            ent.place(x=x , y=y+30)
            listaEntry.append(ent)
            y += 60
        btnSave = Button(self.regjistri, text = 'Ruaj', command = regjistroKlasen)
        btnSave.place(x=30, y=330)









drejti = drejtori()
