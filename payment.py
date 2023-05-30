from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector

class Payment_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Adamson University")
        self.root.geometry("1285x563+260+233")

        #-------------- VARIABLE --------------
        self.var_student_number = StringVar()
        self.var_payment_method = StringVar()
        self.var_acc_name = StringVar()
        self.var_acc_number = StringVar()
        self.var_payment_amount = StringVar()

        #-------------- TITLE --------------
        lbl_title = Label(self.root, text="ONLINE PAYMENT", font = ("Arial", 18, "bold"), bg = "sky blue", fg = "navy blue", bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

        #-------------- LABEL FRAME --------------
        label_frame_up = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Assessment of Fees", font = ("Arial", 12, "bold"), padx =1 )
        label_frame_up.place(x = 5, y = 50, width  = 440, height = 240)

        #tuition fee lec
        label_tuition_fee = Label(label_frame_up, text = "Tuition Fee Lecture", font = ("Arial", 12), padx = 2, pady = 4)
        label_tuition_fee.grid (row = 0, column = 0, sticky = W)

        tuition_fee = Label(label_frame_up, text = "30,000 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        tuition_fee.grid (row = 0, column = 1, sticky = W)

        #tuition fee lab
        label_tuition_lab = Label(label_frame_up, text = "Tuition Fee Laboratory", font = ("Arial", 12), padx = 2, pady = 4)
        label_tuition_lab.grid (row = 1, column = 0, sticky = W)

        tuition_lab = Label(label_frame_up, text = "10,500 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        tuition_lab.grid (row = 1, column = 1, sticky = W)

        #lab fee
        label_lab_fee = Label(label_frame_up, text = "Laboratory Usage Fee", font = ("Arial", 12), padx = 2, pady = 4)
        label_lab_fee.grid (row = 2, column = 0, sticky = W)

        lab_fee = Label(label_frame_up, text = "10,000 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        lab_fee.grid (row = 2, column = 1, sticky = W)

        #development
        label_dev = Label(label_frame_up, text = "Development Fee", font = ("Arial", 12), padx = 2, pady = 4)
        label_dev.grid (row = 3, column = 0, sticky = W)

        dev = Label(label_frame_up, text = "  1,000 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        dev.grid (row = 3, column = 1, sticky = W)

        #ausg
        label_ausg = Label(label_frame_up, text = "AUSG", font = ("Arial", 12), padx = 2, pady = 4)
        label_ausg.grid (row = 4, column = 0, sticky = W)

        ausg = Label(label_frame_up, text = "     500 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        ausg.grid (row = 4, column = 1, sticky = W)

        #energy
        label_energy = Label(label_frame_up, text = "Energy Cost (Aircon)", font = ("Arial", 12), padx = 2, pady = 4)
        label_energy.grid (row = 5, column = 0, sticky = W)

        energy = Label(label_frame_up, text = "  2,280 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        energy.grid (row = 5, column = 1, sticky = W)

        #total
        label_total = Label(label_frame_up, text = "TOTAL", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        label_total.grid (row = 6, column = 0, sticky = W)

        total = Label(label_frame_up, text = "54,280 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        total.grid (row = 6, column = 1, sticky = W)

        
        #-------------- LABEL FRAME --------------
        label_frame_left = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Payment Information", font = ("Arial", 12, "bold"), padx =2 )
        label_frame_left.place(x = 5, y = 300, width  = 440, height = 250)

        #-------------- LABEL AND ENTRY --------------
        #reference number
        label_student_number = Label(label_frame_left, text = "Student Number", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_student_number.grid (row = 0, column = 0, sticky = W)

        student_number = ttk.Entry(label_frame_left, textvariable = self.var_student_number, font = ("Arial", 13, "bold"), width = 29)
        student_number.grid(row = 0, column = 1)
        
        #payment method
        label_method = Label(label_frame_left, text = "Payment Method", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_method.grid (row = 1, column = 0, sticky = W)

        combo_method = ttk.Combobox(label_frame_left, textvariable = self.var_payment_method, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_method["value"]= ("Gcash", "PayMaya", "Banco de Oro", "Philippine National Bank (PNB)", "Bank of the Philippine Islands (BPI)", "Union Bank of the Philippines", "Metrobank", "Security Bank")
        combo_method.current(0)
        combo_method.grid(row = 1, column = 1)

        #acc name
        label_acc_name = Label(label_frame_left, text = "Account Name", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_acc_name.grid (row = 2, column = 0, sticky = W)

        acc_name = ttk.Entry(label_frame_left, textvariable = self.var_acc_name, font = ("Arial", 13, "bold"), width = 29)
        acc_name.grid(row = 2, column = 1)

        #acc number
        label_acc_num = Label(label_frame_left, text = "Account Number", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_acc_num.grid (row = 3, column = 0, sticky = W)

        acc_num = ttk.Entry(label_frame_left, textvariable = self.var_acc_number, font = ("Arial", 13, "bold"), width = 29)
        acc_num.grid(row = 3, column = 1)

        #payment amount 
        label_amount = Label(label_frame_left, text = "Payment Amount", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_amount.grid (row = 4, column = 0, sticky = W)

        amount = ttk.Entry(label_frame_left, textvariable = self.var_payment_amount, font = ("Arial", 13, "bold"), width = 29)
        amount.grid(row = 4, column = 1)


        #-------------- BUTTON FRAME --------------
        btn_frame = Label(label_frame_left, bd = 2, relief = RIDGE)
        btn_frame.place (x = 10, y = 185, width = 411, height = 36)

        btn_add = Button(btn_frame, command = self.add_data, text = "Pay", font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_add.grid(row = 0, column = 0, padx = 1)

        btn_update = Button(btn_frame, command = self.update, text = "Update", font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_update.grid(row = 0, column = 1, padx = 1)

        btn_delete = Button(btn_frame, command = self.mDelete, text = "Delete", font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_delete.grid(row = 0, column = 2, padx = 1)

        btn_reset = Button(btn_frame, command = self.reset, text = "Reset", font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_reset.grid(row = 0, column = 3, padx = 1)

        #-------------- TABLE FRAME --------------
        table_frame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details and Search System", font = ("Arial", 12, "bold"), padx =2 )
        table_frame.place(x = 450, y = 50, width  = 830, height = 500)

        label_search = Label(table_frame, font = ("Arial", 12, "bold"), text = "Search By:", bg = "sky blue", fg = "white")
        label_search.grid(row = 0, column = 0, sticky = W, padx = 2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable = self.search_var, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_search["value"]= ("StudentNumber", "PaymentMethod", "AccountName", "AccountNumber", "PaymentAmount")
        combo_search.current(0)
        combo_search.grid(row = 0, column = 1, padx = 2)

        self.txt_search = StringVar()
        search = ttk.Entry(table_frame, textvariable = self.txt_search, font = ("Arial", 13, "bold"), width = 24)
        search.grid(row = 0, column = 2, padx = 2)
        
        btn_search = Button(table_frame, text = "Search", command = self.search, font = ("Arial", 11, "bold"), bg = "white", fg = "navy blue", width = 10)
        btn_search.grid(row = 0, column = 3, padx = 1)

        btn_showall = Button(table_frame, text = "Show All", command = self.fetch_payment, font = ("Arial", 11, "bold"), bg = "white", fg = "navy blue", width = 10)
        btn_showall.grid(row = 0, column = 4, padx = 1)

        #-------------- DATA TABLE --------------
        details_table = Label(table_frame, bd = 2, relief = RIDGE)
        details_table.place (x = 0, y = 50, width = 820, height = 350)

        scroll_x = ttk.Scrollbar(details_table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient = VERTICAL)

        self.Payment_Details_Table = ttk.Treeview(details_table, column =("student_number", "payment_method", "acc_name", "acc_num", "payment_amount"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Payment_Details_Table.xview)
        scroll_y.config(command = self.Payment_Details_Table.yview)

        #-------------- CONTENTS OF DATA TABLE --------------
        self.Payment_Details_Table.heading("student_number", text = "Student Number")
        self.Payment_Details_Table.heading("payment_method", text = "Payment Method")
        self.Payment_Details_Table.heading("acc_name", text = "Account Name")
        self.Payment_Details_Table.heading("acc_num", text = "Account Number")
        self.Payment_Details_Table.heading("payment_amount", text = "Payment Amount")

        self.Payment_Details_Table["show"] = "headings"

        self.Payment_Details_Table.column("student_number", width = 100)
        self.Payment_Details_Table.column("payment_method", width = 100)
        self.Payment_Details_Table.column("acc_name", width = 100)
        self.Payment_Details_Table.column("acc_num", width = 100)
        self.Payment_Details_Table.column("payment_amount", width = 100)

        
        self.Payment_Details_Table.pack(fill = BOTH, expand = 1)
        self.Payment_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_payment()
    
    def add_data(self):
        if self.var_student_number.get() == "" or self.var_payment_method.get() == "" or self.var_acc_name.get() == "" or self.var_acc_number.get() == "" or self.var_payment_amount.get() == "":
            messagebox.showerror("Error", "All boxes must be answered", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "Jere6125-", database = "emp_2")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into payment values(%s,%s,%s,%s,%s)", (
                            self.var_student_number.get(),
                            self.var_payment_method.get(),
                            self.var_acc_name.get(),
                            self.var_acc_number.get(),
                            self.var_payment_amount.get(),
                            
                        ))
                
                conn.commit()
                self.fetch_payment()
                conn.close()
                messagebox.showinfo("Success", "Payment Information has been added.", parent = self.root)

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent = self.root)

    def fetch_payment(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "Jere6125-", database = "emp_2")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from payment")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Payment_Details_Table.delete(*self.Payment_Details_Table.get_children())
            for i in rows:
                self.Payment_Details_Table.insert("", END, values = i)
            conn.commit()
        conn.close()

    def get_cursor(self, event = ""):
        cursor_row = self.Payment_Details_Table.focus()
        content = self.Payment_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_student_number.set(row[0]),
        self.var_payment_method.set(row[1]),
        self.var_acc_name.set(row[2]),
        self.var_acc_number.set(row[3]),
        self.var_payment_amount.set(row[4]),
        
    def update(self):
        if self.var_payment_amount.get() == "":
            messagebox.showerror("Error", "Please Enter Payment Amount", parent = self.root)

        elif self.var_acc_number.get() == "":
            messagebox.showerror("Error", "Please Enter Account Number", parent = self.root)

        else:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "Jere6125-", database = "emp_2")
            my_cursor = conn.cursor()
            my_cursor.execute("update payment set PaymentMethod =%s, AccountName =%s, AccountNumber =%s, PaymentAmount = %s", (
                            self.var_payment_method.get(),
                            self.var_acc_name.get(),
                            self.var_acc_number.get(),
                            self.var_payment_amount.get(),
                        ))
            conn.commit()
            self.fetch_payment()
            conn.close()
            messagebox.showinfo("Update", "Payment details has been updated successfully.", parent = self.root)
    
    def mDelete(self):
        mDelete = messagebox.askyesno("Online Enrollment", "Do you want to delete the information for this payment?", parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "Jere6125-", database = "emp_2")
            my_cursor = conn.cursor()
            query = "delete from payment where StudentNumber=%s"
            value = (self.var_student_number.get(),)
            my_cursor.execute(query, value)

        else:
            if not mDelete:
                return
            
        conn.commit()
        self.fetch_payment()
        conn.close()

    def reset(self):
        self.var_student_number.set(""),
        #self.var_payment_method.set(""),
        self.var_acc_name.set(""),
        self.var_acc_number.set(""),
        self.var_payment_amount.set("")

    def search(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "Jere6125-", database = "emp_2")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from payment where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Payment_Details_Table.delete(*self.Payment_Details_Table.get_children())
            for i in rows:
                self.Payment_Details_Table.insert("", END, values = i)
            conn.commit()
        conn.close()



if __name__ == "__main__":
    root = Tk()
    obj = Payment_Win(root)
    root.mainloop()