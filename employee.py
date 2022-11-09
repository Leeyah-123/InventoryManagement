import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


# IMS = Inventory Management System
class EmployeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x550+227+130")
        self.root.title("Employee Dashboard")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False, False)

        # All Variables
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        # search frame
        search_frame = LabelFrame(self.root, text="Search Employee", bg="white")
        search_frame.place(x=250, y=20, width=600, height=70)

        # options
        search = ttk.Combobox(search_frame, textvariable=self.var_search_by, values=("Select", "Email", "Name", "Contact"),
                              state="readonly", justify=CENTER, font=("goudy old style", 15))
        search.place(x=10, y=10, width=180)
        search.current(0)

        txt_search = Entry(search_frame,textvariable=self.var_search_txt, font=("goudy old style", 15), bg="lightyellow")
        txt_search.place(x=200, y=10)

        # search button
        btn_search = Button(search_frame, text="Search", font=("goudy old style", 15),
                            bg="#4caf50", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=410, y=10, width=150, height=26)

        # title
        title = Label(self.root, text="Employee Details", bg="#0f4d7d",
                      fg="white", font=("times new roman", 15))
        title.place(x=50, y=100, width=1000)

        # content
        # ==============================================row1============================================================
        lbl_emp_id = Label(self.root, text="Emp ID", bg="white",
                           font=("times new roman", 15))
        lbl_emp_id.place(x=50, y=150)

        lbl_gender = Label(self.root, text="Gender", bg="white",
                           font=("times new roman", 15))
        lbl_gender.place(x=350, y=150)

        lbl_contact = Label(self.root, text="Contact", bg="white",
                            font=("times new roman", 15))
        lbl_contact.place(x=750, y=150)

        txt_emp_id = Entry(self.root, textvariable=self.var_emp_id, bg="lightyellow",
                           font=("times new roman", 15), width=20)
        txt_emp_id.place(x=130, y=150)

        gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Female", "Male"),
                              state="readonly", justify=CENTER, font=("goudy old style", 13), width=30)
        gender.place(x=420, y=150)
        gender.current(0)

        txt_contact = Entry(self.root, textvariable=self.var_contact, bg="lightyellow",
                            font=("times new roman", 15), width=25)
        txt_contact.place(x=817, y=150)

        # ===================================row2=======================================================================
        lbl_name = Label(self.root, text="Name", bg="white",
                           font=("times new roman", 15))
        lbl_name.place(x=50, y=190)

        lbl_dob = Label(self.root, text="D.O.B", bg="white",
                           font=("times new roman", 15))
        lbl_dob.place(x=350, y=190)

        lbl_doj = Label(self.root, text="D.O.J", bg="white",
                            font=("times new roman", 15))
        lbl_doj.place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, bg="lightyellow",
                           font=("times new roman", 15), width=20)
        txt_name.place(x=130, y=190)

        txt_dob = Entry(self.root, textvariable=self.var_dob, bg="lightyellow",
                        font=("times new roman", 15), width=29)
        txt_dob.place(x=420, y=190)

        txt_doj = Entry(self.root, textvariable=self.var_doj, bg="lightyellow",
                            font=("times new roman", 15), width=25)
        txt_doj.place(x=817, y=190)

        # ===================================row3=======================================================================
        lbl_email = Label(self.root, text="Email", bg="white",
                           font=("times new roman", 15))
        lbl_email.place(x=50, y=230)

        lbl_password = Label(self.root, text="Password", bg="white",
                           font=("times new roman", 15))
        lbl_password.place(x=350, y=230)

        lbl_utype = Label(self.root, text="User-type", bg="white",
                            font=("times new roman", 15))
        lbl_utype.place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, bg="lightyellow",
                           font=("times new roman", 15), width=20)
        txt_email.place(x=130, y=230)

        txt_password = Entry(self.root, textvariable=self.var_pass, bg="lightyellow",
                        font=("times new roman", 15), width=27)
        txt_password.place(x=440, y=230)

        utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Employee", "Admin"),
                              state="readonly", justify=CENTER, font=("goudy old style", 13), width=24)
        utype.place(x=832, y=230)
        utype.current(0)

        # =========================row4=================================================================================
        lbl_address = Label(self.root, text="Address", bg="white",
                           font=("times new roman", 15))
        lbl_address.place(x=50, y=270)

        lbl_salary = Label(self.root, text="Salary", bg="white",
                           font=("times new roman", 15))
        lbl_salary.place(x=650, y=270)

        self.txt_address = Text(self.root, bg="lightyellow",
                           font=("times new roman", 15), width=50, height=4)
        self.txt_address.place(x=130, y=270)

        txt_salary = Entry(self.root,bg="lightyellow", textvariable=self.var_salary,
                        font=("times new roman", 15), width=36)
        txt_salary.place(x=709, y=270)

        # =================buttons======================================================================================
        btn_add = Button(self.root, text="Save", font=("goudy old style", 15),
                         bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        btn_add.place(x=641, y=310, width=100, height=26)

        btn_update = Button(self.root, text="Update", font=("goudy old style", 15),
                         bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        btn_update.place(x=760, y=310, width=100, height=26)

        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15),
                         bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        btn_delete.place(x=880, y=310, width=100, height=26)

        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15),
                         bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=1000, y=310, width=100, height=26)

        # ==============Employee Details================================================================================
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=370, relwidth=1, height=180)

        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender",
                                                              "contact", "dob", "doj", "pass",
                                                              "utype", "address", "salary"),
                                          xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)


        self.EmployeeTable.heading("eid", text="Emp Id")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=140)
        self.EmployeeTable.column("email", width=150)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=120)
        self.EmployeeTable.column("dob", width=105)
        self.EmployeeTable.column("doj", width=105)
        self.EmployeeTable.column("pass", width=120)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("address", width=130)
        self.EmployeeTable.column("salary", width=100)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease - 1>", self.get_data)

        self.show()

