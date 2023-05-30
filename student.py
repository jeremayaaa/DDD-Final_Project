from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import random
import mysql.connector
from print import Print_Win


class Student_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Adamson University")
        self.root.geometry("1285x563+260+233")

        #-------------- VARIABLE --------------
        self.var_student_number = StringVar()
        x = random.randint(202300001, 202300999)
        self.var_student_number.set(str(x))

        self.var_first_name = StringVar()
        self.var_middle_name = StringVar()
        self.var_last_name = StringVar()
        self.var_gender = StringVar()
        self.var_citizenship = StringVar()
        self.var_mobile_number = StringVar()
        self.var_region = StringVar()
        self.var_province = StringVar()
        self.var_email_address = StringVar()
        self.var_birth_month = StringVar()
        self.var_birth_day = StringVar()
        self.var_birth_year = StringVar()
        self.var_course = StringVar()
        

        #-------------- TITLE --------------
        lbl_title = Label(self.root, text="ONLINE ENROLLMENT", font = ("Arial", 18, "bold"), bg = "sky blue", fg = "navy blue", bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

        #-------------- LABEL FRAME --------------
        label_frame_left = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Student Information", font = ("Arial", 12, "bold"), padx =2 )
        label_frame_left.place(x = 5, y = 50, width  = 440, height = 500)

        #-------------- LABEL AND ENTRY --------------
        self.var_id = 0
        
        #student number
        label_fname = Label(label_frame_left, text = "Student Number", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_fname.grid (row = 0, column = 0, sticky = W)

        fname = ttk.Entry(label_frame_left, textvariable = self.var_student_number, font = ("Arial", 13, "bold"), width = 29, state = "readonly")
        fname.grid(row = 0, column = 1)

        #fname
        label_fname = Label(label_frame_left, text = "First Name", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_fname.grid (row = 1, column = 0, sticky = W)

        fname = ttk.Entry(label_frame_left, textvariable = self.var_first_name, font = ("Arial", 13, "bold"), width = 29)
        fname.grid(row = 1, column = 1)

        #mname
        label_mname = Label(label_frame_left, text = "Middle Name", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_mname.grid (row = 2, column = 0, sticky = W)

        mname = ttk.Entry(label_frame_left, textvariable = self.var_middle_name, font = ("Arial", 13, "bold"), width = 29)
        mname.grid(row = 2, column = 1)

        #lname
        label_lname = Label(label_frame_left, text = "Last Name", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_lname.grid (row = 3, column = 0, sticky = W)

        lname = ttk.Entry(label_frame_left, textvariable = self.var_last_name, font = ("Arial", 13, "bold"), width = 29)
        lname.grid(row = 3, column = 1)

        #gender
        label_gender = Label(label_frame_left, text = "Gender", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_gender.grid (row = 4, column = 0, sticky = W)

        combo_gender = ttk.Combobox(label_frame_left, textvariable = self.var_gender, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_gender["value"]= ("Male", "Female", "Rather Not Say")
        combo_gender.current(0)
        combo_gender.grid(row = 4, column = 1)

        #Citizenship
        label_citizenship = Label(label_frame_left, text = "Citizenship", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_citizenship.grid (row = 5, column = 0, sticky = W)

        combo_citizenship = ttk.Combobox(label_frame_left, textvariable = self.var_citizenship, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_citizenship["value"]= ("American", "Chinese", "Egyptian", "Filipino", "French", "Indian", "Japanese")
        combo_citizenship.current(0)
        combo_citizenship.grid(row = 5, column = 1)

        #Mobile Number
        label_mobile = Label(label_frame_left, text = "Mobile Number", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_mobile.grid (row = 6, column = 0, sticky = W)

        mobile = ttk.Entry(label_frame_left, textvariable = self.var_mobile_number, font = ("Arial", 13, "bold"), width = 29)
        mobile.grid(row = 6, column = 1)

        #Region
        label_region = Label(label_frame_left, text = "Region", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_region.grid (row = 7, column = 0, sticky = W)

        combo_region = ttk.Combobox(label_frame_left, textvariable = self.var_region, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_region["value"]= ("ARMM", "CAR", "NCR", "Region I", "Region II","Region III","Region IV-A","Region IV-B","Region V","Region VI","Region VII","Region VIII","Region IV","Region X","Region XI","Region XII", "Region XIII")
        combo_region.current(0)
        combo_region.grid(row = 7, column = 1)

        #Province
        label_province = Label(label_frame_left, text = "Province (if NCR)", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_province.grid (row = 8, column = 0, sticky = W)

        combo_province = ttk.Combobox(label_frame_left, textvariable = self.var_province, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_province["value"]= ("First District (City of Manila)", "Second District", "Third District", "Fourth District")
        combo_province.current(0)
        combo_province.grid(row = 8, column = 1)

        #Email
        label_email = Label(label_frame_left, text = "Email Address", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_email.grid (row = 9, column = 0, sticky = W)

        email = ttk.Entry(label_frame_left, textvariable = self.var_email_address, font = ("Arial", 13, "bold"), width = 29)
        email.grid(row = 9, column = 1)
 
        #Bday
        label_bday = Label(label_frame_left, text = "Date of Birth", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_bday.grid (row = 10, column = 0, sticky = W)

        lbl_bday = Label(label_frame_left, bd = 0, relief = RIDGE)
        lbl_bday.grid(row = 10, column = 1, sticky = W)

        combo_month = ttk.Combobox(lbl_bday, textvariable = self.var_birth_month, font = ("Arial", 12, "bold"), width = 10, state = "readonly")
        combo_month["value"]= ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        combo_month.current(0)
        combo_month.grid(row = 0, column = 0, padx = 1)

        combo_day = ttk.Combobox(lbl_bday, textvariable = self.var_birth_day, font = ("Arial", 12, "bold"), width = 4, state = "readonly")
        combo_day["value"]= ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        combo_day.current(0)
        combo_day.grid(row = 0, column = 1, padx = 1)

        combo_year = ttk.Combobox(lbl_bday, textvariable = self.var_birth_year, font = ("Arial", 12, "bold"), width = 7, state = "readonly")
        combo_year["value"]= ("2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003","2002", "2001", "2000", "1999","1998", "1997", "1996", "1995", "1994", "1993", "1992", "1991", "1990")
        combo_year.current(0)
        combo_year.grid(row = 0, column = 2, padx = 1)

        #Course
        label_course = Label(label_frame_left, text = "Course", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_course.grid (row = 11, column = 0, sticky = W)

        combo_course = ttk.Combobox(label_frame_left, textvariable = self.var_course, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_course["value"] = ("BS Architecture", "BS Accountancy", "BS Major in Financial Management", "BSBA Major in Marketing Management", "BSBA Major in Operations Management", "BS Customs Administration", "BS Hospitality Management", "BS Chemical Engineering", "BS Civil Engineering", "BS Computer Engineering", "BS Electrical Engineering", "BS Electronics Engineering", "BS Industrial Engineering", "BS Mechanical Engineering", "BS Mining Engineering", "BS Geology", "BS Petroleum Engineering", "BS Nursing", "BS Pharmacy", "BS Juris Doctor");
        combo_course.current(0)
        combo_course.grid(row = 11, column = 1)

        

        #-------------- BUTTON FRAME --------------
        btn_frame = Label(label_frame_left, bd = 2, relief = RIDGE)
        btn_frame.place (x = 10, y = 428, width = 411, height = 36)

        btn_add = Button(btn_frame, text = "Add", command = self.add_data, font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_add.grid(row = 0, column = 0, padx = 1)

        btn_update = Button(btn_frame, text = "Update", command = self.update, font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_update.grid(row = 0, column = 1, padx = 1)

        btn_delete = Button(btn_frame, text = "Delete", command = self.mDelete, font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_delete.grid(row = 0, column = 2, padx = 1)

        btn_reset = Button(btn_frame, text = "Reset", command = self.reset, font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_reset.grid(row = 0, column = 3, padx = 1)

        #-------------- TABLE FRAME --------------
        table_frame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details and Search System", font = ("Arial", 12, "bold"), padx =2 )
        table_frame.place(x = 450, y = 50, width  = 830, height = 428)

        label_search = Label(table_frame, font = ("Arial", 12, "bold"), text = "Search By:", bg = "sky blue", fg = "white")
        label_search.grid(row = 0, column = 0, sticky = W, padx = 2)

        #btn_print = Button(table_frame, text = "Print", command = self.print_details, font = ("Arial", 11, "bold"), bg = "sky blue", fg = "navy blue", width = 10)
        #btn_print.grid(row = 0, column = 0, sticky = W, padx = 2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable = self.search_var, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_search["value"]= ("StudentNumber", "LastName", "MobileNumber")
        combo_search.current(0)
        combo_search.grid(row = 0, column = 1, padx = 2)

        self.txt_search = StringVar()
        search = ttk.Entry(table_frame, textvariable = self.txt_search, font = ("Arial", 13, "bold"), width = 24)
        search.grid(row = 0, column = 2, padx = 2)
        
        btn_search = Button(table_frame, text = "Search", command = self.search, font = ("Arial", 11, "bold"), bg = "white", fg = "navy blue", width = 10)
        btn_search.grid(row = 0, column = 3, padx = 1)

        btn_showall = Button(table_frame, text = "Show All", command = self.fetch_data, font = ("Arial", 11, "bold"), bg = "white", fg = "navy blue", width = 10)
        btn_showall.grid(row = 0, column = 4, padx = 1)

        #-------------- PRINT --------------
        #table_print = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Print Student Enrollment Info", font = ("Arial", 12, "bold"), padx =2 )
        #table_print.place(x = 450, y = 480, width  = 830, height = 100)
        
        #btn_print = Button(table_frame, text = "Print", command = self.print_details, font = ("Arial", 11, "bold"), bg = "white", fg = "navy blue", width = 10)
        #btn_print.place(x=100, y=800, width = 255, height = 153)

        

        #-------------- DATA TABLE --------------
        details_table = Label(table_frame, bd = 2, relief = RIDGE)
        details_table.place (x = 0, y = 50, width = 820, height = 350)

        scroll_x = ttk.Scrollbar(details_table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient = VERTICAL)

        self.Student_Details_Table = ttk.Treeview(details_table, column =("student_number", "first_name", "middle_name", "last_name", "gender", "citizenship", "mobile_number", "region", "province", "email_address",  "birth_month", "birth_day", "birth_year", 'course'), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Student_Details_Table.xview)
        scroll_y.config(command = self.Student_Details_Table.yview)

        #-------------- CONTENTS OF DATA TABLE --------------
        #self.Student_Details_Table.heading("id", text = "ID")
        self.Student_Details_Table.heading("student_number", text = "Student Number")
        self.Student_Details_Table.heading("first_name", text = "First Name")
        self.Student_Details_Table.heading("middle_name", text = "Middle Name")
        self.Student_Details_Table.heading("last_name", text = "Last Name")
        self.Student_Details_Table.heading("gender", text = "Gender")
        self.Student_Details_Table.heading("citizenship", text = "Citizenship")
        self.Student_Details_Table.heading("mobile_number", text = "Mobile Number")
        self.Student_Details_Table.heading("region", text = "Region")
        self.Student_Details_Table.heading("province", text = "Province (if NCR)")
        self.Student_Details_Table.heading("email_address", text = "Email Address")
        self.Student_Details_Table.heading("birth_month", text = "Birth Month")
        self.Student_Details_Table.heading("birth_day", text = "Birth Day")
        self.Student_Details_Table.heading("birth_year", text = "Birth Year")
        self.Student_Details_Table.heading("course", text = "Course")

        self.Student_Details_Table["show"] = "headings"

        #self.Student_Details_Table.column("ID", width = 100)
        self.Student_Details_Table.column("student_number", width = 100)
        self.Student_Details_Table.column("first_name", width = 100)
        self.Student_Details_Table.column("middle_name", width = 100)
        self.Student_Details_Table.column("last_name", width = 100)
        self.Student_Details_Table.column("gender", width = 100)
        self.Student_Details_Table.column("citizenship", width = 100)
        self.Student_Details_Table.column("mobile_number", width = 100)
        self.Student_Details_Table.column("region", width = 100)
        self.Student_Details_Table.column("province", width = 100)
        self.Student_Details_Table.column("email_address", width = 100)
        self.Student_Details_Table.column("birth_month", width = 100)
        self.Student_Details_Table.column("birth_day", width = 100)
        self.Student_Details_Table.column("birth_year", width = 100)
        self.Student_Details_Table.column("course", width = 100)

        self.Student_Details_Table.pack(fill = BOTH, expand = 1)
        self.Student_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_student_number.get() == "" or self.var_first_name.get() == "" or self.var_last_name.get() == "" or self.var_gender.get() == "" or self.var_citizenship.get() == "" or self.var_mobile_number.get() == "" or self.var_region.get() == "" or self.var_email_address.get() == "" or self.var_birth_month.get() == "" or self.var_birth_day.get() == "" or self.var_birth_year.get() == "" or  self.var_course.get() == "":
            messagebox.showerror("Error", "All boxes must be answered", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "Jere6125-", database = "emp_2")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                            #self.var_id.get(),
                            self.var_student_number.get(),
                            self.var_first_name.get(),
                            self.var_middle_name.get(),
                            self.var_last_name.get(),
                            self.var_gender.get(),
                            self.var_citizenship.get(),
                            self.var_mobile_number.get(),
                            self.var_region.get(),
                            self.var_province.get(),
                            self.var_email_address.get(),
                            self.var_birth_month.get(),
                            self.var_birth_day.get(),
                            self.var_birth_year.get(),
                            self.var_course.get()
                        ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Information has been added.", parent = self.root)

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent = self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "Jere6125-", database = "emp_2")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Student_Details_Table.delete(*self.Student_Details_Table.get_children())
            for i in rows:
                self.Student_Details_Table.insert("", END, values = i)
            conn.commit()
        conn.close()

    def get_cursor(self, event = ""):
        cursor_row = self.Student_Details_Table.focus()
        content = self.Student_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_student_number.set(row[0]),
        self.var_first_name.set(row[1]),
        self.var_middle_name.set(row[2]),
        self.var_last_name.set(row[3]),
        self.var_gender.set(row[4]),
        self.var_citizenship.set(row[5]),
        self.var_mobile_number.set(row[6]),
        self.var_region.set(row[7]),
        self.var_province.set(row[8]),
        self.var_email_address.set(row[9]),
        self.var_birth_month.set(row[10]),
        self.var_birth_day.set(row[11]),
        self.var_birth_year.set(row[12]),
        self.var_course.set(row[13])

    def update(self):
        if self.var_mobile_number.get() == "":
            messagebox.showerror("Error", "Please Enter Mobile Number", parent = self.root)

        else:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "Jere6125-", database = "emp_2")
            my_cursor = conn.cursor()
            my_cursor.execute("update student set FirstName =%s, MiddleName =%s, LastName =%s, Gender = %s, Citizenship = %s, MobileNumber = %s, Region = %s, Province = %s, EmailAddress = %s, BirthMonth = %s, BirthDay = %s, BirthYear = %s, Course = %s", (
                            self.var_first_name.get(),
                            self.var_middle_name.get(),
                            self.var_last_name.get(),
                            self.var_gender.get(),
                            self.var_citizenship.get(),
                            self.var_mobile_number.get(),
                            self.var_region.get(),
                            self.var_province.get(),
                            self.var_email_address.get(),
                            self.var_birth_month.get(),
                            self.var_birth_day.get(),
                            self.var_birth_year.get(),
                            self.var_course.get()
                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Student information has been updated successfully.", parent = self.root)
    
    def mDelete(self):
        mDelete = messagebox.askyesno("Online Enrollment", "Do you want to delete the information of this student?", parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "Jere6125-", database = "emp_2")
            my_cursor = conn.cursor()
            query = "delete from student where StudentNumber=%s"
            value = (self.var_student_number.get(),)
            my_cursor.execute(query, value)

        else:
            if not mDelete:
                return
            
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_student_number.set(""),
        self.var_first_name.set(""),
        self.var_middle_name.set(""),
        self.var_last_name.set(""),
        #self.var_gender.set(""),
        #self.var_citizenship.set(""),
        self.var_mobile_number.set(""),
        #self.var_region.set(""),
        #self.var_province.set(""),
        self.var_email_address.set(""),
        #self.var_birth_month.set(""),
        #self.var_birth_day.set(""),
        #self.var_birth_year.set(""),
        #self.var_course.set(""),

        x = random.randint(202300001, 202300999)
        self.var_student_number.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "Jere6125-", database = "emp_2")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from student where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Student_Details_Table.delete(*self.Student_Details_Table.get_children())
            for i in rows:
                self.Student_Details_Table.insert("", END, values = i)
            conn.commit()
        conn.close()

    def print_details(self):
        self.new_window = Toplevel(self.root)      
        self.app = Print_Win(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Student_Win(root)
    root.mainloop()