from tkinter import *
from functools import partial


class login:

    window = Tk()

    @staticmethod
    def validateLogin(username, password):
        print("Username entered :", username.get())
        print("Password entered :", password.get())
        if username.get() == "waiz" and password.get() == "1234":
            print("success")
            login.window.destroy()
        return

    @staticmethod
    def run():
        # window
        login.window.geometry('400x150')
        login.window.title('Login')

        # username label and text entry box
        Label(login.window, text="User Name").grid(row=0, column=0)
        username = StringVar()
        Entry(login.window, textvariable=username).grid(row=0, column=1)

        # password label and password entry box
        Label(login.window, text="Password").grid(row=1, column=0)
        password = StringVar()
        Entry(login.window, textvariable=password, show='◉').grid(row=1, column=1)

        validateLogin = partial(login.validateLogin, username, password)

        # login button
        Button(login.window, text="Login", command=validateLogin).grid(row=4, column=3)

        login.window.mainloop()