# ==============================================functions===============================================================
    def add(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
           if self.var_emp_id.get() == "":
               messagebox.showerror("Error", "Employee ID is required", parent=self.root)
           elif self.var_name.get() == "":
                   messagebox.showerror("Error", "Employee name is required", parent=self.root)
           elif self.var_email.get() == "":
               messagebox.showerror("Error", "Email is required", parent=self.root)
           elif self.var_gender.get() == "":
               messagebox.showerror("Error", "Gender is required", parent=self.root)
           elif self.var_contact.get() == "":
               messagebox.showerror("Error", "Contact is required", parent=self.root)
           else:
               cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
               row = cur.fetchone()
               if row != None:
                   messagebox.showerror("Error", "This Employee ID already exists", parent=self.root)
               else:
                   cur.execute("INSERT INTO employee (eid, name, email, gender, contact, dob, doj, "
                               "pass, utype, address, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               (self.var_emp_id.get(), self.var_name.get(),
                               self.var_email.get(), self.var_gender.get(),
                               self.var_contact.get(), self.var_dob.get(),
                               self.var_doj.get(), self.var_pass.get(),
                               self.var_utype.get(), self.txt_address.get('0.0', END),
                               self.var_salary.get()))
                   con.commit()
                   messagebox.showinfo("Success", "Employee added successfully", parent=self.root)
                   self.show()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')


    def show(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')


    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(f)
        row = content['values']

        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete('1.0', END),
        self.txt_address.insert(END, row[9]),
        self.var_salary.set(row[10])


    def update(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
           if self.var_emp_id.get() == "":
               messagebox.showerror("Error", "Employee ID is required", parent=self.root)
           else:
               cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
               row = cur.fetchone()
               if row == None:
                   messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
               else:
                   cur.execute("UPDATE employee set name=?, email=?, gender=?, contact=?, dob=?, doj=?, "
                               "pass=?, utype=?, address=?, salary=? WHERE (eid=?)",
                               (self.var_name.get(), self.var_email.get(),
                                self.var_gender.get(), self.var_contact.get(),
                                self.var_dob.get(), self.var_doj.get(),
                                self.var_pass.get(), self.var_utype.get(),
                                self.txt_address.get('1.0', END),
                               self.var_salary.get(), self.var_emp_id.get(),))
                   con.commit()
                   messagebox.showinfo("Success", "Employee updated successfully", parent=self.root)
                   self.show()
                   con.close()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')


    def delete(self):
        con = sqlite3.connect(database=r'IMS.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    option = messagebox.askyesno("Confirm", "Are you sure you want to delete this employee?", parent=self.root)
                    if option == 1:
                        cur.execute("DELETE FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee deleted successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')


    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Employee"),
        self.txt_address.delete('0.0', END),
        self.var_salary.set("")
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
                cur.execute("SELECT * FROM employee WHERE " + str(self.var_search_by.get()) + " LIKE '%" + self.var_search_txt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')


if __name__ == "__main__":
    root = Tk()
    obj = EmployeeClass(root)
    root.mainloop()
