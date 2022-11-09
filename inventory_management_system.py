import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import datetime as dt
import time
from employee import EmployeeClass
from supplier import SupplierClass
from category import CategoryClass
from product import ProductClass
from sales import SalesClass


# IMS = Inventory Management System
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        self.tot_employee = StringVar()
        self.tot_supplier = StringVar()
        self.tot_category = StringVar()
        self.tot_product = StringVar()
        self.tot_sales = []
        self.get_tot_employee()
        self.get_tot_supplier()
        self.get_tot_category()
        self.get_tot_product()
        self.get_tot_sales()

        # title
        self.icon_title = Image.open("Images/logo.jpg")
        self.icon_title = self.icon_title.resize((50, 50), Image.ANTIALIAS)
        self.icon_title = ImageTk.PhotoImage(self.icon_title)
        title = Label(self.root, text="Inventory Management System",
                      font=("verdana", 30, "bold"), bg="#010c48",
                      fg="white", anchor="w", padx=20, image=self.icon_title,
                      compound=LEFT)
        title.place(x=0, y=0, relwidth=1, height=50)

        # log-out button
        btn_logout = Button(self.root, text="Logout", font=("verdana", 15, "bold"), command=self.log_out,
                            bg="red", fg="yellow", cursor="hand2")
        btn_logout.place(x=1250, y=8, height=35)

        # date and time
        date = dt.datetime.now()
        current_time = time.strftime('%H:%M')
        self.date_and_time = Label(self.root, text=f"Welcome to Inventory Management System\t\t "
                                                   f"Date: {date: %A, %B, %d, %Y}\t\t Time:{current_time}",
                                   font=("verdana", 9), bg="#4d636d",
                                   fg="white", compound=CENTER)
        self.date_and_time.place(x=0, y=50, relwidth=1, height=20)

        # left menu
        self.menu_logo = Image.open("Images/menu.jpg")
        self.menu_logo = self.menu_logo.resize((200, 200), Image.ANTIALIAS)
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)

        left_menu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        left_menu.place(x=0, y=79, width=225, height=598)

        lbl_menu_logo = Label(left_menu, image=self.menu_logo)
        lbl_menu_logo.pack(side=TOP, fill=X)

        menu_lbl = Label(left_menu, text="MENU", font=("verdana", 15, "bold"),
                         bg="#009688", fg="yellow")
        menu_lbl.pack(side=TOP, fill=X)

        # menu side icon
        self.icon_side = Image.open("Images/side.png")
        self.icon_side = self.icon_side.resize((30, 30), Image.ANTIALIAS)
        self.icon_side = ImageTk.PhotoImage(self.icon_side)

        # employee button
        employee_btn = Button(left_menu, text="Employee", font=("verdana", 15), command=self.employee,
                              bg="white", fg="green", bd=3, cursor="hand2", height=50,
                              image=self.icon_side, compound=LEFT, padx=5, anchor="w")
        employee_btn.pack(side=TOP, fill=X)

        # supplier button
        supplier_btn = Button(left_menu, text="Supplier", font=("verdana", 15), command=self.supplier,
                              bg="white", fg="green", bd=3, cursor="hand2", height=50,
                              image=self.icon_side, compound=LEFT, padx=5, anchor="w")
        supplier_btn.pack(side=TOP, fill=X)

        # category button
        category_btn = Button(left_menu, text="Category", font=("verdana", 15), command=self.category,
                              bg="white", fg="green", bd=3, cursor="hand2", height=50,
                              image=self.icon_side, compound=LEFT, padx=5, anchor="w")
        category_btn.pack(side=TOP, fill=X)

        # product button
        product_btn = Button(left_menu, text="Product", font=("verdana", 15), command=self.product,
                             bg="white", fg="green", bd=3, cursor="hand2", height=50,
                             image=self.icon_side, compound=LEFT, padx=5, anchor="w")
        product_btn.pack(side=TOP, fill=X)

        # sales button
        sales_btn = Button(left_menu, text="Sales", font=("verdana", 15), command=self.sales,
                           bg="white", fg="green", bd=3, cursor="hand2", height=50,
                           image=self.icon_side, compound=LEFT, padx=5, anchor="w")
        sales_btn.pack(side=TOP, fill=X)

        # exit button
        exit_btn = Button(left_menu, text="Exit", font=("verdana", 15), command=self.exit_program,
                          bg="white", fg="green", bd=3, cursor="hand2", height=50,
                          image=self.icon_side, compound=LEFT, padx=5, anchor="w")
        exit_btn.pack(side=TOP, fill=X)

        # content
        # employee content

        self.lbl_employee = Label(self.root, text=f"Total Employee\n[ {self.tot_employee} ]",
                                  bg="#33bbf9", fg="white", bd=5, relief=RIDGE,
                                  font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=100, height=170, width=300)

        # supplier
        self.lbl_supplier = Label(self.root, text=f"Total Supplier\n[ {self.tot_supplier} ]",
                                  bg="#33bbf9", fg="white", bd=5, relief=RIDGE,
                                  font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=100, height=170, width=300)

        # category
        self.lbl_category = Label(self.root, text=f"Total Category\n[ {self.tot_category} ]",
                                  bg="#33bbf9", fg="white", bd=5, relief=RIDGE,
                                  font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=100, height=170, width=300)

        # product
        self.lbl_product = Label(self.root, text=f"Total Product\n[ {self.tot_product} ]",
                                 bg="#33bbf9", fg="white", bd=5, relief=RIDGE,
                                 font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=170, width=300)

        # sales
        self.lbl_sales = Label(self.root, text=f"Total Sales\n[ {self.num_tot_sales} ]",
                               bg="#33bbf9", fg="white", bd=5, relief=RIDGE,
                               font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=170, width=300)

        # footer
        lbl_footer = Label(self.root, text="IMS-Inventory Management System \n "
                                           "For any technical issue contact: 09087634598",
                           font=("verdana", 9), bg="#4d636d",
                           fg="white", compound=CENTER)
        lbl_footer.pack(side=BOTTOM, fill=X)

    # ===================================================================================================================

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = EmployeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = SupplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CategoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ProductClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = SalesClass(self.new_win)

    def exit_program(self):
        leave = messagebox.askyesno("Confirm", "Do you really want to exit?", parent=self.root)
        if leave == 1:
            self.root.quit()

    def get_tot_employee(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM employee")
        rows = cur.fetchall()
        self.tot_employee = len(rows)

    def get_tot_supplier(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM supplier")
        rows = cur.fetchall()
        self.tot_supplier = len(rows)

    def get_tot_category(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM category")
        rows = cur.fetchall()
        self.tot_category = len(rows)

    def get_tot_product(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM product")
        rows = cur.fetchall()
        self.tot_product = len(rows)

    def get_tot_sales(self):
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.tot_sales.append(i)
        self.num_tot_sales = len(self.tot_sales)


    def log_out(self):
        log_confirm = messagebox.askyesno("Confirm", "Are you sure you want to log out?", parent=self.root)
        if log_confirm == 1:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
