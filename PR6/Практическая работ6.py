 # -*- coding: utf-8 -*-
 """


    Практическая работа 2. номер зачетной книжки 21-702
    Автор: Федоров Артем Андреевич
    Дата:26.01.2022
"""
from cgitb import text
from http import client
from msvcrt import LK_NBLCK
from multiprocessing.connection import Client
from tkinter import *  
from tkinter import ttk 
from tkinter import messagebox 


# задача 2
def chislo():
    x=int(tab1N.get())
    p=1
    if x<=2:
        messagebox.showwarning('название','введите другое число')
    else:
        while p <= x:
            p=p+1
            if x%p!=0:
                messagebox.showinfo('Готово!',x)
            break
    
# Задача 4
def day1():
    x=int(tab2X.get())
    y=int(tab2Y.get())
    day=1
    while (x<=y):
        x=x*1.1
        day=day+1
    
    messagebox.showinfo("задание 4",str(y) + " километров пробежал спортсмен за " + str(day) + " дней.")
# Задача 6
def credznach():
    x = float(tab3X.get())
    cnt = 0
    srzn = 0
    while x != 0:
        srzn += x
        cnt += 1
        x = float(tab3X.get())
        srzn /= cnt
        tab3.update()
        Rezyltat.config(text='срднее значение'+str(srzn))
        



  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x400')  
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control) 
tab_control.pack(expand=1, fill='both')  
tab_control.add(tab1, text='Первая работа')  
tab_control.add(tab2, text='Вторая работа')
tab_control.add(tab3, text='Третья работа')
# информация о задаче2
Label(tab1, text="Задание 2:Дано целое число, не меньшее 2. Выведите его").pack()
Label(tab1, text="наименьший натуральный делитель, отличный от 1.").pack()

# информация о задаче4
Label(tab2, text="Задание 4. В первый день спортсмен пробежал X километров, а затем он каждый день").pack()
Label(tab2, text="увеличивал пробег на 10% от предыдущего значения. По данному числу Y определите").pack()
Label(tab2, text="номер дня, на который пробег спортсмена составит не менее Y километров.").pack()
Label(tab2, text="Программа получает на вход действительные числа X и Y").pack()
Label(tab2, text="и должна вывести одно натуральное число.").pack()
# информация о задаче6
Label(tab3, text ="Определите среднее значение всех элементов последовательности, завершающейся числом 0.").pack()

# виджеты для задачи2
Label(tab1, text="Введите число больше 2").pack(pady=(5,0))
tab1N = Entry(tab1, width=70)
tab1N.pack()

Button(tab1, width=30, text="Поехали", command=chislo).pack(pady=(5,0))
# виджеты для задачи 4
Label(tab2, text="Сколько километров спортсмен пробежал в первый день?").pack(pady=(5,0))
tab2X = Entry(tab2, width=70)
tab2X.pack()

Label(tab2, text="Сколько километров спортсмен пробежал всего?").pack()
tab2Y = Entry(tab2, width=70)
tab2Y.pack()

Button(tab2, width=30, text="Поехали", command=day1).pack(pady=(5,0))

# виджеты для задачи 6
Label(tab3, text="введите число").pack(pady=(5,0))
tab3X = Entry(tab3, width=70)
tab3X.pack()

Button(tab3, width=30, text="Поехали", command=credznach).pack(pady=(5,0))
Rezyltat=Label(tab3, text='для ввыода текста')
Rezyltat.pack()
window.mainloop()