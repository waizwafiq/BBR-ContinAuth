from tkinter import *
from functools import partial


class login:
    window = Tk()

    @staticmethod
    def toggle_fullscreen():
        login.window.attributes('-topmost', True)
        login.window.attributes('-fullscreen', True)
        login.window.state('zoomed')
        login.window.resizable(0, 0)

    @staticmethod
    def validate():
        print("Username entered :", username_verify.get())
        print("Password entered :", password_verify.get())

        if username_verify.get() == "waiz" and password_verify.get() == "1234":
            login.window.destroy()
            #login.login_success()
            print("success")
        else:
            username_login_entry.delete(0, END)
            password_login_entry.delete(0, END)

        return

    # @staticmethod
    # def login_success():
    #     global login_success_screen  # make login_success_screen global
    #     login_success_screen = Toplevel(login.window)
    #     login_success_screen.attributes('-toplevel', True)
    #     login_success_screen.title("Success")
    #     login_success_screen.geometry("300x200")
    #     Label(login_success_screen, text="Login Success", borderwidth=10).pack()
    #     txt = f"Welcome, {username_verify.get()}"
    #     Label(login_success_screen, text=txt, borderwidth=30).pack()
    #
    #     # create OK button
    #     Button(login_success_screen, text="OK", command=login.window.destroy).pack()

    @staticmethod
    def run():
        global username_verify, password_verify, username_login_entry, password_login_entry
        # window
        window = login.window

        window.title("Login")
        login.toggle_fullscreen()

        Label(window, text="Please enter details below to login",
              borderwidth=window.winfo_screenwidth() // 10).pack()
        Label(window, text="").pack()

        username_verify = StringVar()
        password_verify = StringVar()

        Label(window, text="Username ").pack()
        username_login_entry = Entry(window, textvariable=username_verify)
        username_login_entry.pack()
        Label(window, text="").pack()
        Label(window, text="Password ").pack()
        password_login_entry = Entry(window, textvariable=password_verify, show='◉')
        password_login_entry.pack()
        Label(window, text="").pack()
        Button(window, text="Login", width=10, height=1, command=login.validate).pack()

        window.mainloop()
