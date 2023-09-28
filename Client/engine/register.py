from engine.request import post
from engine.messenger import main as mess
from tkinter import *
from tkinter import messagebox


def main():
    window = Tk()
    text = StringVar()
    code = None
    email = None
    password = None
    last_name = None
    first_name = None

    def namaewa_ni():
        nonlocal first_name, last_name
        if len(text.get()) != 0:
            if len(text.get().split()) >= 2:
                first_name = text.get().split()[0]
                last_name = text.get().split()[1]
            else:
                first_name = text.get().split()[0]
                last_name = 'None'
            params = {'method': 'confirm', 'email': email, 'pass': password, 'first_name': first_name, 'last_name':last_name}
            response = post(params)
            window.destroy()
            mess(response['response'])
        else:
            messagebox.showinfo('Пустота в моей душе', 'Пожалуйста введите имя и фамилия')


    def namaewa():
        nonlocal password
        if len(text.get()) != 0:
            if len(text.get()) > 6:
                password = text.get()
                label.configure(text='Ваше имя и фамилия:')
                text.set('')
                button.configure(command=namaewa_ni)
            else:
                messagebox.showinfo('Пустота в моей душе', 'Пароль должен быть длинее 6 символов')
        else:
            messagebox.showinfo('Пустота в моей душе', 'Пожалуйста придумайте пароль')


    def check_code():
        if len(text.get()) != 0:
            if str(code) == text.get():
                label.configure(text='Придумайте пароль')
                text.set('')
                button.configure(command=namaewa)
            else:
                messagebox.showinfo('Неправильно', 'Код подтверждения не верный!')
        else:
            messagebox.showinfo('Пустота в моей душе', 'Введите код подтверждения')


    def reg_code():
        nonlocal email, code
        if len(text.get()) != 0:
            params = {'method': 'register', 'email': text.get()}
            code = post(params)
            if 'error' not in str(code):
                email = text.get()
                code = code['code']
                label.configure(text='Код подтверждения:')
                text.set('')
                button.configure(command=check_code)
            else:
                messagebox.showinfo('Пустота в моей душе', 'Пожалуйста, введите ваш email!')
        else:
            messagebox.showinfo('Пустота в моей душе', 'Пожалуйста, введите ваш email!')
            text.set('')

    window.title('Регистрация')
    window.geometry('400x250')
    label = Label(window, text='Вфш email:')
    label.grid(column=1, row=0)
    entry = Entry(window, width=20, textvariable=text)
    entry.grid(column=1, row=0)
    button = Button(window, text='Готово', command=reg_code)
    button.grid(column=3, row=0)
    window.mainloop()