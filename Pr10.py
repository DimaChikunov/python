import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Checkbutton
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox

window = Tk()
window.geometry('800x500')
window.title("Чикунов Д.В.")


tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Вкладка 1')
tabControl.add(tab2, text='Вкладка 2')
tabControl.add(tab3, text='Вкладка 3')

def proizv():
    a = EntryA.get()
    a = int(a)

    b = EntryB.get()
    b = int(b)
    result = str(a * b)
    EntryC.delete(0, END)
    EntryC.insert(0, result)
def summa():
    a = EntryA.get()
    a = int(a)

    b = EntryB.get()
    b = int(b)
    result = str(a + b)
    EntryC.delete(0, END)
    EntryC.insert(0, result)
def raz():
    a = EntryA.get()
    a = int(a)

    b = EntryB.get()
    b = int(b)
    result = str(a - b)
    EntryC.delete(0, END)
    EntryC.insert(0, result)
def delenie():
    a = EntryA.get()
    a = int(a)

    b = EntryB.get()
    b = int(b)
    result = str(a // b)
    EntryC.delete(0, END)
    EntryC.insert(0, result)


Label(tab1, text='Первое число').grid(row=0, sticky=W)
Label(tab1, text='Второе число').grid(row=1, sticky=W)

EntryA = Entry(tab1, width=10, font='Arial 14')
EntryB = Entry(tab1, width=10, font='Arial 14')
EntryC = Entry(tab1, width=20, font='Arial 14')


EntryA.grid(row=0, column=1, sticky=E)
EntryB.grid(row=1, column=1, sticky=E)

EntryC.grid(row=2, columnspan=2)


but = Button(tab1, text='*',command=proizv)
but.grid(row=0, column=2, sticky=E)
but = Button(tab1, text='+',command=summa)
but.grid(row=1, column=2, sticky=E)
but = Button(tab1, text='-',command=raz)
but.grid(row=1, column=3, sticky=E)
but = Button(tab1, text='/',command=delenie)
but.grid(row=0, column=3, sticky=E)


lbl=Label(tab2)
lbl.grid(column=2, row=1)
txt = scrolledtext.ScrolledText(tab3, height=14, width=70)
txt.grid(column=0, row=0)



cs1=BooleanVar()
cs2=BooleanVar()
cs3=BooleanVar()
ccl1 = Checkbutton(tab2, text="Первый вариант", var=cs1)
ccl2 = Checkbutton(tab2, text="Второй вариант", var=cs2)
ccl3 = Checkbutton(tab2, text="Третий вариант", var=cs3)
ccl1.grid(column=0, row=0)
ccl2.grid(column=0, row=1)
ccl3.grid(column=0, row=2)



def button():
    if ((ccl1.instate(['selected']) == True) and (ccl2.instate(['selected']) == True) and (ccl3.instate(['selected']) == True)):
        messagebox.showinfo('Text', 'Вы выбрали первый, второй и третий вар.')
    elif ((ccl1.instate(['selected']) == True) and (ccl2.instate(['selected']) == True)):
        messagebox.showinfo('Text', 'Вы выбрали первый и второй вар.')
    elif ((ccl2.instate(['selected']) == True) and (ccl3.instate(['selected']) == True)):
        messagebox.showinfo('Text', 'Вы выбрали второй и третий вар.')
    elif ((ccl1.instate(['selected']) == True) and (ccl3.instate(['selected']) == True)):
        messagebox.showinfo('Text', 'Вы выбрали первый и третий вар.')
    elif ccl1.instate(['selected'])== True:
        messagebox.showinfo('Text', 'Вы выбрали первый вар.')
    elif ccl2.instate(['selected'])== True:
        messagebox.showinfo('Text', 'Вы выбрали второй вар.')
    elif ccl3.instate(['selected'])== True:
        messagebox.showinfo('Text', 'Вы выбрали третий вар.')
    else:
        messagebox.showinfo('Text', 'Вы ничего не выбрали.......')

btn= Button(tab2,text="ТЫК!", command=button)
btn.grid(column=3, row=1)


def open():
    file = filedialog.askopenfile()
    with open(file, "r+", encoding= 'utf-8-sig') as f:
        line = f.read()
        txt.insert('1.0', line)
        txt.place(x=0, y=0)

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label="OPEN", command=open)
new_item.add_separator()
menu.add_cascade(label="Файл", menu=new_item)
window.config(menu=menu)



tabControl.pack(expand=1, fill="both")


window.mainloop()