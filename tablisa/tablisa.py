from tkinter import *
from tkinter.messagebox import *
aken=Tk()

def rus():
	showinfo(title="Литература",message="Основной урок\n Учитель - Ljudmila Mikhailova\n Кабинет - B 221")
def log():
	showinfo(title="Логистика",message="Основной урок\n Учитель - Inessa Klemanskaja\n Кабинет - B 002")
def mat():
	showinfo(title="Математика",message="Основной урок\n Учитель - Nadewda Voronova\n Кабинет - B 133")
def matem():
	showinfo(title="Доп.Математика",message="Доп.урок\n Учитель - Nadewda Voronova\n Кабинет - B 133")
def angl():
	showinfo(title="Английский",message="Основной урок\n Учитель - Olga Borodina\n Кабинет - B 227")
def est():
	showinfo(title="Эстонский",message="Основной урок\n Учитель - Olesja Ojamäe\n Кабинет - B 234")
def kemi():
	showinfo(title="Доп.Химия",message="Доп.урок\n Учитель - Svetlana Pesestkaja\n Кабинет - B 144")
def ests():
	showinfo(title="Доп.Эстонский",message="Доп.урок\n Учитель - Olesja Ojamäe\n Кабинет - B 234")
def prog():
	showinfo(title="Програмирование",message="Основной урок\n Учитель - Marina Oleinik\n Кабинет - E 07")
def kunst():
	showinfo(title="Исскуство",message="Основной урок\n Учитель - Aleksandrova\n Кабинет - B 232")
def fizra():
	showinfo(title="Физкультура",message="Основной урок\n Учитель - Maksim\n Кабинет - Zal A")
def füs():
	showinfo(title="Физика",message="Основной урок\n Учитель - Nadewda Voronova\n Кабинет - B 133")
def raken():
	showinfo(title="Ракендусттарквара",message="Основной урок\n Учитель - Merkulova\n Кабинет - E 10")
def angld():
	showinfo(title="Доп.Английский",message="Доп.урок\n Учитель - Olga Borodina\n Кабинет - B 227")
def okno():
	showinfo(title="Oкно",message="Свободное время")





