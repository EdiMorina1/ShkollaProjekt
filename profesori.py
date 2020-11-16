import sqlite3
from tkinter import*

class profesori:
	def __init__(self):
		self.conn=sqlite3.connect("shkolla.db")
		self.c = self.conn.cursor()
		self.root = Tk()
		self.root.attributes("-fullscreen", True)
		self.mungesa = LabelFrame(self.root,text = "Regjistro Mungesat", bg="#FFF").place(x=80,y=15,width=300, height = 700)
		self.nota = LabelFrame(self.root,text = "Noto Nxenesin", bg="#FFF").place(x=500,y=15,width=300, height = 700)
		self.perfundoNoten = LabelFrame(self.root,text = "Perfundo noten Nxenesin", bg="#FFF").place(x=915,y=15,width=300, height = 700)
		self.mungesaBTN = Button(self.mungesa, text = "Sheno Nxenesin",command = self.shenoNxenesin).place(x=150, y=670)
		self.notaBTN = Button(self.nota, text = "Sheno Nxenesin",command = self.shenoNoten).place(x=580, y=670)
		self.PerfundonotatBTN = Button(self.perfundoNoten, text = "Sheno Nxenesin",command = self.perfundoNoten).place(x=1000, y=670)
		
        # krijimi i tabelave dhe entryve te mungesat

		labelat = ["ID e profesorit", "ID e nxenesit","Ora mesimore","Aryshmeria"]
		self.entrytLista = []
		x=90
		y=90
		for i in range (len(labelat)):
			Label(self.mungesa, text = labelat[i]).place(x=x, y=y)
			ent = Entry(self.mungesa)
			ent.place(x=x, y=y+30)
			self.entrytLista.append(ent)
			y = y+60


        
        # krijimi i tabelave dhe entryve te notat

		labelat1 = ["ID e profesorit", "Id e nxenesit","Perioda","Nota"]
		self.entrytListaNota = []
		x=520
		y=90
		for i in range (len(labelat1)):
			Label(self.nota, text = labelat[i]).place(x=x, y=y)
			ent = Entry(self.nota)
			ent.place(x=x, y=y+30)
			self.entrytListaNota.append(ent)
			y = y+60




		labelat2 = ["ID e profesorit", "Id e nxenesit","peroidat","nota"]
		self.entrytListaNotaPerfundimtare = []
		x=930
		y=90
		for i in range (len(labelat2)):
			Label(self.perfundoNoten, text = labelat[i]).place(x=x, y=y)
			ent = Entry(self.perfundoNoten)
			ent.place(x=x, y=y+30)
			self.entrytListaNotaPerfundimtare.append(ent)
			y = y+60








		self.root.mainloop()

	def shenoNxenesin(self):
		tedhenat=[]
		for i in range(len(self.entrytLista)):
			tedhenat.append(self.entrytLista[i].get())


			self.execute("""INSERT INTO mungesat (idProfi, idNxenesi, ora, arsyeshmeria)values(?,?,?,?);""",tedhenat)
			self.conn.commit()

	def shenoNoten(self):
		tedhenat=[]
		for i in range(len(self.entrytListaNota)):
			tedhenat.append(self.entrytListaNota[i].get())
			self.execute("""INSERT INTO notat(idNxenesi, idProfi, idPerioda, notaVlera)values(?,?,?,?);""",tedhenat)
			self.conn.commit()

	def perfundoNoten(self):
		tedhenat = []
		for i in range (len(self.entrytListaNotaPerfundimtare)):
			tedhenat.append(self.entrytListaNotaPerfundimtare[i].get())
			nxenesi = tedhenat[1]
			perioda = tedhenat[2]
			self.c.execute("""SELECT notaVlera from notat where idNxenesi = ? and idPerioda=?;""",(nxenesi,perioda)
			self.conn.commit()
    rezult = self.c.fetchall()
	print(rezult)




    	
profi = profesori()