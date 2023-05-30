from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox


class Contact_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Adamson University")
        self.root.geometry("1285x563+260+233")

        #-------------- TITLE --------------
        #lbl_title = Label(self.root, text="CONTACT US", font = ("Arial", 18, "bold"), bg = "sky blue", fg = "navy blue", bd = 4, relief = RIDGE)
        #lbl_title.place(x = 0, y = 0, width = 1286, height = 50)

        lbl_bg = Label(self.root, bd = 0, relief = RIDGE)
        lbl_bg.place(x = 0, y = 0, width = 1295, height = 600)

        #-------------- LOC --------------
        location = Image.open(r"C:\Users\jere\DATABASE\location.png")
        location = location.resize((30, 30), Image.ANTIALIAS)
        self.photolocation = ImageTk.PhotoImage(location)

        lbl_location = Label(lbl_bg, image = self.photolocation, bd = 0, relief = RIDGE)
        lbl_location.place(x = 485, y = 32, width = 30, height = 30)

        #label_loc1 = Label(lbl_bg, text = "Adamson University", font = ("Arial", 9), padx = 0, pady = 0)
        #label_loc1.place (x = 565, y = 20)
        #label_loc2 = Label(lbl_bg, text = "900 San Marcelino Street, Ermita", font = ("Arial", 9), padx = 0, pady = 0)
        #label_loc2.place (x = 565, y = 40)
        #label_loc3 = Label(lbl_bg, text = "1000 Manila, Philippines", font = ("Arial", 9), padx = 0, pady = 0)
        #label_loc3.place (x = 565, y = 60)

        #-------------- CALL --------------
        call = Image.open(r"C:\Users\jere\DATABASE\call.png")
        call = call.resize((30, 30), Image.ANTIALIAS)
        self.photocall = ImageTk.PhotoImage(call)

        lbl_call = Label(lbl_bg, image = self.photocall, bd = 0, relief = RIDGE)
        lbl_call.place(x = 485, y = 102, width = 30, height = 30)

        label_call1 = Label(lbl_bg, text = "8524 - 20 - 11", font = ("Arial", 9), padx = 0, pady = 0)
        label_call1.place (x = 565, y = 108)

        #-------------- MESSAGE --------------
        message = Image.open(r"C:\Users\jere\DATABASE\message.png")
        message = message.resize((30, 30), Image.ANTIALIAS)
        self.photomessage = ImageTk.PhotoImage(message)

        lbl_message = Label(lbl_bg, image = self.photomessage, bd = 0, relief = RIDGE)
        lbl_message.place(x = 485, y = 172, width = 30, height = 30)

        label_mess1 = Label(lbl_bg, text = "webmaster@adamson.edu.ph", font = ("Arial", 9), padx = 0, pady = 0)
        label_mess1.place (x = 565, y = 178)

        
        #-------------- BG --------------
        main_bg = Image.open(r"C:\Users\jere\DATABASE\svbg.jpg")
        main_bg = main_bg.resize((1288, 590), Image.ANTIALIAS)
        self.photomain_bg = ImageTk.PhotoImage(main_bg)

        lblmain_bg = Label(lbl_bg, image = self.photomain_bg, bd = 0, relief = RIDGE)
        lblmain_bg.place(x = 0, y = 0, width = 1285, height = 570)

        #-------------- CONTACT --------------
        contact = Image.open(r"C:\Users\jere\DATABASE\contact.png")
        contact = contact.resize((320, 160), Image.ANTIALIAS)
        self.photocontact = ImageTk.PhotoImage(contact)

        lbl_contact = Label(lbl_bg, image = self.photocontact, bd = 2, relief = RIDGE)
        lbl_contact.place(x = 495, y = 380, width = 320, height = 160)






if __name__ == "__main__":
    root = Tk()
    obj = Contact_Win(root)
    root.mainloop()