from tkinter import *
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Engineering Cycle Management")
        self.root.resizable(False, False)

        # logo
        img = Image.open(r"images/logo_fst.png")
        img = img.resize((500, 120), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=500, y=0, width=500, height=120)

        # background
        img1 = Image.open(r"images/bg.png")
        img1 = img1.resize((1530, 710), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title
        title_lbl = Label(bg_img, text="Engineering Cycle Management", font=("poppins", 35, "bold"), bg="white",
                          fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=55)

        # Student Button
        img2 = Image.open(r"images/person.jpg")
        img2 = img2.resize((220, 220), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(bg_img, image=self.photoimg2, command=self.student_details, cursor="hand2")
        b1.place(x=250, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
                      font=("poppins", 15, "bold"), bg="cyan", fg="green")
        b1_1.place(x=250, y=300, width=220, height=40)

        # Detect Face Button
        img3 = Image.open(r"images/person2.jpg")
        img3 = img3.resize((220, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b2 = Button(bg_img, image=self.photoimg3, cursor="hand2", command=self.face_data)
        b2.place(x=675, y=100, width=220, height=220)
        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=("poppins", 15, "bold"), bg="cyan", fg="green")
        b2_1.place(x=675, y=300, width=220, height=40)

        # Attendance Button
        img4 = Image.open(r"images/person3.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b3 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.attend_data)
        b3.place(x=1050, y=100, width=220, height=220)
        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attend_data, font=("poppins", 15, "bold"), bg="cyan", fg="green")
        b3_1.place(x=1050, y=300, width=220, height=40)

        # Train Data Button
        img5 = Image.open(r"images/person4.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b4 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.train_data)
        b4.place(x=250, y=380, width=220, height=220)
        b4_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("poppins", 15, "bold"), bg="cyan", fg="green")
        b4_1.place(x=250, y=580, width=220, height=40)

        # Photos Button
        img6 = Image.open(r"images/person5.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b5 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.open_img)
        b5.place(x=675, y=380, width=220, height=220)
        b5_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("poppins", 15, "bold"), bg="cyan", fg="green")
        b5_1.place(x=675, y=580, width=220, height=40)

        # Help Button
        img7 = Image.open(r"images/person6.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b6 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b6.place(x=1050, y=380, width=220, height=220)
        b6_1 = Button(bg_img, text="Help", cursor="hand2", font=("poppins", 15, "bold"), bg="cyan", fg="green")
        b6_1.place(x=1050, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    # Make buttons work
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def attend_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)

    root.mainloop()
