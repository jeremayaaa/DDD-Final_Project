from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox


class About_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Adamson University")
        self.root.geometry("1285x563+260+233")

        #-------------- TITLE --------------
        lbl_title = Label(self.root, text="ABOUT ADAMSON UNIVERSITY", font = ("Arial", 18, "bold"), bg = "sky blue", fg = "navy blue", bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

        #-------------- LABEL FRAME --------------
        label_frame_pres = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "About the President", font = ("Arial", 12, "bold"), padx =1 )
        label_frame_pres.place(x = 10, y = 55, width  = 555, height = 500)

        #-------------- FATHER --------------
        father = Image.open(r"C:\Users\jere\DATABASE\father.jpg")
        father = father.resize((210, 300), Image.ANTIALIAS)
        self.photofather = ImageTk.PhotoImage(father)

        lblfather = Label(label_frame_pres, image = self.photofather, bd = 4, relief = RIDGE)
        lblfather.place(x = 5, y = 5, width = 210, height = 308)

        #text for father
        label_father_name = Label(label_frame_pres, text = "Fr. Marcelo V. Manimtim, CM", font = ("Arial", 10, "bold"), padx = 2, pady = 4)
        label_father_name.place (x = 220, y = 5)

        label_position = Label(label_frame_pres, text = "Sixth President of Adamson University", font = ("Arial", 10, "bold"), padx = 2, pady = 4)
        label_position.place (x = 220, y = 25)

        label_des1 = Label(label_frame_pres, text = " Fr. Marcelo V. Manimtim, CM was born on October 30, 1950 in", font = ("Arial", 8), padx = 2, pady = 4)
        label_des1.place (x = 230, y = 50)
        label_des2 = Label(label_frame_pres, text = "Tagaytay City, Cavite province. He began his elementary studies in", font = ("Arial", 8), padx = 2, pady = 4)
        label_des2.place (x = 217, y = 70)
        label_des3 = Label(label_frame_pres, text = "Tagaytay and entered St. Vincent’s Seminary in Valenzuela, ", font = ("Arial", 8), padx = 2, pady = 4)
        label_des3.place (x = 217, y = 90)
        label_des4 = Label(label_frame_pres, text = "Bulacan in June 1963 after a chance meeting with a Vincentian", font = ("Arial", 8), padx = 2, pady = 4)
        label_des4.place (x = 217, y = 110)
        label_des5 = Label(label_frame_pres, text = "priest during the summer. ", font = ("Arial", 8), padx = 2, pady = 4)
        label_des5.place (x = 217, y = 130)

        label_des6 = Label(label_frame_pres, text = "Fr. Manimtim finished AB in Philosophy at Adamson University", font = ("Arial", 8), padx = 2, pady = 4)
        label_des6.place (x = 230, y = 150)
        label_des7 = Label(label_frame_pres, text = "in 1972, thus making him the second alumnus to become President", font = ("Arial", 8), padx = 2, pady = 4)
        label_des7.place (x = 217, y = 170)
        label_des8 = Label(label_frame_pres, text = "of the university. He then studied Theology at the University of", font = ("Arial", 8), padx = 2, pady = 4)
        label_des8.place (x = 217, y = 190)
        label_des9 = Label(label_frame_pres, text = "Santo Tomas, graduating with a bachelor’s degree in 1976.", font = ("Arial", 8), padx = 2, pady = 4)
        label_des9.place (x = 217, y = 210)
        
        label_des10 = Label(label_frame_pres, text = "His path to priesthood continued at the Vincentian Hills Seminary,", font = ("Arial", 8), padx = 2, pady = 4)
        label_des10.place (x = 230, y = 230)
        label_des11 = Label(label_frame_pres, text = "which he entered in June 1968. Fr. Manimtim made his perpetual", font = ("Arial", 8), padx = 2, pady = 4)
        label_des11.place (x = 217, y = 250)
        label_des12 = Label(label_frame_pres, text = "vows on May 26, 1975 and was ordained to the priesthood on ", font = ("Arial", 8), padx = 2, pady = 4)
        label_des12.place (x = 217, y = 270)
        label_des13 = Label(label_frame_pres, text = "March 15, 1976. ", font = ("Arial", 8), padx = 2, pady = 4)
        label_des13.place (x = 217, y = 290)

        label_des14 = Label(label_frame_pres, text = "He took graduate studies at the Gregorian Pontifical University in Rome, Italy, finishing his special studies in", font = ("Arial", 8), padx = 2, pady = 4)
        label_des14.place (x = 16, y = 313)
        label_des14 = Label(label_frame_pres, text = "Church History in 1980 and his doctorate in Philosophy in 1993.   ", font = ("Arial", 8), padx = 2, pady = 4)
        label_des14.place (x = 3, y = 333)

        label_des15 = Label(label_frame_pres, text = "Fr. Manimtim’s pastoral ministry began in 1976, when he was appointed Prefect of Discipline at St. Vincent’s ", font = ("Arial", 8), padx = 2, pady = 4)
        label_des15.place (x = 16, y = 353)
        label_des16 = Label(label_frame_pres, text = "Seminary in Bulacan. After finishing his studies in Rome, he returned to the Philippines in 1980 and taught  ", font = ("Arial", 8), padx = 2, pady = 4)
        label_des16.place (x = 3, y = 373)
        label_des17 = Label(label_frame_pres, text = "Church History at the San Carlos Major Seminary in Cebu City for a year. In 1981, he became the Spiritual", font = ("Arial", 8), padx = 2, pady = 4)
        label_des17.place (x = 3, y = 393)
        label_des18 = Label(label_frame_pres, text = "Director at Vincentian Hills Seminary in Angono, Rizal for three years and Rector for four years. After pursuing ", font = ("Arial", 8), padx = 2, pady = 4)
        label_des18.place (x = 3, y = 413)
        label_des19 = Label(label_frame_pres, text = "his doctorate, he was sent as a missionary to the Solomon Islands in 1993. Together with two other ", font = ("Arial", 8), padx = 2, pady = 4)
        label_des19.place (x = 3, y = 433)
        label_des20 = Label(label_frame_pres, text = "Vincentians, he established the Holy Name of Mary Seminary in Honiara.", font = ("Arial", 8), padx = 2, pady = 1)
        label_des20.place (x = 3, y = 453)


        #-------------- LABEL FRAME --------------
        label_frame_vis = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Vision and Mission Statement", font = ("Arial", 12, "bold"), padx =1 )
        label_frame_vis.place(x = 570, y = 55, width  = 705, height = 275)

        label_vis1 = Label(label_frame_vis, text = "Vision Statement", font = ("Arial", 10, "bold"), padx = 2, pady = 4)
        label_vis1.place (x = 5, y = 3)
        label_vis2 = Label(label_frame_vis, text = "Adamson University, a Catholic, Vincentian educational institution, is a recognized leading center for quality education particularly", font = ("Arial", 8), padx = 2, pady = 4)
        label_vis2.place (x = 5, y = 23)
        label_vis3 = Label(label_frame_vis, text = "for the socially disadvantaged.", font = ("Arial", 8), padx = 2, pady = 4)
        label_vis3.place (x = 5, y = 43)

        label_vis4 = Label(label_frame_vis, text = "Mission Statement", font = ("Arial", 10, "bold"), padx = 2, pady = 4)
        label_vis4.place (x = 5, y = 73)
        label_vis5 = Label(label_frame_vis, text = "As a Catholic University, we diligently pursue truth and knowledge, inspired by Gospel values and guided by the teachings of the Church;", font = ("Arial", 8), padx = 2, pady = 4)
        label_vis5.place (x = 5, y = 93)
        label_vis6 = Label(label_frame_vis, text = "As a Vincentian community, we inspire others to follow the example of St. Vincent de Paul , who led and organized his contemporaries", font = ("Arial", 8), padx = 2, pady = 4)
        label_vis6.place (x = 5, y = 123)
        label_vis7 = Label(label_frame_vis, text = "in creatively responding to those who are in need;", font = ("Arial", 8), padx = 2, pady = 4)
        label_vis7.place (x = 5, y = 143)
        label_vis8 = Label(label_frame_vis, text = "As an institution of learning, we assist in the formation of competent, creative and socially responsible leaders through our commitment", font = ("Arial", 8), padx = 2, pady = 4)
        label_vis8.place (x = 5, y = 173)
        label_vis9 = Label(label_frame_vis, text = "to excellence in discovery, learning and service;", font = ("Arial", 8), padx = 2, pady = 4)
        label_vis9.place (x = 5, y = 193)
        label_vis10 = Label(label_frame_vis, text = "As a catalyst of social transformation, we provide quality services that empower others to become agents of change.", font = ("Arial", 8), padx = 2, pady = 4)
        label_vis10.place (x = 5, y = 223)

        #-------------- LABEL FRAME --------------
        label_frame_paul = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "About St. Vincent de Paul", font = ("Arial", 12, "bold"), padx =1 )
        label_frame_paul.place(x = 570, y = 335, width  = 705, height = 220)

        #-------------- FATHER --------------
        vincent = Image.open(r"C:\Users\jere\DATABASE\vincent.jpg")
        vincent = vincent.resize((210, 300), Image.ANTIALIAS)
        self.photovincent = ImageTk.PhotoImage(vincent)

        lblvincent = Label(label_frame_paul, image = self.photovincent, bd = 4, relief = RIDGE)
        lblvincent.place(x = 5, y = 5, width = 150, height = 185)

        label_vince1 = Label(label_frame_paul, text = "This remarkable man, born at Pouy in Southern France in 1581, had a rather self-seeking start in the", font = ("Arial", 8), padx = 2, pady = 4)
        label_vince1.place (x = 173, y = 3)
        label_vince2 = Label(label_frame_paul, text = "priesthood. Under the influence of spiritual directors like St. Francis de Sales, Cardinal de Berulle, and Andre", font = ("Arial", 8), padx = 2, pady = 4)
        label_vince2.place (x = 160, y = 23)
        label_vince3 = Label(label_frame_paul, text = "Duval, he underwent a striking conversion in which he gave his life over to God in the service of the poor. ", font = ("Arial", 8), padx = 2, pady = 4)
        label_vince3.place (x = 160, y = 43)
        label_vince4 = Label(label_frame_paul, text = "He founded the Congregation of the Mission in 1625, a community of priests and brothers whose end is", font = ("Arial", 8), padx = 2, pady = 4)
        label_vince4.place (x = 160, y = 63)
        label_vince5 = Label(label_frame_paul, text = "'to preach the good news to the poor' and the Daughters of Charity (1633), at that time a new form of", font = ("Arial", 8), padx = 2, pady = 4)
        label_vince5.place (x = 160, y = 83)
        label_vince6 = Label(label_frame_paul, text = "community where the sisters lived in the world' to serve the sick poor spiritually and corporally. He also", font = ("Arial", 8), padx = 2, pady = 4)
        label_vince6.place (x = 160, y = 103)
        label_vince7 = Label(label_frame_paul, text = "established the Confraternities of Charity (lay organizations, both of men and women, founded in parishes ", font = ("Arial", 8), padx = 2, pady = 4)
        label_vince7.place (x = 160, y = 123)
        label_vince8 = Label(label_frame_paul, text = "also to assist the poor spiritually and corporally) and the Ladies of Charity. These groups continue to the ", font = ("Arial", 8), padx = 2, pady = 4)
        label_vince8.place (x = 160, y = 143)
        label_vince9 = Label(label_frame_paul, text = "present day in a very large numbers.", font = ("Arial", 8), padx = 2, pady = 4)
        label_vince9.place (x = 160, y = 163)




if __name__ == "__main__":
    root = Tk()
    obj = About_Win(root)
    root.mainloop()