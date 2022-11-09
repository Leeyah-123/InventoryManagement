from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import time


# IMS = Inventory Management System
class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.resizable(False, False)

# ========================All Variables=================================================================================
        self.var_search = StringVar()
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()
        self.var_cal_input = StringVar()
        self.cart_list = []

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
        btn_logout = Button(self.root, text="Logout", font=("verdana", 15, "bold"),
                            bg="red", fg="yellow", cursor="hand2")
        btn_logout.place(x=1250, y=8, height=35)

        # date and time
        self.date_and_time = Label(self.root, text="Welcome to Inventory Management System\t\t "
                                                   "Date: DD-MM-YYYY\t\t Time:HH:MM:SS",
                                   font=("verdana", 9), bg="#4d636d",
                                   fg="white", compound=CENTER)
        self.date_and_time.place(x=0, y=50, relwidth=1, height=20)

        # footer
        lbl_footer = Label(self.root, text="IMS-Inventory Management System \n "
                                           "For any technical issue contact: 09087634598",
                           font=("times new roman", 16), bg="#4d636d", activeforeground="white",
                           fg="white", compound=CENTER, activebackground="#4d636d")
        lbl_footer.pack(side=BOTTOM, fill=X)

# ============================Product Frame=============================================================================
        product_frame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        product_frame1.place(x=10, y=90, width=410, height=550)

        p_title = Label(product_frame1, text="All Products", font=("verdana", 20, "bold"), bg="#262626", fg="white")
        p_title.pack(side=TOP, fill=X)

        product_frame2 = Frame(product_frame1, bd=2, relief=RIDGE, bg="white")
        product_frame2.place(x=2, y=42, width=398, height=90)

        lbl_search = Label(product_frame2, text="Search Product | By Name",
                           font=("goudy old style", 15, "bold"), bg="white", fg="green")
        lbl_search.place(x=2, y=5)

        lbl_prod_name = Label(product_frame2, text="Product Name",
                         font=("goudy old style", 15, "bold"), bg="white")
        lbl_prod_name.place(x=5, y=45)

        txt_search = Entry(product_frame2, textvariable=self.var_search,
                           font=("goudy old style", 15), bg="lightyellow")
        txt_search.place(x=130, y=48, width=150, height=25)

        btn_search = Button(product_frame2, text="Search", font=("goudy old style", 15),
                            bg="#2196f3", fg="white", cursor="hand2", command=self.search)

        btn_search.place(x=295, y=48, width=100, height=25)

        btn_show_all = Button(product_frame2, text="Show All", font=("goudy old style", 15),
                              bg="#083531", fg="white", cursor="hand2", command=self.show)

        btn_show_all.place(x=295, y=10, width=100, height=25)

        product_frame_3 = Frame(product_frame1, bd=3, relief=RIDGE)
        product_frame_3.place(x=2, y=140, width=395, height=375)

        scrollx = Scrollbar(product_frame_3, orient=HORIZONTAL)
        scrolly = Scrollbar(product_frame_3, orient=VERTICAL)

        self.ProductTable = ttk.Treeview(product_frame_3, columns=("pid", "name", "price", "qty", "status"),
                                         xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pid", text="Product ID")
        self.ProductTable.heading("name", text="Name")
        self.ProductTable.heading("price", text="Price")
        self.ProductTable.heading("qty", text="QTY")
        self.ProductTable.heading("status", text="Status")

        self.ProductTable["show"] = "headings"

        self.ProductTable.column("pid", width=40)
        self.ProductTable.column("name", width=100)
        self.ProductTable.column("price", width=100)
        self.ProductTable.column("qty", width=50)
        self.ProductTable.column("status", width=90)

        self.ProductTable.pack(fill=BOTH, expand=1)
        self.ProductTable.bind("<ButtonRelease - 1>", self.get_data)

        lbl_note = Label(product_frame1, text="Note: To remove product from cart, Enter QTY=0",
                         font=("goudy old style", 12), anchor="w", bg="white", fg="red")
        lbl_note.pack(side=BOTTOM, fill=X)

# ======================================Customer Frame==================================================================
        customer_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        customer_frame.place(x=420, y=90, width=530, height=70)

        c_title = Label(customer_frame, text="Customer Details", font=("goudy old style", 15), bg="lightgrey")
        c_title.pack(side=TOP, fill=X)

        lbl_name = Label(customer_frame, text="Name",
                         font=("times new roman", 15), bg="white")
        lbl_name.place(x=5, y=35)

        txt_name = Entry(customer_frame, textvariable=self.var_cname,
                         font=("times new roman", 13), bg="lightyellow")
        txt_name.place(x=65, y=35, width=180)

        lbl_contact = Label(customer_frame, text="Contact No.",
                            font=("times new roman", 15), bg="white")
        lbl_contact.place(x=260, y=35)

        txt_contact = Entry(customer_frame, textvariable=self.var_contact,
                            font=("times new roman", 13), bg="lightyellow")
        txt_contact.place(x=360, y=35, width=140)

# ===============================Calculator=============================================================================
        calculator_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        calculator_frame.place(x=420, y=190, width=530, height=360)

        cal_frame = Frame(calculator_frame, bd=9, relief=RIDGE, bg="white")
        cal_frame.place(x=5, y=10, width=268, height=340)

        self.txt_cal_input = Entry(cal_frame, textvariable=self.var_cal_input, font=('arial', 15, 'bold'),
                                   width=21, bd=10, relief=GROOVE, state="readonly", justify=RIGHT)
        self.txt_cal_input.grid(row=0, columnspan=4)

        btn_7 = Button(cal_frame, text='7', font=('arial', 15, 'bold'), cursor="hand2",
                       bd=5, width=4, pady=10, command=lambda: self.get_input(7))
        btn_7.grid(row=1, column=0)
        btn_8 = Button(cal_frame, text='8', font=('arial', 15, 'bold'), cursor="hand2",
                       bd=5, width=4, pady=10, command=lambda: self.get_input(8))
        btn_8.grid(row=1, column=1)
        btn_9 = Button(cal_frame, text='9', font=('arial', 15, 'bold'), cursor="hand2",
                       bd=5, width=4, pady=10, command=lambda: self.get_input(9))
        btn_9.grid(row=1, column=2)
        btn_sum = Button(cal_frame, text='+', font=('arial', 15, 'bold'), cursor="hand2",
                         bd=5, width=4, pady=10, command=lambda: self.get_input('+'))
        btn_sum.grid(row=1, column=3)

        btn_4 = Button(cal_frame, text='4', font=('arial', 15, 'bold'), cursor="hand2",
                       bd=5, width=4, pady=10, command=lambda: self.get_input(4))
        btn_4.grid(row=2, column=0)
        btn_5 = Button(cal_frame, text='5', font=('arial', 15, 'bold'), cursor="hand2",
                       bd=5, width=4, pady=10, command=lambda: self.get_input(5))
        btn_5.grid(row=2, column=1)
        btn_6 = Button(cal_frame, text="6", font=('arial', 15, 'bold'), cursor="hand2",
                       bd=5, width=4, pady=10, command=lambda: self.get_input(6))
        btn_6.grid(row=2, column=2)
        btn_sub = Button(cal_frame, text='-', font=('arial', 15, 'bold'), cursor="hand2",
                         bd=5, width=4, pady=10, command=lambda: self.get_input('-'))
        btn_sub.grid(row=2, column=3)

        btn_1 = Button(cal_frame, text='1', font=('arial', 15, 'bold'), cursor="hand2",
                       bd=5, width=4, pady=10, command=lambda: self.get_input(1))
        btn_1.grid(row=3, column=0)
        btn_2 = Button(cal_frame, text='2', font=('arial', 15, 'bold'), cursor="hand2",
                       bd=5, width=4, pady=10, command=lambda: self.get_input(2))
        btn_2.grid(row=3, column=1)
        btn_3 = Button(cal_frame, text="3", font=('arial', 15, 'bold'), cursor="hand2",
                       bd=5, width=4, pady=10, command=lambda: self.get_input(3))
        btn_3.grid(row=3, column=2)
        btn_mul = Button(cal_frame, text='*', font=('arial', 15, 'bold'), cursor="hand2",
                         bd=5, width=4, pady=10, command=lambda: self.get_input('*'))
        btn_mul.grid(row=3, column=3)

        btn_0 = Button(cal_frame, text='0', font=('arial', 15, 'bold'), cursor="hand2",
                       bd=5, width=4, pady=15, command=lambda: self.get_input(0))
        btn_0.grid(row=4, column=0)
        btn_c = Button(cal_frame, text='AC', font=('arial', 15, 'bold'), cursor="hand2",
                       bd=5, width=4, pady=15, command=self.clear_cal)
        btn_c.grid(row=4, column=1)
        btn_equal = Button(cal_frame, text="=", font=('arial', 15, 'bold'), cursor="hand2",
                           bd=5, width=4, pady=15, command=self.perform_cal)
        btn_equal.grid(row=4, column=2)
        btn_div = Button(cal_frame, text='/', font=('arial', 15, 'bold'), cursor="hand2",
                         bd=5, width=4, pady=15, command=lambda: self.get_input('/'))
        btn_div.grid(row=4, column=3)

        cart_frame = Frame(calculator_frame, bd=3, relief=RIDGE)
        cart_frame.place(x=280, y=8, width=245, height=342)
        self.cart_title = Label(cart_frame, text="CART \tTotal Product: [0]", font=("goudy old style", 15), bg="lightgrey")
        self.cart_title.pack(side=TOP, fill=X)

        scrollx = Scrollbar(cart_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(cart_frame, orient=VERTICAL)

        self.CartTable = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty"),
                                      xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid", text="Product ID")
        self.CartTable.heading("name", text="Name")
        self.CartTable.heading("price", text="Price")
        self.CartTable.heading("qty", text="QTY")

        self.CartTable["show"] = "headings"

        self.CartTable.column("pid", width=70)
        self.CartTable.column("name", width=100)
        self.CartTable.column("price", width=90)
        self.CartTable.column("qty", width=40)

        self.CartTable.pack(fill=BOTH, expand=1)
        self.CartTable.bind("<ButtonRelease - 1>", self.get_data_cart)

# ================================Cart Buttons==========================================================================
        add_cart = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        add_cart.place(x=420, y=550, width=530, height=90)

        lbl_p_name = Label(add_cart, text="Product Name", font=("goudy old style", 15), bg="white")
        lbl_p_name.place(x=5, y=5)

        txt_p_name = Entry(add_cart, textvariable=self.var_pname, font=("goudy old style", 15),
                           bg="lightyellow", state="readonly")
        txt_p_name.place(x=5, y=35, width=190, height=23)

        lbl_p_price = Label(add_cart, text="Price Per Qty", font=("goudy old style", 15), bg="white")
        lbl_p_price.place(x=230, y=5)

        txt_p_price = Entry(add_cart, textvariable=self.var_price, font=("goudy old style", 15),
                            bg="lightyellow", state="readonly")
        txt_p_price.place(x=230, y=35, width=150, height=23)

        lbl_p_qty = Label(add_cart, text="Quantity", font=("goudy old style", 15), bg="white")
        lbl_p_qty.place(x=390, y=5)

        txt_p_qty = Entry(add_cart, textvariable=self.var_qty, font=("goudy old style", 15),
                          bg="lightyellow")
        txt_p_qty.place(x=390, y=35, width=120, height=23)

        self.lbl_in_stock = Label(add_cart, text="In Stock", font=("goudy old style", 15), bg="white", bd=0)
        self.lbl_in_stock.place(x=5, y=58)

        btn_clear_cart = Button(add_cart, text="Clear", font=("times new roman", 15, "bold"),
                                bg="lightgrey", cursor="hand2", command=self.clear_cart)
        btn_clear_cart.place(x=180, y=58, width=150, height=22)

        btn_add_cart = Button(add_cart, text="Add | Update Cart", font=("times new roman", 15, "bold"),
                              bg="orange", cursor="hand2", command=self.update_cart)
        btn_add_cart.place(x=340, y=58, width=180, height=22)

# =======================Billing Area===================================================================================
        bill_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_frame.place(x=953, y=90, width=394, height=431)

        b_title = Label(bill_frame, text="Customer Bill Area", font=("goudy old style", 20, "bold"),
                        bg="#f44336", fg="white")
        b_title.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
        scrolly2.pack(side=RIGHT, fill=Y)

        self.txt_bill_area = Text(bill_frame, yscrollcommand=scrolly2.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly2.config(command=self.txt_bill_area.yview)

# =======================Billing Buttons================================================================================
        bill_menu_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_menu_frame.place(x=953, y=520, width=394, height=120)

        self.lbl_amount = Label(bill_menu_frame, text="Bill Amount\n [0]", font=("goudy old style", 15, "bold"),
                                bg="#3f51b5", fg="white")
        self.lbl_amount.place(x=2, y=5, width=120, height=60)

        self.lbl_discount = Label(bill_menu_frame, text="Discount\n [5%]", font=("goudy old style", 15, "bold"),
                                  bg="#8bc34a", fg="white")
        self.lbl_discount.place(x=124, y=5, width=120, height=60)

        self.lbl_net_pay = Label(bill_menu_frame, text="Net Pay\n [0]", font=("goudy old style", 15, "bold"),
                                 bg="#607d8b", fg="white")
        self.lbl_net_pay.place(x=246, y=5, width=145, height=60)

        btn_print = Button(bill_menu_frame, text="Print", font=("goudy old style", 15, "bold"),
                           bg="lightgreen", fg="white", cursor='hand2', command=self.print_bill)
        btn_print.place(x=2, y=70, width=120, height=40)

        btn_clear_all = Button(bill_menu_frame, text="Clear All", font=("goudy old style", 15, "bold"),
                               bg="grey", fg="white", cursor='hand2', command=self.clear_bill)
        btn_clear_all.place(x=124, y=70, width=120, height=40)

        btn_generate = Button(bill_menu_frame, text="Generate|Save Bill", font=("goudy old style", 13, "bold"),
                              bg="#009688", fg="white", cursor='hand2', command=self.generate_bill)
        btn_generate.place(x=246, y=70, width=145, height=40)
        self.show()

# ==========================All Functions===============================================================================
    def get_input(self, num):
        x_num = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(x_num)

    def clear_cal(self):
        self.var_cal_input.set("")

    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT pid, name, price, qty, status FROM product where status='Active'")
            rows = cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def search(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Search input required", parent=self.root)
            else:
                cur.execute("SELECT pid, name, price, qty, status FROM product WHERE name LIKE '%"
                            + self.var_search.get() + "%' and status='Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert("", END, values=row)
                    self.var_search.set("")
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def get_data(self, ev):
        f = self.ProductTable.focus()
        content = self.ProductTable.item(f)
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_in_stock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')

    def get_data_cart(self, ev):
        f = self.CartTable.focus()
        content = self.CartTable.item(f)
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_in_stock.config(text=f"In Stock [{str(row[4])}]")
        # self.var_stock.set(row[4])
        self.var_qty.set(row[3])

    def update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror('Error', 'Please select product from the list', parent=self.root)
        elif self.var_qty.get() == '':
            messagebox.showerror('Error', 'Quantity is required', parent=self.root)
        elif int(self.var_qty.get()) > int(self.var_stock.get()):
            messagebox.showerror('Error', 'Invalid Quantity', parent=self.root)
        else:
            price_cal = self.var_price.get()
            # pid, name, price, qty, status
            cart_data = [self.var_pid.get(), self.var_pname.get(), price_cal, self.var_qty.get(), self.var_stock.get()]
            # =============update cart=======================
            present = 'no'
            index_ = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index_ += 1
            if present == 'yes':
                op = messagebox.askyesno('Confirm', 'Product already in cart\n '
                                                    'Do you want to update or remove from cart', parent=self.root)
                if op:
                    if self.var_qty.get() == "0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2] = price_cal  # price
                        self.cart_list[index_][3] = self.var_qty.get()  # qty

            else:
                self.cart_list.append(cart_data)

            self.show_cart()
            self.bill_update()

    def bill_update(self):
        self.bill_amnt = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            self.bill_amnt += float(row[2]) * int(row[3])
        self.discount = (self.bill_amnt * 5)/100
        self.net_pay = self.bill_amnt - self.discount
        self.lbl_amount.config(text=f"Bill Amount\n [N{str(self.bill_amnt)}]")
        self.lbl_net_pay.config(text=f"Net Pay\n [N{str(self.net_pay)}]")
        self.cart_title.config(text=f"CART \tTotal Product: [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def generate_bill(self):
        if self.var_cname.get() == '' or self.var_contact.get() == '':
            messagebox.showerror("Error", "Please fill in all necessary fields", parent=self.root)
        elif len(self.cart_list) == 0:
            messagebox.showerror("Error", "Please add product to the cart", parent=self.root)
        else:
            # =========================Bill Top======================================================
            self.bill_top()
            # =========================Bill Middle===================================================
            self.bill_middle()
            # =========================Bill Last=====================================================
            self.bill_bottom()

            fp = open(f'bill/{str(self.invoice)}.txt', 'w')
            fp.write(self.txt_bill_area.get('1.0', END))
            fp.close()
            messagebox.showinfo('Saved', 'Bill has been saved', parent=self.root)

    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
\t\tSANI-Inventory
\t Phone No. 09087634598, Sabo Kaduna
{str('='*46)}
Customer Name: {self.var_cname.get()}
Phone No. :{self.var_contact.get()}
Bill No. :{str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str('='*46)}
Product Name\t\t\tQTY\tPrice
{str('='*46)}
'''
        self.txt_bill_area.delete('1.0', END)
        self.txt_bill_area.insert('1.0', bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp = f'''
{str('='*46)}
Bill Amount\t\t\t\tN{self.bill_amnt}
Discount\t\t\t\tN{self.discount}
Net Pay\t\t\t\tN{self.net_pay}
{str('='*46)}\n
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)

    def bill_middle(self):
        try:
            for row in self.cart_list:
                name = row[1]
                qty = row[3]
                price = float(row[2]) * int(row[3])
                price = str(price)
                self.txt_bill_area.insert(END, "\n " + name + "\t\t\t" + qty + "\tN" + price)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def clear_cart(self):
        self.var_cname.set('')
        self.var_contact.set('')
        self.var_qty.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.lbl_in_stock.config(text="In Stock [0]")

    def clear_bill(self):
        op = messagebox.askyesno("Confirm", "Do you really want to clear out the bill?", parent=self.root)
        if op:
            self.clear_cart()
            del self.cart_list[:]
            self.lbl_amount.config(text=f"Bill Amount\n [N0]")
            self.lbl_net_pay.config(text=f"Net Pay\n [N0]")
            self.cart_title.config(text=f"CART \tTotal Product: [0]")
            self.var_search.set("")
            self.show()
            self.show_cart()
            self.txt_bill_area.delete('1.0', END)

    def print_bill(self):
        messagebox.showinfo("Print", "Function currently disabled", parent=self.root)


# ======================================================================================================================
if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
