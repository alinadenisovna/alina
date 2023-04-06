from tkinter import *
from simpletk import *
from tkinter.messagebox import askokcancel
app = TApplication("Библиотечный каталог")
app.position = (200, 200)
app.size = (450, 150)
app.resizable = (True, True)
app.minsize = (100, 100)
app.maxsize = (900, 700)
f=("Comic Sans MS", 14)

a=TEdit(app, font=f, width=10)
a.position=(0,200)
a.text="sdfgs"


def newk(sender):
    window1 = TApplication("Создать новый каталог")
    window1.position = (200, 200)
    window1.size = (600, 300)
    window1.resizable = (True, True)
    window1.minsize = (100, 100)
    window1.maxsize = (900, 700)
    lbh = TLabel ( window1, text = "Автор: ", font = f )
    lbh.position = (10, 0)
    lba = TLabel ( window1, text = "Название: ", font = f )
    lba.position = (10, 30)
    lbn = TLabel ( window1, text = "Содержание: ", font = f )
    lbn.position = (10, 60)
    a=TEdit(window1, font=f, width=35)
    a.position=(150,0)
    a.text="sdfgs"
    lbaa = TEdit ( window1, font = f, width = 35 )
    lbaa.position = (150, 30)
    lbaa.text = "арвкеркы"
    lbnn = TEdit ( window1, font = f, width = 35 )
    lbnn.position = (150, 60)
    lbnn.text = "ркуеыри укып"
    akn1 = TButton ( window1, text = "Далее ", width = 10)
    akn1.position = (10, 150)
    akn1["state"]="normal"
    akn2 = TButton ( window1, text = "Создать каталог ", width = 20 )
    akn2.position = (100, 150)
    akn2["state"]="normal"
    window1.Run()

def redk (sender):
    window3 = TApplication("Редактировать каталог")
    window3.position = (200, 200)
    window3.size = (600, 300)
    window3.resizable = (True, True)
    window3.minsize = (100, 100)
    window3.maxsize = (900, 700)
    rlbr = TLabel ( window3, text = "Номер книги:", font = f )
    rlbr.position = (10, 0)
    rad=TComboBox(window3, height=4,width=4,font = f)
    r=[1,2,3,4,5]
    for i in r:
        rad.addItem(i)
        rad.position=(150, 0)
    rlbh = TLabel ( window3, text = "Автор: ", font = f )
    rlbh.position = (10, 30)
    rlba = TLabel ( window3, text = "Название: ", font = f )
    rlba.position = (10, 60)
    rlbn = TLabel ( window3, text = "Содержание: ", font = f )
    rlbn.position = (10, 90)
    pkn = TButton ( window3, text = "ок", width = 10)
    pkn.position = (10, 200)

def poplk (sender):
    window4 = TApplication("Редактировать каталог")
    window4.position = (200, 200)
    window4.size = (600, 300)
    window4.resizable = (True, True)
    window4.minsize = (100, 100)
    window4.maxsize = (900, 700)
    plbh = TLabel ( window4, text = "Автор: ", font = f )
    plbh.position = (10, 0)
    plba = TLabel ( window4, text = "Название: ", font = f )
    plba.position = (10, 30)
    plbn = TLabel ( window4, text = "Содержание: ", font = f )
    plbn.position = (10, 60)
    plbhh = TEdit ( window4, font = f, width = 35 )
    plbhh.position = (150, 0)
    plbhh.text = ""
    plbaa = TEdit ( window4, font = f, width = 35 )
    plbaa.position = (150, 30)
    plbaa.text = ""
    plbnn = TEdit ( window4, font = f, width = 35 )
    plbnn.position = (150, 60)
    plbnn.text = ""
    pkn = TButton ( window4, text = "ок", width = 10)
    pkn.position = (10, 200)
    
