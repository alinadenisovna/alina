from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import askokcancel

window = Tk()
window.title("Библиотечный каталог")
window.geometry('370x185')
f=("Times New Roman", 14)

def create():
    filename = filedialog.asksaveasfilename(filetypes=[("Текстовый документ", "*.txt")])
    if filename:
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
        def further():
            if (txt1.get()=='' or txt2.get()=='' or txt3.get()==''):
                showinfo("Ошибка", "Заполните все поля")  
            else:
                lines=["Автор: "+txt1.get(),"Название: "+txt2.get(),"Содержание: "+txt3.get()+'\n']
                with open (filename, 'a') as b:
                    for line in lines:
                        q=b.write(line+'\n')
        def sozdat():
            okno = Tk()
            okno.title("Новый каталог")
            okno.geometry('490x422')
            txt = scrolledtext.ScrolledText(okno, width=52, height=20, font=f)
            txt.grid(column=0, row=0)
            with open(filename, 'r') as b:
                for line in b:
                    q=line.strip()
                    txt.insert(INSERT, q+'\n')
        def ochist():
            txt1.delete(0, END)
            txt2.delete(0, END)
            txt3.delete(0, END)
        btn1 = Button(window1, text="Далее",  font=f, command=further)
        btn1.grid(column=0, row=6)
        btn2 = Button(window1, text="Создать каталог",  font=f, command=sozdat)
        btn2.grid(column=1, row=6)
        btn3 = Button(window1, text="Очистить",  font=f, command=ochist)
        btn3.grid(column=1, row=5)
    else:
        askokcancel("Ошибка", "Вы не выбрали файл")

def openk():
    filename = filedialog.askopenfilename(filetypes=[('Текстовый документ',"*.txt")])
    if filename:
        window2 = Tk()
        window2.title("Открыть каталог")
        window2.geometry('500x500')
        txt = scrolledtext.ScrolledText(window2, width=52, height=20, font=f, state=NORMAL)
        txt.grid(column=0, row=0)
        with open(filename, 'r') as b:
            for line in b:
                q=line.strip()
                txt.insert(INSERT, q+'\n')
        def redakt():
            txt.delete(1.0, END)
            okno2 = Tk()
            okno2.title("Редактировать каталог")
            okno2.geometry('500x500')
            txt1 = scrolledtext.ScrolledText(okno2, width=52, height=20, font=f)
            txt1.grid(column=0, row=0)
            with open (filename, 'r') as b: 
                for line in b:
                    q=line.strip()
                    txt1.insert(INSERT, q+'\n')
            def ok():
                res=txt1.get('1.0', 'end-1c' )
                txt.insert(INSERT, res)
                with open (filename, 'w') as b:
                    q=b.write(res)
                okno2.destroy()
            btn = Button(okno2, text="ок",  font=f, command=ok)
            btn.grid(column=0, row=2)
        btn1 = Button(window2, text="Редактировать каталог",  font=f, command=redakt)
        btn1.grid(column=0, row=100)
        def popoln():
            txt.delete(1.0, END)
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
            def ok():
                if (txt1.get()=='' or txt2.get()=='' or txt3.get()==''):
                    showinfo("Ошибка", "Заполните все поля")
                else:
                    res=['\n'+"Автор: "+txt1.get(),"Название: "+txt2.get(),"Содержание: "+txt3.get()]
                    with open (filename, 'a') as b:
                        for line in res:
                            q=b.write(line+'\n')
                    with open(filename, 'r') as b:
                        for line in b:
                            q=line.strip()
                            txt.insert(INSERT, q+'\n')
                    okno1.destroy()
            btn = Button(okno1, text="ок",  font=f, command=ok)
            btn.grid(column=0, row=4)
        btn2 = Button(window2, text="Пополнить каталог",  font=f, command=popoln)
        btn2.grid(column=0, row=3)
    else:
        askokcancel("Ошибка", "Вы не выбрали файл")

