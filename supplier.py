from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


# IMS = Inventory Management System
class SupplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x550+227+130")
        self.root.title("Supplier Dashboard")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False, False)

        # All Variables
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        # =============================================search frame=====================================================
        lbl_search = Label(self.root, text="Search By Invoice No.", bg="white", font=("goudy old style", 15, "bold"))
        lbl_search.place(x=670, y=90)

        txt_search = Entry(self.root, textvariable=self.var_search_txt, font=("goudy old style", 15), bg="lightyellow")
        txt_search.place(x=855, y=90, width=80, height=30)

        # search button
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15),
                            bg="#4caf50", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=950, y=90, width=130, height=30)

        # =============================================title============================================================
        title = Label(self.root, text="Supplier Details", bg="#0f4d7d",
                      fg="white", font=("times new roman", 20, "bold"))
        title.place(x=50, y=10, width=1000, height=40)

        # content
        # ==============================================row1============================================================
        lbl_supplier_invoice = Label(self.root, text="Invoice No.", bg="white",
                                     font=("times new roman", 15))
        lbl_supplier_invoice.place(x=50, y=80)

        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, bg="lightyellow",
                                     font=("times new roman", 15), width=20)
        txt_supplier_invoice.place(x=147, y=80)

        # ===================================row2=======================================================================
        lbl_name = Label(self.root, text="Name", bg="white",
                         font=("times new roman", 15))
        lbl_name.place(x=50, y=120)

        txt_name = Entry(self.root, textvariable=self.var_name, bg="lightyellow",
                         font=("times new roman", 15), width=20)
        txt_name.place(x=147, y=120)

        # ===================================row3=======================================================================
        lbl_contact = Label(self.root, text="Contact", bg="white",
                            font=("times new roman", 15))
        lbl_contact.place(x=50, y=160)

        txt_contact = Entry(self.root, textvariable=self.var_contact, bg="lightyellow",
                            font=("times new roman", 15), width=20)
        txt_contact.place(x=147, y=160)

        # =========================row4=================================================================================
        lbl_desc = Label(self.root, text="Description", bg="white",
                         font=("times new roman", 15))
        lbl_desc.place(x=50, y=200)

        self.txt_desc = Text(self.root, bg="lightyellow",
                             font=("times new roman", 15), width=50, height=7)
        self.txt_desc.place(x=147, y=200)

        # =================buttons======================================================================================
        btn_add = Button(self.root, text="Save", font=("goudy old style", 15),
                         bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        btn_add.place(x=147, y=380, width=100, height=35)

        btn_update = Button(self.root, text="Update", font=("goudy old style", 15),
                            bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        btn_update.place(x=280, y=380, width=100, height=35)

        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15),
                            bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        btn_delete.place(x=415, y=380, width=100, height=35)

        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15),
                           bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=550, y=380, width=100, height=35)

        # ==============Supplier Details================================================================================
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=670, y=120, width=410, height=350)

        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)

        self.SupplierTable = ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "desc"),
                                          xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice", text="Invoice")
        self.SupplierTable.heading("name", text="Name")
        self.SupplierTable.heading("contact", text="Contact")
        self.SupplierTable.heading("desc", text="Description")

        self.SupplierTable["show"] = "headings"

        self.SupplierTable.column("invoice", width=90)
        self.SupplierTable.column("name", width=140)
        self.SupplierTable.column("contact", width=120)
        self.SupplierTable.column("desc", width=100)

        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease - 1>", self.get_data)

        self.show()

    # ===================================================functions======================================================
    def add(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice is required", parent=self.root)

            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Invoice No. is already assigned", parent=self.root)
                else:
                    cur.execute("INSERT INTO supplier (invoice, name, contact, desc) "
                                "VALUES (?, ?, ?, ?)",
                                (self.var_sup_invoice.get(), self.var_name.get(),
                                 self.var_contact.get(), self.txt_desc.get('1.0', END)))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def show(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM supplier")
            rows = cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def get_data(self, ev):
        f = self.SupplierTable.focus()
        content = self.SupplierTable.item(f)
        row = content['values']

        # print row
        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.txt_desc.delete('1.0', END),
        self.txt_desc.insert(END, row[3]),

    def update(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. is required", parent=root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    cur.execute("UPDATE supplier set name=?, contact=?, desc=? WHERE (invoice=?)",
                                (self.var_name.get(), self.var_contact.get(),
                                 self.txt_desc.get('1.0', END), self.var_sup_invoice.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                    self.show()
                    con.close()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def delete(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice is required", parent=root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid invoice", parent=self.root)
                else:
                    option = messagebox.askyesno("Confirm", "Are you sure you want to delete this supplier?",
                                                 parent=self.root)
                    if option == 1:
                        cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier deleted successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def clear(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.txt_desc.delete('0.0', END),
        self.var_search_txt.set("")

        self.show()

    def search(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_search_txt.get() == "":
                messagebox.showerror("Error", "Invoice No. required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_search_txt.get(),))
                row = cur.fetchone()
                if row != 0:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')


if __name__ == "__main__":
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()
