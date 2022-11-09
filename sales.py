from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from billing import BillClass
import os


# IMS = Inventory Management System
class SalesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+227+130")
        self.root.title("Sales Dashboard")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False, False)

# ===================================All Variables======================================================================
        self.var_invoice = StringVar()
        self.bill_list = []

# =========================================title========================================================================
        title = Label(self.root, text="View Customer Bills", bg="#184a45",
                      fg="white", font=("times new roman", 30, "bold"), relief=RIDGE, bd=3)
        title.pack(side=TOP, fill=X, padx=10, pady=20)

# =======================================Entry==========================================================================
        lbl_invoice = Label(self.root, text="Invoice No.", font=("times new roman", 15),
                            bg="white")
        lbl_invoice.place(x=50, y=100)

        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15),
                            bg="lightyellow")
        txt_invoice.place(x=160, y=100, width=180, height=28)

        btn_search = Button(self.root, text="Search", font=("times new roman", 15, "bold"),
                            bg="#2196f3", fg="white", relief=RAISED, command=self.search)
        btn_search.place(x=360, y=100, width=120, height=28)

        btn_clear = Button(self.root, text="Clear", font=("times new roman", 15, "bold"),
                           bg="lightgreen", fg="white", relief=RAISED, command=self.clear)
        btn_clear.place(x=490, y=100, width=120, height=28)

        sales_frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_frame.place(x=50, y=140, width=200, height=330)

        scrolly = Scrollbar(sales_frame, orient=VERTICAL)
        self.SalesList = Listbox(sales_frame, font=("goudy old style", 15), bg="white",
                                 yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.SalesList.yview)
        self.SalesList.pack(fill=BOTH, expand=1)
        self.SalesList.bind("<ButtonRelease - 1>", self.get_data)

# ========================================Billing Area==================================================================
        bill_frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_frame.place(x=280, y=140, width=410, height=330)

        title2 = Label(bill_frame, text="Customer Bill Area", bg="orange",
                       font=("times new roman", 20, "bold"), relief=RIDGE, bd=3)
        title2.pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
        self.BillArea = Text(bill_frame, bg="lightyellow",
                             yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.BillArea.yview)
        self.BillArea.pack(fill=BOTH, expand=1)

# =============================Bill label============================================================================
        self.bill_btn = Button(self.root, text="Generate bill", font=("times new roman", 15, "bold"),
                               bg="red", fg="white", relief=RAISED, command=self.billing)
        self.bill_btn.place(x=620, y=100, width=120, height=28)

# ==================================Image===============================================================================
        self.bill_image = Image.open("Images/bill.jpg")
        self.bill_image = self.bill_image.resize((350, 300), Image.ANTIALIAS)
        self.bill_image = ImageTk.PhotoImage(self.bill_image)

        lbl_bill_image = Label(self.root, image=self.bill_image, bd=0)
        lbl_bill_image.place(x=730, y=130)
        self.show()

# ===============================functions==============================================================================
    def show(self):
        del self.bill_list[:]
        self.SalesList.delete('0', END)
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.SalesList.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):
        index_ = self.SalesList.curselection()
        file_name = self.SalesList.get(index_)
        # print(file_name)
        self.BillArea.delete('1.0', END)
        fp = open(f"bill/{file_name}", "r")
        for i in fp:
            self.BillArea.insert(END, i)
        fp.close()

    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice No. is required", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp = open(f"bill/{self.var_invoice.get()}.txt", "r")
                self.BillArea.delete('1.0', END)
                for i in fp:
                    self.BillArea.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)

    def clear(self):
        self.show()
        self.var_invoice.set("")
        self.BillArea.delete('1.0', END)

    def billing(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = BillClass(self.new_win)


if __name__ == "__main__":
    root = Tk()
    obj = SalesClass(root)
    root.mainloop()