def openk(sender):
    window2 = TApplication("Открыть каталог")
    window2.position = (200, 200)
    window2.size = (600, 300)
    window2.resizable = (True, True)
    window2.minsize = (100, 100)
    window2.maxsize = (900, 700)
    okn1 = TButton ( window2, text = "Редактировать каталог", width = 20)
    okn1.position = (10, 250)
    okn1["state"]="normal"
    okn1.onClick=redk
    okn2 = TButton ( window2, text = "Пополнить каталог", width = 20 )
    okn2.position = (200, 250)
    okn2["state"]="normal"
    okn2.onClick=poplk
    prop = TEdit ( window2, font = f, width = 10 )
    prop.position = (10, 10)
    prop.text = ""
    with open('baza.txt', 'r', encoding="utf-8") as b:
        q=b.readlines()
        prop.text=q   

def sodkn (sender):
    window5 = TApplication("Редактировать каталог")
    window5.position = (200, 200)
    window5.size = (600, 300)
    window5.resizable = (True, True)
    window5.minsize = (100, 100)
    window5.maxsize = (900, 700)
    rlbr = TLabel ( window5, text = "Автор: ", font = f )
    rlbr.position = (10, 0)
    rad=TComboBox(window5, height=4,width=4,font = f)
    r=[1,2,3,4,5]
    for i in r:
        rad.addItem(i)
        rad.position=(150, 0)
    rlbr = TLabel ( window5, text = "Название: ", font = f )
    rlbr.position = (10, 30)
    rad=TComboBox(window5, height=4,width=4,font = f)
    r=[1,2,3,4,5]
    for i in r:
        rad.addItem(i)
        rad.position=(150, 30)
    plbn = TLabel ( window5, text = "Содержание: ", font = f )
    plbn.position = (10, 120)
    plbnn = TEdit ( window5, font = f, width = 35 )
    plbnn.position = (150,120)
    plbnn.text = ""
    pkn = TButton ( window5, text = "ок", width = 10)
    pkn.position = (10, 80)


def nazkn (sender):
    window6 = TApplication("Редактировать каталог")
    window6.position = (200, 200)
    window6.size = (600, 300)
    window6.resizable = (True, True)
    window6.minsize = (100, 100)
    window6.maxsize = (900, 700)
    plbn = TLabel ( window6, text = "Содержание: ", font = f )
    plbn.position = (10, 0)
    plbnn = TEdit ( window6, font = f, width = 35 )
    plbnn.position = (150,0)
    plbnn.text = ""
    plbh = TLabel ( window6, text = "Название: ", font = f )
    plbh.position = (10, 80)
    plbhh = TEdit ( window6, font = f, width = 35 )
    plbhh.position = (150, 80)
    plbhh.text = ""
    pkn = TButton ( window6, text = "ок", width = 10)
    pkn.position = (10, 40)
    
def slkn (sender):
    window7 = TApplication("Редактировать каталог")
    window7.position = (200, 200)
    window7.size = (600, 300)
    window7.resizable = (True, True)
    window7.minsize = (100, 100)
    window7.maxsize = (900, 700)
    plbn = TLabel ( window7, text = "Введите текст: ", font = f )
    plbn.position = (10, 0)
    plbnn = TEdit ( window7, font = f, width = 35 )
    plbnn.position = (150,0)
    plbnn.text = ""
    plbh = TLabel ( window7, text = "Список книг: ", font = f )
    plbh.position = (10, 80)
    plbhh = TEdit ( window7, font = f, width = 35 )
    plbhh.position = (150, 80)
    plbhh.text = ""
    pkn = TButton ( window7, text = "ок", width = 10)
    pkn.position = (10, 40)



kn1 = TButton ( app, text = "Создать каталог ", width = 60)
kn1.position = (10, 0)
kn1["state"]="normal"
kn2 = TButton ( app, text = "Открыть каталог ", width = 60 )
kn2.position = (10, 30)
kn2["state"]="normal"
kn3 = TButton ( app, text = "Получить содержание книги ", width = 60 )
kn3.position = (10, 60)
kn3["state"]="normal"
kn4 = TButton ( app, text = "Получить книгу по содержанию ", width = 60 )
kn4.position = (10, 90)
kn4["state"]="normal"
kn5 = TButton ( app, text = "Получить список книг с заданным текстом ", width = 60 )
kn5.position = (10, 120)
kn5["state"]="normal"


kn1.onClick=newk  #название функции
kn2.onClick=openk
kn3.onClick=sodkn
kn4.onClick=nazkn
kn5.onClick=slkn


app.Run()

