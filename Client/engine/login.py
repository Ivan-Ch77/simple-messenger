from engine.request import post
from engine.messenger import main as mess
from tkinter import *
from tkinter import messagebox


def main():
    window = Tk()
    email = StringVar()
    password = StringVar()

    def login():
        if len(email.get()) != 0:
            if len(password.get()) != 0:
                response = post({'method': 'login', 'email': email.get().strio(), 'pass': password.get().strip()})
                if 'error' not in str(response):
                    window.destroy()
                    mess(response['response'])
                else:
                    messagebox.showinfo('осторожно', 'Либо email, либо пароль не верный')
            else:
                messagebox.showinfo('Пустота в моей душе', 'Пожалуйста введите email')
        else:
            messagebox.showinfo('Пустота в моей душе', 'Пожалуйста введите email')

    window.title('Вход')
    window.geometry('400x250')
    label = Label(window, text='Ваш email:')
    label.grid(column=0, row=0)
    entry = Entry(window, width=20, textvariable=email)
    entry.grid(column=1, row=0)
    label_ni = Label(window, text='Ваш пароль:')
    label_ni.grid(column=0, row=1)
    entry_ni = Entry(window, width=20, textvariable=password)
    button = Button(window, text='Готово', command=login)
    button.grid(column=2, row=1)
    window.mainloop()
    