def receive_inside():
    filename = filedialog.askopenfilename(filetypes=[('Текстовый документ',"*.txt")])
    if filename:
        window3 = Tk()
        window3.title("Получить содержание книги")
        window3.geometry('500x250')
        lb1 = Label(window3, text="Автор:", font = f)
        lb1.grid(column=0, row=0)
        txt1 = Entry(window3, width=35, font = f)
        txt1.grid(column=1, row=0)
        lb2 = Label ( window3, text = "Название: ", font = f )
        lb2.grid(column=0, row=1)
        txt2 = Entry(window3, width=35, font = f)
        txt2.grid(column=1, row=1)
        lb3 = Label ( window3, text = "Содержание: ", font = f )
        lb3.grid(column=0, row=4)
        txt3 = scrolledtext.ScrolledText(window3, width=40, height=5, font=f)
        txt3.grid(column=1, row=4)
        def soderj():
            if (txt1.get()=='' or txt2.get()==''):
                showinfo("Ошибка", "Заполните все поля")
            else:
                a="Автор: "+txt1.get()
                n="Название: "+txt2.get()
                with open(filename, 'r') as b:
                    lines=b.readlines()
                    for line_idx, line in enumerate (lines):
                        if line.find(a)!=-1 and lines[line_idx+1].find(n)!=-1:
                            txt3.insert(INSERT, lines[line_idx+2][12:])
        def ochist():
            txt1.delete(0, END)
            txt2.delete(0, END)
            txt3.delete(1.0, END)
        btn1 = Button(window3, text="ок",  font=f, command=soderj)
        btn1.grid(column=0, row=3)
        btn2 = Button(window3, text="очистить",  font=f, command=ochist)
        btn2.grid(column=1, row=3)
    else:
        askokcancel("Ошибка", "Вы не выбрали файл")

def receive_book():
    filename = filedialog.askopenfilename(filetypes=[('Текстовый документ',"*.txt")])
    if filename:
        window4 = Tk()
        window4.title("Получить книгу по содержанию")
        window4.geometry('650x185')
        lb1 = Label(window4, text="Введите содержание:", font = f)
        lb1.grid(column=0, row=0)
        txt1 = Entry(window4, width=50, font = f)
        txt1.grid(column=1, row=0)
        lb2 = Label ( window4, text = "Название: ", font = f )
        lb2.grid(column=0, row=3)
        txt2 = Entry(window4, width=50, font = f)
        txt2.grid(column=1, row=3)
        def ok():
            if txt1.get()=='':
                showinfo("Ошибка", "Заполните все поля")
            else:
                a=txt1.get()
                with open(filename, 'r') as b:
                    lines=b.readlines()
                    for line_idx, line in enumerate (lines):
                        if line.find(a)!=-1:
                            txt2.insert(INSERT, lines[line_idx-2][7:]+" "+'"'+lines[line_idx-1][10:]+'"')
        def ochist():
            txt1.delete(0, END)
            txt2.delete(0, END)
        btn2 = Button(window4, text="очистить",  font=f, command=ochist)
        btn2.grid(column=1, row=2)
        btn = Button(window4, text="ок",  font=f, command=ok)
        btn.grid(column=0, row=2)
    else:
        askokcancel("Ошибка", "Вы не выбрали файл")

def receive_list():
    filename = filedialog.askopenfilename(filetypes=[('Текстовый документ',"*.txt")])
    if filename:
        window5 = Tk()
        window5.title("Получить список книг с заданным текстом")
        window5.geometry('500x250')
        lb1 = Label(window5, text="Введите текст:", font = f)
        lb1.grid(column=0, row=0)
        txt1 = Entry(window5, width=35, font = f)
        txt1.grid(column=1, row=0)
        lb2 = Label ( window5, text = "Список книг: ", font = f )
        lb2.grid(column=0, row=3)
        txt = scrolledtext.ScrolledText(window5, width=40, height=5, font=f)
        txt.grid(column=1, row=3)
        def ok():
            if txt1.get()=='':
                showinfo("Ошибка", "Заполните все поля")
            else:
                a=txt1.get()
                with open(filename, 'r') as b:
                    lines=b.readlines()
                    for line_idx, line in enumerate (lines):
                        if line.find(a)!=-1:
                            txt.insert(INSERT, lines[line_idx-2][7:]+lines[line_idx-1][10:]+'\n')
        def ochist():
            txt1.delete(0, END)
            txt.delete(1.0, END)
        btn2 = Button(window5, text="очистить",  font=f, command=ochist)
        btn2.grid(column=1, row=2)
        btn = Button(window5, text="ок",  font=f, command=ok)
        btn.grid(column=0, row=2)
    else:
        askokcancel("Ошибка", "Вы не выбрали файл")
    
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
