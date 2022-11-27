import requests
from tkinter import *
from tkinter import ttk
from pprint import pprint
import json

window = Tk()
window.title('Чикунов Д.В.')
window.geometry('800x500')

txt = Entry(window, width=10)
txt.grid(column=0, row=0)
txt.insert(0, 'cockroach')


def file(vivod, text):
    vivod = open('C:\\Users\\Dima\\Desktop\\УНИК\\УНИК\\pr11\\pr11vivod.txt', 'w')
    vivod.write(text)


def button():
    try:
        json = requests.get(f'https://api.github.com/users/{txt.get()}').json()
    except:
        json = requests.get(f'https://api.github.com/users/cockroach').json()
    try:
        company = json['company']
    except:
        company = 'None'
    try:
        created_at = json['created-at']
    except:
        created_at = 'None'
    try:
        email = json['email']
    except:
        email = 'None'
    try:
        id = json['id']
    except:
        id = 'None'
    try:
        name = json['name']
    except:
        name = 'None'
    try:
        url = json['url']
    except:
        url = 'None'
    file('C:\\Users\\Dima\\Desktop\\УНИК\\УНИК\\pr11\\pr11vivod.txt', f"'company': {company}\n'created_at': {created_at}\n'email':{email}\n'id':{id}\n'name':{name}\n'url':{url}")


btn = Button(window, text='ПОИСК', fg='red', bg='white', command=button)
btn.grid(column=2, row=0)

window.mainloop()