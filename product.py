from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


# IMS = Inventory Management System
class ProductClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+227+130")
        self.root.title("Product Dashboard")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False, False)

# ==================================All Variables=======================================================================
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()

        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()

        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

# =================================Product Frame========================================================================
        product_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        product_frame.place(x=10, y=10, width=450, height=480)

# ===================================title==============================================================================
        title = Label(product_frame, text="Manage Product Details", bg="#0f4d7d",
                      fg="white", font=("times new roman", 15))
        title.pack(side=TOP, fill=X)

# ==================================Labels==============================================================================
        lbl_category = Label(product_frame, text="Category", bg="white",
                             font=("times new roman", 15))
        lbl_category.place(x=30, y=60)

        lbl_supplier = Label(product_frame, text="Supplier", bg="white",
                             font=("times new roman", 15))
        lbl_supplier.place(x=30, y=110)

        lbl_product_name = Label(product_frame, text="Product Name", bg="white",
                                 font=("times new roman", 15))
        lbl_product_name.place(x=30, y=160)

        lbl_price = Label(product_frame, text="Price", bg="white",
                          font=("times new roman", 15))
        lbl_price.place(x=30, y=210)

        lbl_qty = Label(product_frame, text="Quantity", bg="white",
                        font=("times new roman", 15))
        lbl_qty.place(x=30, y=260)

        lbl_status = Label(product_frame, text="Status", bg="white",
                           font=("times new roman", 15))
        lbl_status.place(x=30, y=310)

# ===============================Entry==================================================================================
        cmb_cat = ttk.Combobox(product_frame, textvariable=self.var_cat, values=self.cat_list,
                               state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_frame, textvariable=self.var_sup, values=self.sup_list,
                               state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_sup.place(x=150, y=110, width=200)
        cmb_sup.current(0)

        txt_name = Entry(product_frame, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow")
        txt_name.place(x=150, y=160, width=200)

        txt_price = Entry(product_frame, textvariable=self.var_price, font=("goudy old style", 15), bg="lightyellow")
        txt_price.place(x=150, y=210, width=200)

        txt_qty = Entry(product_frame, textvariable=self.var_qty, font=("goudy old style", 15), bg="lightyellow")
        txt_qty.place(x=150, y=260, width=200)

        cmb_status = ttk.Combobox(product_frame, textvariable=self.var_status, values=("Active", "Inactive"),
                                  state="readonly", justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)

# =========================buttons======================================================================================
        btn_add = Button(product_frame, text="Save", font=("goudy old style", 15),
                         bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        btn_add.place(x=10, y=400, width=100, height=40)

        btn_update = Button(product_frame, text="Update", font=("goudy old style", 15),
                            bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        btn_update.place(x=120, y=400, width=100, height=40)

        btn_delete = Button(product_frame, text="Delete", font=("goudy old style", 15),
                            bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        btn_delete.place(x=230, y=400, width=100, height=40)

        btn_clear = Button(product_frame, text="Clear", font=("goudy old style", 15),
                           bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=340, y=400, width=100, height=40)

# =======================search frame===================================================================================
        search_frame = LabelFrame(self.root, text="Search Employee", bg="white")
        search_frame.place(x=480, y=10, width=600, height=70)

# =========================search options===============================================================================
        search = ttk.Combobox(search_frame, textvariable=self.var_search_by,
                              values=("Select", "Category", "Supplier", "Product Name"),
                              state="readonly", justify=CENTER, font=("goudy old style", 15))
        search.place(x=10, y=10, width=180)
        search.current(0)

        txt_search = Entry(search_frame, textvariable=self.var_search_txt, font=("goudy old style", 15),
                           bg="lightyellow")
        txt_search.place(x=200, y=10)

# ==========================search button===============================================================================
        btn_search = Button(search_frame, text="Search", font=("goudy old style", 15),
                            bg="#4caf50", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=410, y=10, width=150, height=26)

# ===========================Product Details============================================================================
        product_frame = Frame(self.root, bd=3, relief=RIDGE)
        product_frame.place(x=480, y=100, width=600, height=390)

        scrollx = Scrollbar(product_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(product_frame, orient=VERTICAL)

        self.product_table = ttk.Treeview(product_frame, columns=("pid", "category", "supplier", "name",
                                                                  "price", "qty", "status"),
                                          xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="Product ID")
        self.product_table.heading("category", text="Category")
        self.product_table.heading("supplier", text="Supplier")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Quantity")
        self.product_table.heading("status", text="Status")

        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=90)
        self.product_table.column("category", width=140)
        self.product_table.column("supplier", width=150)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=120)
        self.product_table.column("qty", width=105)
        self.product_table.column("status", width=105)

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease - 1>", self.get_data)

        self.show()

# ============================functions=================================================================================

    def fetch_cat_sup(self):
        self.cat_list.append("<Empty>")
        self.sup_list.append("<Empty>")
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("SELECT name FROM supplier")
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def add(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select" or self.var_cat.get() == "<Empty>" or self.var_sup.get() == "<Empty>" or \
                    self.var_sup.get() == "Select" or self.var_name.get() == "":
                messagebox.showerror("Error", "Please fill in all input fields", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Product name already assigned", parent=self.root)
                else:
                    cur.execute("INSERT INTO product (category, supplier, name, price, qty, status)"
                                "VALUES (?, ?, ?, ?, ?, ?)",
                                (self.var_cat.get(), self.var_sup.get(),
                                 self.var_name.get(), self.var_price.get(),
                                 self.var_qty.get(), self.var_status.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Product added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def show(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def get_data(self, ev):
        f = self.product_table.focus()
        content = self.product_table.item(f)
        row = content['values']

        self.var_pid.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2])
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6])

    def update(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please select product from list", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    cur.execute("UPDATE product set category=?, supplier=?, name=?, "
                                "price=?, qty=?, status=? WHERE (pid=?)",
                                (self.var_cat.get(), self.var_sup.get(),
                                 self.var_name.get(), self.var_price.get(),
                                 self.var_qty.get(), self.var_status.get(),
                                 self.var_pid.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Product updated successfully", parent=self.root)
                    self.show()
                    con.close()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def delete(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please select product from list", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    option = messagebox.askyesno("Confirm", "Are you sure you want to delete this product?",
                                                 parent=self.root)
                    if option == 1:
                        cur.execute("DELETE FROM product WHERE pid=?", (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Product deleted successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")

        self.var_search_by.set("Select")
        self.var_search_txt.set("")

        self.show()

    def search(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_search_by.get() == "Select":
                messagebox.showerror("Error", "Select Search By option", parent=self.root)
            elif self.var_search_txt.get() == "":
                messagebox.showerror("Error", "Search input required", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE " + str(
                    self.var_search_by.get()) + " LIKE '%" + self.var_search_txt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')


# ======================================================================================================================
if __name__ == "__main__":
    root = Tk()
    obj = ProductClass(root)
    root.mainloop()
