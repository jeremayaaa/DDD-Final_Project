from tkinter import*
from PIL import Image, ImageTk
from student import Student_Win
from payment import Payment_Win
from about import About_Win
from contact import Contact_Win


class Student_Info:
    def __init__(self, root):
        self.root = root
        self.root.title("Adamson University")
        self.root.geometry("1550x800+0+0")

        #-------------- BG --------------
        imgbg = Image.open(r"C:\Users\jere\DATABASE\adamson-university1.jpg")
        imgbg = imgbg.resize((1550, 300), Image.ANTIALIAS)
        self.photoimgbg = ImageTk.PhotoImage(imgbg)

        lblimgbg = Label(self.root, image = self.photoimgbg, bd = 4, relief = RIDGE)
        lblimgbg.place(x = 0, y = 0, width = 1550, height = 150)

        #-------------- LOGO --------------
        #logo = Image.open(r"C:\Users\jere\DATABASE\logo.PNG")
        #logo = logo.resize((150, 150), Image.ANTIALIAS)
        #self.photologo = ImageTk.PhotoImage(logo)

        #lblimg = Label(self.root, image = self.photologo, bg = "navy blue", bd = 4, relief = RIDGE)
        #lblimg.place(x = 0, y = 0, width = 255, height = 150)

        #-------------- TITLE --------------
        lbl_title = Label(self.root, text="ADAMSON UNIVERSITY", font = ("Times New Roman", 40, "bold"), bg = "navy blue", fg = "white", bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y = 150, width = 1551, height = 50)

        #-------------- MAIN FRAME --------------
        main_frame = Frame(self.root, bd = 4, relief = RIDGE)
        main_frame.place(x=0, y=200, width = 1550, height = 620)

        #-------------- MENU --------------
        lbl_menu = Label(main_frame, text="MENU", font = ("Times New Roman", 20, "bold"), bg = "navy blue", fg = "white", bd = 4, relief = RIDGE)
        lbl_menu.place(x = 0, y = 0, width = 255, height = 50)

        #-------------- BUTTON FRAME --------------
        btn_frame = Frame(main_frame, bd = 3, relief = RIDGE)
        btn_frame.place(x=0, y=50, width = 255, height = 153)

        student_btn = Button(btn_frame, text="ONLINE ENROLLMENT", command = self.student_details, width = 22, font = ("Times New Roman", 14, "bold"), bg = "sky blue", fg = "navy blue", bd = 0, cursor = "hand1")
        student_btn.grid(row = 0, column = 0, pady = 1)
        
        dp_btn = Button(btn_frame, text="ONLINE PAYMENT", command = self.payment_details, width = 22, font = ("Times New Roman", 14, "bold"), bg = "sky blue", fg = "navy blue", bd = 0, cursor = "hand1")
        dp_btn.grid(row = 1, column = 0, pady = 1)
        
        details_btn = Button(btn_frame, text="ABOUT", command = self.about_details, width = 22, font = ("Times New Roman", 14, "bold"), bg = "sky blue", fg = "navy blue", bd = 0, cursor = "hand1")
        details_btn.grid(row = 2, column = 0, pady = 1)

        logout_btn = Button(btn_frame, text="CONTACT", command = self.contact_details,width = 22, font = ("Times New Roman", 14, "bold"), bg = "sky blue", fg = "navy blue", bd = 0, cursor = "hand1")
        logout_btn.grid(row = 3, column = 0, pady = 1)

        #-------------- MAIN BG --------------
        main_bg = Image.open(r"C:\Users\jere\DATABASE\svbg.jpg")
        main_bg = main_bg.resize((1288, 590), Image.ANTIALIAS)
        self.photomain_bg = ImageTk.PhotoImage(main_bg)

        lblmain_bg = Label(main_frame, image = self.photomain_bg, bd = 4, relief = RIDGE)
        lblmain_bg.place(x = 255, y = 0, width = 1288, height = 595)

        #-------------- IMAGES --------------
        img1 = Image.open(r"C:\Users\jere\DATABASE\student1.png")
        img1 = img1.resize((255, 210), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(main_frame, image = self.photoimg1, bd = 4, relief = RIDGE)
        lblimg1.place(x = 0, y = 200, width = 255, height = 210)

        img2 = Image.open(r"C:\Users\jere\DATABASE\student2.jpg")
        img2 = img2.resize((255, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(main_frame, image = self.photoimg2, bd = 4, relief = RIDGE)
        lblimg2.place(x = 0, y = 395, width = 255, height = 200)

    #-------------- STUDENT APPLICATION --------------
    def student_details(self):
        self.new_window = Toplevel(self.root)      
        self.app = Student_Win(self.new_window)

    def payment_details(self):
        self.new_window = Toplevel(self.root)      
        self.app = Payment_Win(self.new_window)

    def about_details(self):
        self.new_window = Toplevel(self.root)      
        self.app = About_Win(self.new_window)

    def contact_details(self):
        self.new_window = Toplevel(self.root)      
        self.app = Contact_Win(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = Student_Info(root)
    root.mainloop()

