import tkinter as tk
from canvas import app
from helpers import clean_screen
from products import render_main_products_screen

def render_main_login_screen(error=None):
    clean_screen()

    tk.Label(app,text="Username:").grid(row=0,column=0)
    username = tk.Entry(app)
    username.grid(row=0,column=1)
    tk.Label(app,text="Password:").grid(row=1,column=0)
    password = tk.Entry(app)
    password.grid(row=1,column=1)
    button = tk.Button(app,text="enter", bg="green",
              command=lambda: login(username.get(), password.get()))
    button.grid(row=2,column=1)
    if error:
        tk.Label(app,text=error).grid(row=3,column=1)



def login(username,password, error=None):
    with open("db/user_credentials_db.txt", "r") as file:
        data = file.readlines()
        for el in data:
            name, pwd = el.strip().split(", ")
            if name == username and pwd == password:
                render_main_products_screen()
                return

    render_main_login_screen(error="invalid username or password")





def register_action():
    print("register action")


def render_main_enter_screen():
    tk.Button(app,text="login",
              bg="green",
              fg="white",
              command=render_main_login_screen
              ).grid(row=0,column=0)
    tk.Button(app,text="register",
              bg="yellow",
              fg="black",).grid(row=0,column=1)





