from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


# IMS = Inventory Management System
class CategoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("690x520+227+130")
        self.root.title("Category Dashboard")
        self.root.config(bg="white")
        self.root.focus_force()

# =======================================All Variables==================================================================
        self.var_cat_id = StringVar()
        self.var_cat_name = StringVar()

# ===========================================title======================================================================
        lbl_title = Label(self.root, text="Manage Product Category", bd=3, relief=RIDGE,
                          font=("goudy old style", 30, "bold"), bg="#184a45", fg="white")
        lbl_title.pack(side=TOP, fill=X)

        lbl_name = Label(self.root, text="Enter Category Name",
                         font=("goudy old style", 30, "bold"), bg="white")
        lbl_name.place(x=50, y=80)

        txt_name = Entry(self.root, textvariable=self.var_cat_name,
                         font=("goudy old style", 18, "bold"), bg="lightyellow")
        txt_name.place(x=50, y=150, width=300, height=30)

# =======================================buttons========================================================================
        btn_add = Button(self.root, text="ADD", fg="white", cursor="hand2", command=self.add,
                         font=("goudy old style", 18, "bold"), bg="#4caf50")
        btn_add.place(x=50, y=190, height=30, width=150)

        btn_delete = Button(self.root, text="DELETE", fg="white", cursor="hand2", command=self.delete,
                            font=("goudy old style", 18, "bold"), bg="red")
        btn_delete.place(x=230, y=190, height=30, width=150)

        btn_clear = Button(self.root, text="CLEAR", fg="white", cursor="hand2", command=self.clear,
                            font=("goudy old style", 18, "bold"), bg="#607d8b")
        btn_clear.place(x=410, y=190, height=30, width=150)

# ====================================Category Details==================================================================
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=0, y=270, width=690, height=250)

        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(cat_frame, orient=VERTICAL)

        self.CategoryTable = ttk.Treeview(cat_frame, columns=("cid", "name"),
                                          xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("cid", text="Category ID")
        self.CategoryTable.heading("name", text="Name")

        self.CategoryTable["show"] = "headings"

        self.CategoryTable.column("cid", width=90)
        self.CategoryTable.column("name", width=140)

        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease - 1>", self.get_data)

        self.show()

# ======================================functions=======================================================================
    def add(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_cat_name.get() == "":
                messagebox.showerror("Error", "Category name is required", parent=self.root)

            else:
                cur.execute("SELECT * FROM category WHERE name=?", (self.var_cat_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This category name is already assigned", parent=self.root)
                else:
                    cur.execute("INSERT INTO category (name) "
                                "VALUES (?)", (self.var_cat_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category added successfully", parent=self.root)
                    self.show()
                    self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def show(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category")
            rows = cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def get_data(self, ev):
        f = self.CategoryTable.focus()
        content = self.CategoryTable.item(f)
        row = content['values']

        # print row
        self.var_cat_id.set(row[0]),
        self.var_cat_name.set(row[1]),

    def delete(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_cat_name.get() == "":
                messagebox.showerror("Error", "Please select category", parent=root)
            else:
                cur.execute("SELECT * FROM category WHERE name=?", (self.var_cat_name.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Category does not exist", parent=self.root)
                else:
                    option = messagebox.askyesno("Confirm", "Are you sure you want to delete this category?",
                                                 parent=self.root)
                    if option == 1:
                        cur.execute("DELETE FROM category WHERE cat_id=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category deleted successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def clear(self):
        self.var_cat_id.set("")
        self.var_cat_name.set(""),

        self.show()

# ======================================================================================================================
if __name__ == "__main__":
    root = Tk()
    obj = CategoryClass(root)
    root.resizable(False, False)
    root.mainloop()
