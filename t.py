from tkinter import *
from tkinter import scrolledtext  
from tkinter.messagebox import askokcancel
window = Tk()
window.title("Библиотечный каталог")
window.geometry('370x185')
f=("Times New Roman", 14)

def create(): #надо чтобы сохранялось написанное в строки
    window1 = Tk()
    window1.title("Создать новый каталог")
    window1.geometry('450x185')
    lb1 = Label(window1, text="Автор:", font = f)
    lb1.grid(column=0, row=0)
    txt1 = Entry(window1, width=35, font = f)
    txt1.grid(column=1, row=0)
    lb2 = Label ( window1, text = "Название: ", font = f )
    lb2.grid(column=0, row=1)
    txt2 = Entry(window1, width=35, font = f)
    txt2.grid(column=1, row=1)
    lb3 = Label ( window1, text = "Содержание: ", font = f )
    lb3.grid(column=0, row=2)
    txt3 = Entry(window1, width=35, font = f)
    txt3.grid(column=1, row=2)
    def ochist():
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
    def further():
        index=1
        res=txt1.get()+txt2.get()+txt3.get()
        with open (f'{index}.txt', 'w') as b: #начинает с 1, надо как-то с кнопкой связать, чтобы когда нажимаешь index был +1
            q=b.write(res)
            index=index+1
    btn1 = Button(window1, text="Далее",  font=f, command=further, state=NORMAL)
    btn1.grid(column=0, row=6)
    def sozdat():
        okno = Tk()
        okno.title("Новый каталог")
        okno.geometry('400x250')
        txt = scrolledtext.ScrolledText(okno, width=40, height=10, font=f)
        txt.grid(column=0, row=0)
        index=1
        with open (f'{index}.txt', 'r') as b:
            for line in b:
                q=line.strip()
                #в окно не выводит строками, а в idle выводит, значит ошибка в работе с окном
                txt.insert(INSERT, q)
            index=index+1
    btn2 = Button(window1, text="Создать каталог",  font=f, command=sozdat)
    btn2.grid(column=1, row=6)
    btn3 = Button(window1, text="Очистить",  font=f, command=ochist)
    btn3.grid(column=1, row=5)

def openk():
    window2 = Tk()
    window2.title("Открыть каталог")
    window2.geometry('700x500')
    def redakt(): #надо чтобы отредактирвоанный текст сохранялся в файл + избавиться от {}
        okno2 = Tk()
        okno2.title("Редактировать каталог")
        okno2.geometry('450x300')
        txt = scrolledtext.ScrolledText(okno2, width=40, height=10, font=f)
        txt.grid(column=0, row=0)
        with open ("baza.txt", 'r') as b:
            q=b.readlines()
        txt.insert(INSERT, q)
        def ok():
            #
            okno2.destroy()
        btn = Button(okno2, text="ок",  font=f, command=ok)
        btn.grid(column=0, row=2)
        
    btn1 = Button(window2, text="Редактировать каталог",  font=f, command=redakt)
    btn1.grid(column=0, row=100)
    def popoln():
        okno1 = Tk()
        okno1.title("Пополнить каталог")
        okno1.geometry('450x185')
        lb1 = Label(okno1, text="Автор:", font = f)
        lb1.grid(column=0, row=0)
        txt1 = Entry(okno1, width=35, font = f)
        txt1.grid(column=1, row=0)
        lb2 = Label (okno1, text = "Название: ", font = f )
        lb2.grid(column=0, row=1)
        txt2 = Entry(okno1, width=35, font = f)
        txt2.grid(column=1, row=1)
        lb3 = Label (okno1, text = "Содержание: ", font = f )
        lb3.grid(column=0, row=2)
        txt3 = Entry(okno1, width=35, font = f)
        txt3.grid(column=1, row=2)
        def ok(): #
            res=txt1.get()+txt2.get()+txt3.get()
            with open ("baza.txt", 'a') as b:
                q=b.write(res)
            okno1.destroy()
            lbl = Label(okno1, text=q, font = f)
            lbl.grid(column=0, row=0)
        btn = Button(okno1, text="ок",  font=f, command=ok)
        btn.grid(column=0, row=4)
    btn2 = Button(window2, text="Пополнить каталог",  font=f, command=popoln)
    btn2.grid(column=1, row=100)
    with open('baza.txt', 'r') as b:
        kol=1
        for line in b:
            q=line.strip()
            kol=kol+1
            lb = Label(window2, text=q, font = f)
            lb.grid(column=0, row=kol)

    
def receive_inside():
    window3 = Tk()
    window3.title("Получить содержание книги")
    window3.geometry('450x185')
    lb1 = Label(window3, text="Автор:", font = f)
    lb1.grid(column=0, row=0)
    txt1 = Entry(window3, width=35, font = f)
    txt1.grid(column=1, row=0)
    lb2 = Label ( window3, text = "Название: ", font = f )
    lb2.grid(column=0, row=1)
    txt1 = Entry(window3, width=35, font = f)
    txt1.grid(column=1, row=1)
    lb3 = Label ( window3, text = "Содержание: ", font = f )
    lb3.grid(column=0, row=4)
    def soderj():
        with open('1.txt', 'r') as b: 
            q=b.readlines()
            for line in b:
                a=line.strip()
                b=txt1.get()
                if a==b:
                    txt3 = Entry(window3, width=35, font = f)
                    txt3.grid(column=1, row=4)
                    txt3.insert(INSERT, "")
                    break
    btn1 = Button(window3, text="ок",  font=f, command=soderj)
    btn1.grid(column=0, row=3)
    
    
def receive_book():
    window4 = Tk()
    window4.title("Получить книгу по содержанию")
    window4.geometry('500x185')
    lb1 = Label(window4, text="Введите содержание:", font = f)
    lb1.grid(column=0, row=0)
    txt1 = Entry(window4, width=35, font = f)
    txt1.grid(column=1, row=0)
    lb2 = Label ( window4, text = "Название: ", font = f )
    lb2.grid(column=0, row=3)
    btn = Button(window4, text="ок",  font=f)
    btn.grid(column=0, row=2)
    
def receive_list():
    window5 = Tk()
    window5.title("Получить список книг с заданным текстом")
    window5.geometry('450x185')
    lb1 = Label(window5, text="Введите текст:", font = f)
    lb1.grid(column=0, row=0)
    txt1 = Entry(window5, width=35, font = f)
    txt1.grid(column=1, row=0)
    lb2 = Label ( window5, text = "Список книг: ", font = f )
    lb2.grid(column=0, row=3)
    btn = Button(window5, text="ок",  font=f)
    btn.grid(column=0, row=2)

btn1 = Button(window, text="Создать каталог",  font=f, command=create)
btn1.grid(column=0, row=0)
btn2 = Button(window, text="Открыть каталог",  font=f, command=openk)
btn2.grid(column=0, row=1)
btn3 = Button(window, text="Получить содержание книги ",  font=f, command=receive_inside)
btn3.grid(column=0, row=2)
btn4 = Button(window, text="Получить книгу по содержанию ",  font=f, command=receive_book)
btn4.grid(column=0, row=3)
btn5 = Button(window, text="Получить список книг с заданным текстом ",  font=f, command=receive_list)
btn5.grid(column=0, row=4)

window.mainloop()


