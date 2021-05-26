from tkinter import *
from functools import partial


class login:
    window = Tk()

    @staticmethod
    def toggle_fullscreen():
        window = login.window
        window.attributes("-fullscreen", True)
        return "break"

    @staticmethod
    def validate():
        print("Username entered :", username_verify.get())
        print("Password entered :", password_verify.get())

        if username_verify.get() == "waiz" and password_verify.get() == "1234":
            login.login_success()
            print("success")
        else:
            username_login_entry.delete(0, END)
            password_login_entry.delete(0, END)

        return

    @staticmethod
    def login_success():
        global login_success_screen  # make login_success_screen global
        login_success_screen = Toplevel(login.window)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()

        # create OK button
        Button(login_success_screen, text="OK", command=login.window.destroy).pack()

    @staticmethod
    def run():
        global username_verify, password_verify, username_login_entry, password_login_entry
        # window
        login_screen = login.window
        login.toggle_fullscreen()

        login_screen.title("Login")
        login_screen.geometry("300x250")
        Label(login_screen, text="Please enter details below to login",
              borderwidth=login_screen.winfo_screenwidth() // 10).pack()
        Label(login_screen, text="").pack()

        username_verify = StringVar()
        password_verify = StringVar()

        Label(login_screen, text="Username ").pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Password ").pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
        password_login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1, command=login.validate).pack()

        login_screen.mainloop()
