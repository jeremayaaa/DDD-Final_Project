from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Print_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Adamson University")
        self.root.geometry("1000x563+260+233")
        #root.configure(bg = 'sky blue')

        #-------------- IMAGE BG --------------
        #main_bg = Image.open(r"C:\Users\jere\DATABASE\adu.jpg")
        #main_bg = main_bg.resize((1288, 590), Image.ANTIALIAS)
        #main_bg.putalpha(160)
        #self.photomain_bg = ImageTk.PhotoImage(main_bg)

        #lblmain_bg = Label(self.root, image = self.photomain_bg, bd = 4, relief = RIDGE)
        #lblmain_bg.place(x = 0, y = 0, width = 1287, height = 563)

        #-------------- HEADER --------------
        #label_header = LabelFrame(self.root, bd = 2, relief = RIDGE)
        #label_header.place(x = 0, y = 0, width  = 1288, height = 200)   

        adulogo = Image.open(r"C:\Users\jere\DATABASE\adulogo.png")
        adulogo = adulogo.resize((280, 70), Image.ANTIALIAS)
        self.photo_adulogo = ImageTk.PhotoImage(adulogo)
    
        lbl_adulogo = Label(self.root, image = self.photo_adulogo, bd = 4, padx = 2, pady = 4, relief = RIDGE)
        lbl_adulogo.place(x = 7, y = 7, width = 290, height = 80)

        label_lname = Label(self.root, text = "OFFICE OF THE REGISTRAR", font = ("Arial", 12), fg = "dark blue")
        label_lname.place (x = 750, y = 30)

        #-------------- ENROLLMENT --------------
        label_title = Label(self.root, text = "STUDENT ENROLLMENT INFORMATION", font = ("Arial", 14, "bold"), fg = "dark blue")
        label_title.place (x = 326, y = 80)

        label_title = Label(self.root, text = "S.Y. 2023-2024", font = ("Arial", 10, "bold"), fg = "black")
        label_title.place (x = 460, y = 102)

        #-------------- NAME COURSE STUDENT NO. YEAR --------------
        label_name = Label(self.root, text = "Name             :", font = ("Arial", 12, "bold"), fg = "dark blue")
        label_name.place (x = 80, y = 120)

        #INSERT NAME 

        label_course = Label(self.root, text = "Course          :", font = ("Arial", 12, "bold"), fg = "dark blue")
        label_course.place (x = 80, y = 140)

        #INSERT COURSE

        label_name = Label(self.root, text = "Student No.         :", font = ("Arial", 12, "bold"), fg = "dark blue")
        label_name.place (x = 640, y = 120)

        #INSERT STUDENT NO.

        label_name = Label(self.root, text = "Acad. Year           :", font = ("Arial", 12, "bold"), fg = "dark blue")
        label_name.place (x = 640, y = 140)

        #INSERT ACAD YEAR

        #self.Student_Details_Table.pack(fill = BOTH, expand = 1)
        #self.Student_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)

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
        


if __name__ == "__main__":
    root = Tk()
    root.wm_attributes('-transparentcolor')
    obj = Print_Win(root)
    root.mainloop()