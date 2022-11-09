from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from inventory_management_system import IMS


# IMS = Inventory Management System
class LoginClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x300+400+200")
        self.root.title("Login")
        self.root.focus_force()
        self.root.resizable(False, False)

        self.user_name = StringVar()
        self.password = StringVar()
        self.names = []

        user_name_lbl = Label(self.root, text="Username", font=("verdana", 15, "bold"))
        user_name_lbl.place(x=10, y=10)

        txt_user_name = Entry(self.root, textvariable=self.user_name, font=("verdana", 15), bg="lightyellow")
        txt_user_name.place(x=200, y=10, width=250)

        password_lbl = Label(self.root, text="Password", font=("verdana", 15, "bold"))
        password_lbl.place(x=10, y=60)

        txt_password = Entry(self.root, textvariable=self.password, font=("verdana", 15), bg="lightyellow", show="*")
        txt_password.place(x=200, y=60, width=250)

        btn_login = Button(self.root, text="Login", font=("verdana", 15, "bold"),
                           bg="green", cursor="hand2", command=self.login)
        btn_login.place(x=10, y=110, width=100)

    def login(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        cur.execute("SELECT name FROM employee WHERE utype='Admin'")
        row = cur.fetchall()
        for i in row:
            name = i[0]
            self.names.append(name)
        if self.user_name.get() not in self.names:
            messagebox.showerror("Error", "Invalid Username", parent=self.root)
        else:
            if self.password.get() == "Admin1234":
                self.new_win = Toplevel(self.root)
                self.new_obj = IMS(self.new_win)
            else:
                messagebox.showerror("Error", "Invalid password", parent=self.root)
        con.commit()
        con.close()
        self.user_name.set("")
        self.password.set("")


if __name__ == "__main__":
    root = Tk()
    obj = LoginClass(root)
    root.mainloop()
