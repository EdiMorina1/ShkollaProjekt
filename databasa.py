
import sqlite3

conn = sqlite3.connect('Shkolla.db')
c = conn.cursor()

# sql = """CREATE TABLE lenda (
#   idLenda integer primary key autoincrement,
#   emriLenda text not null
# )"""




# sql = """CREATE TABLE perioda (
#   idPerioda integer primary key autoincrement,
#   emriPerioda text not null
# )"""



# sql = """CREATE TABLE profesori(
#    idProfi integer primary key autoincrement,
#    emriProfi text not null,
#    mbiemriProfi text not null,
#    idLenda text not null,
#    numriPersonal text not null,
#    email text,
#    password text not null,

#    FOREIGN KEY(idLenda) REFERENCES Lenda(idLenda)

# )"""


# sql = """CREATE TABLE klasa(
#  idKlasa integer primary key autoincrement,
#  emriKlasa text not null,
#  paralelja text,
#  vitishkollor text not null,
#  kujdestari integer not null,

#  FOREIGN KEY(kujdestari) REFERENCES profesori(idProfi)



#  )"""


# sql = """CREATE TABLE nxenesi(
#   idNxenesi integer primary key autoincrement,
#   emriNxenesi text not null,
#   mbiemriNxenesi text not null,
#   emriPrindit text not null,
#   mbiemriPrindit text not null,
#   telefoni text not null,
#   klasa integer not null,

#    FOREIGN KEY(klasa) REFERENCES klasa(idklasa)

# )"""




# sql = """CREATE TABLE notat(
#   idNotat integer primary key autoincrement,
#   idNxenesi integer not null,
#   idProfi integer not null,
#   idPerioda integer not null,
#   notaVlera integer not null,

#     FOREIGN KEY(idNxenesi) REFERENCES nxenesi(idNxenesi),
#     FOREIGN KEY(idProfi) REFERENCES profesori(idProfi),
#     FOREIGN KEY(idPerioda) REFERENCES perioda(idPerioda)
# )"""

# sql = """CREATE TABLE notaPerfundimtare(
#   idNota integer primary key autoincrement,
#   nota integer not null,
#   idProfi integer not null,
#   idNxenesi integer not null,

#   FOREIGN KEY(idNxenesi) REFERENCES nxenesi(idNxenesi),
#   FOREIGN KEY(idProfi) REFERENCES profesori(idProfi)


# )"""




# sql = """CREATE TABLE mungesat(
#  idMungesa integer primary key autoincrement,
#  idNxenesi integer not null,
#  idProfi integer not null,
#  ora text not null,
#  arsyshmeria text not null,

#  FOREIGN KEY(idNxenesi) REFERENCES nxenesi(idNxenesi),
#  FOREIGN KEY(idProfi) REFERENCES profesori(idProfi)



# )"""


# sql = """CREATE TABLE drejtori(
#   idDrejtori integer primary key autoincrement,
#   emriDrejtori text not null,
#   mbiemriDrejtori text not null,
#   numriPersonal text not null,
#   email text,
#   password text not null

# )"""

c.execute(sql)