Label(text="",font="Arial 15",height=5,width=12,relief="groove").grid(row=1,column=1)
Label(text="Teisipäev",font="Arial 15",height=5,width=12,relief="groove").grid(row=2,column=0)
Label(text="",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=0)
Label(text="Esmaspäev",font="Arial 15",height=5,width=12,relief="groove").grid(row=1,column=0)
Label(text="Kolmapäev",font="Arial 15",height=5,width=12,relief="groove").grid(row=3,column=0)
Label(text="Neljapäev",font="Arial 15",height=5,width=12,relief="groove").grid(row=4,column=0)
Label(text="Reede",font="Arial 15",height=5,width=12,relief="groove").grid(row=5,column=0)
Label(text="0",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=1)
Label(text="1",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=2)
Label(text="2",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=3)
Label(text="3",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=4)
Label(text="4",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=5)
Label(text="5",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=6)
Label(text="6",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=7)
Label(text="7",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=8)
Label(text="8",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=9)
Label(text="9",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=10)
Label(text="10",font="Arial 15",height=5,width=12,relief="groove").grid(row=0,column=11)
Button(text="Eesti keel\nteise keelena\ngrupp2",font="Arial=10",bg="GREY",height=5,width=15,relief="groove",command=est).grid(row=1,column=2)
Button(text="Logistikateenused\nja varude\njuhtimine",bg="GREEN",font="Arial=10",height=5,width=15,relief="groove",command=log).grid(row=1,column=3)
Button(text="Matemaatika",font="Arial=10",bg="PINK",height=5,width=15,relief="groove",command=matem).grid(row=1,column=4)
Button(text="Matemaatika",font="Arial=10",bg="PINK",height=5,width=15,relief="groove",command=matem).grid(row=1,column=5)
Button(text="Окно",font="Arial=10",height=5,width=15,relief="groove",command=okno).grid(row=1,column=6)
Button(text="Keel ja kirjandus",font="Arial=10",bg="LIGHTGREEN",height=5,width=15,relief="groove",command=rus).grid(row=1,column=7)
Button(text="Keel ja kirjandus",font="Arial=10",bg="LIGHTGREEN",height=5,width=15,relief="groove",command=rus).grid(row=1,column=8)
Button(text="Tugiõpe\n(matemaatika)",bg="PINK",font="Arial=10",height=5,width=15,relief="groove",command=matem).grid(row=1,column=9)
Button(text="Tugiõpe\n(Keemia)",font="Arial=10",bg="PURPLE",height=5,width=15,relief="groove",command=kemi).grid(row=2,column=2)
Label(text="",font="Arial=10",height=7,width=15,relief="groove").grid(row=2,column=1)
Button(text="Programeerimise alused",font="Arial=10",bg="LIGHTBLUE",height=5,width=45,relief="groove",command=prog).grid(row=2,column=3,columnspan=3)
Button(text="Окно",font="Arial=10",height=5,width=15,relief="groove",command=okno).grid(row=2,column=6)
Button(text="Füüsika",font="Arial=10",bg="PINK",height=5,width=30,relief="groove",command=füs).grid(row=2,column=5,columnspan=6)
Button(text="Eesti keel\nteise keelena\ngrupp1",bg="#CBC3E3",font="Arial=10",height=5,width=15,relief="groove",command=est).grid(row=3,column=2)
Label(text="",font="Arial=10",height=7,width=15,relief="groove").grid(row=3,column=1)
Button(text="Kunstiained",font="Arial=10",bg="PURPLE",height=5,width=30,relief="groove",command=kunst).grid(row=3,column=3,columnspan=2)
Button(text="Окно",font="Arial=10",height=5,width=15,relief="groove",command=okno).grid(row=3,column=5)
Button(text="Kehaline kasvatus",font="Arial=10",bg="#CBC3E3",height=5,width=30,relief="groove",command=fizra).grid(row=3,column=5,columnspan=4)
Label(text="",font="Arial=10",height=7,width=15,relief="groove").grid(row=4,column=1)
Button(text="Logistikateenused\nja verude\njuhtimine",bg="GREEN",font="Arial=10",height=5,width=30,relief="groove",command=log).grid(row=4,column=2,columnspan=2)
Button(text="Окно",font="Arial=10",height=5,width=15,relief="groove",command=okno).grid(row=4,column=4)
Button(text="Programeerimise alused",font="Arial=10",bg="LIGHTBLUE",height=5,width=30,relief="groove",command=prog).grid(row=4,column=4,columnspan=4)
Button(text="Inglise keel\ngrupp 1",font="Arial=10",bg="#f5f5dc",height=5,width=15,relief="groove",command=angl).grid(row=4,column=7)
Button(text="Inglise keel\ngrupp 1",font="Arial=10",bg="#f5f5dc",height=5,width=15,relief="groove",command=angl).grid(row=4,column=8)
Button(text="Arenduskeskkonna\nloomine",font="Arial=10",bg="Red",height=5,width=30,relief="groove",command=raken).grid(row=4,column=8,columnspan=9)
Button(text="Rühmatajatund",font="Arial=10",bg="Purple",height=5,width=15,relief="groove",command=ests).grid(row=4,column=11)
Label(text="",font="Arial=10",height=7,width=15,relief="groove").grid(row=5,column=1)
Button(text="Eesti keel\ngrupp 1",font="Arial=10",bg="Purple",height=5,width=15,relief="groove",command=est).grid(row=5,column=2)
Button(text="Eesti keel\ngrupp 1",font="Arial=10",bg="Purple",height=5,width=15,relief="groove",command=est).grid(row=5,column=3)
Button(text="Programeerimise alused",font="Arial=10",bg="LIGHTBLUE",height=5,width=80,relief="groove",command=prog).grid(row=5,column=3,columnspan=7)
Button(text="Arenduskeskkonna\nloomine",font="Arial=10",bg="RED",height=5,width=30,relief="groove",command=raken).grid(row=5,column=8,columnspan=9)





aken.title("")
aken.geometry("2000x2000")










aken.mainloop()