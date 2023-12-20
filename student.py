from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Engineering Cycle Management")
        self.root.resizable(False, False)

        # Vars
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_cne = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_photo = StringVar()

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
        title_lbl = Label(self.root, text="Student Management System", font=("poppins", 35, "bold"), bg="white",
                          fg="blue")
        title_lbl.place(x=0, y=130, width=1530, height=55)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=60, width=1480, height=600)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("poppins", 12, "bold"),
                                bg="white")
        left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"images/student_img1.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # Current Course
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Course",
                                          font=("poppins", 12, "bold"), bg="white")
        current_course_frame.place(x=5, y=135, width=720, height=150)

        # Departement :
        dep_label = Label(current_course_frame, text="Departement", font=("poppins", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("poppins", 12, "bold"),
                                 width=17, state="read only")
        dep_combo["values"] = ("Select Departement", "Informatics", "Physics", "Biliogy")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course :
        course_label = Label(current_course_frame, text="Course", font=("poppins", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("poppins", 12, "bold"),
                                    width=17, state="read only")
        course_combo["values"] = ("Select Course", "Python", "Java", "Machine Learning", "Nest JS", "Economy")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year :
        year_label = Label(current_course_frame, text="Year", font=("poppins", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("poppins", 12, "bold"),
                                  width=17, state="read only")
        year_combo["values"] = ("Select Year", "2021/2022", "2022/2023", "2023/2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semster :
        semster_label = Label(current_course_frame, text="Semster", font=("poppins", 12, "bold"), bg="white")
        semster_label.grid(row=1, column=2, padx=10, sticky=W)

        semster_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=("poppins", 12, "bold"),
                                     width=17, state="read only")
        semster_combo["values"] = ("Select Semster", "Semster 1", "Semster 2", "Semster 3", "Semster 4", "Semster 5")
        semster_combo.current(0)
        semster_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, bg="white", text="Class Student Information",
                                         font=("poppins", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)

        # Student ID
        studentid_label = Label(class_student_frame, text="Student ID :", bg="white", font=("poppins", 12, "bold"))
        studentid_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentid_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_std_id,
                                    font=("poppins", 12, "bold"))
        studentid_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        student_name_label = Label(class_student_frame, text="Student Name :", bg="white", font=("poppins", 12, "bold"))
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_std_name,
                                       font=("poppins", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Devision //////// Date de Naissance
        class_devision_label = Label(class_student_frame, text="Date of Birth :", bg="white",
                                     font=("poppins", 12, "bold"))
        class_devision_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_devision_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_div,
                                         font=("poppins", 12, "bold"))
        class_devision_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # National Number
        national_num_label = Label(class_student_frame, text="National Number :", bg="white",
                                   font=("poppins", 12, "bold"))
        national_num_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        national_num_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_cne,
                                       font=("poppins", 12, "bold"))
        national_num_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender :", bg="white", font=("poppins", 12, "bold"))
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("poppins", 12, "bold"),
                                    width=18, state="read only")
        gender_combo["values"] = ("Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Phone Number
        phone_label = Label(class_student_frame, text="Phone Number :", bg="white", font=("poppins", 12, "bold"))
        phone_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_phone,
                                font=("poppins", 12, "bold"))
        phone_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address :", bg="white", font=("poppins", 12, "bold"))
        address_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_address,
                                  font=("poppins", 12, "bold"))
        address_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(class_student_frame, text="Teacher Name :", bg="white", font=("poppins", 12, "bold"))
        teacher_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_teacher,
                                  font=("poppins", 12, "bold"))
        teacher_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take a Sample Photo",
                                    value="Yes")
        radiobtn1.grid(row=6, column=0)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio2, text="No Sample Photo",
                                    value="No")
        radiobtn2.grid(row=6, column=1)

        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=715, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("poppins", 12, "bold"),
                          bg="lime", fg="dark green")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=("poppins", 12, "bold"),
                            bg="cyan", fg="dark green")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("poppins", 12, "bold"),
                            bg="red", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, command=self.rest_data, font=("poppins", 12, "bold"),
                           bg="yellow", fg="green")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take photo Sample", width=35,
                                font=("poppins", 12, "bold"), bg="blue",
                                fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=("poppins", 12, "bold"),
                                  bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Table", font=("poppins", 12, "bold"))
        right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(r"images/student_img2.jpg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # Search System
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search : ",
                                  font=("poppins", 12, "bold"))
        search_frame.place(x=5, y=150, width=700, height=70)

        search_label = Label(search_frame, text="Search by :", bg="white", font=("poppins", 15, "bold"))
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("poppins", 12, "bold"), width=15, state="read only")
        search_combo["values"] = ("Select", "CNE", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=13, font=("poppins", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, font=("poppins", 11, "bold"), bg="gray", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showall_btn = Button(search_frame, text="Show All", width=12, font=("poppins", 11, "bold"), bg="blue",
                             fg="white")
        showall_btn.grid(row=0, column=4, padx=4)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=225, width=700, height=330)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("id", "course", "year", "sem", "dep", "name", "dob",
                                                                "cne", "gender", "phone", "address", "teacher",
                                                                "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("cne", text="CNE")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("cne", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        self.student_table.column("dep", width=100)

    # Fucntions

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required 🙅‍♂️🙅‍♂️", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="python_projet")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_std_id.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_dep.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_cne.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Succes", "Student Information has been addede Successfully",
                                    parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Something went wrong, Due to : {str(es)}",
                                     parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="python_projet")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_std_id.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_dep.set(data[4])
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_cne.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_address.set(data[10]),
        self.var_teacher.set(data[11]),
        self.var_radio1.set(data[12])

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required 🙅‍♂️🙅‍♂️", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Are you sure & you want to update this data",
                                             parent=self.root)
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="python_projet")
                my_cursor = conn.cursor()
                if update > 0:
                    my_cursor.execute("UPDATE student SET course = %s, year = %s, semster = %s,"
                                      "dep = %s, name = %s, division = %s, cne = %s, gender = %s, phone = %s,"
                                      "address = %s, teacher = %s, photo = %s WHERE student_id = %s", (
                                          self.var_course.get(),
                                          self.var_year.get(),
                                          self.var_sem.get(),
                                          self.var_dep.get(),
                                          self.var_std_name.get(),
                                          self.var_div.get(),
                                          self.var_cne.get(),
                                          self.var_gender.get(),
                                          self.var_phone.get(),
                                          self.var_address.get(),
                                          self.var_teacher.get(),
                                          self.var_radio1.get(),
                                          self.var_std_id.get(),
                                      ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Sucess", "Data Updatedd Succefully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Something went wrong, beacause of ->{str(es)}",
                                     parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", f"Something went wrong, Unselected Student", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student",
                                             parent=self.root)
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="python_projet")
                my_cursor = conn.cursor()
                if delete > 0:
                    my_cursor.execute("DELETE FROM student WHERE student_id = %s", (self.var_std_id.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess", "Line Delete Succefully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Something went wrong, beacause of ->{str(es)}", parent=self.root)

    def rest_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_cne.set("")
        self.var_gender.set("Male")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # === Generate Dataset / Take Photo Sample ====

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required 🙅‍♂️🙅‍♂️", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="python_projet")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                my_results = my_cursor.fetchall()
                id = 0
                for x in my_results:
                    id += 1
                my_cursor.execute("UPDATE student SET course = %s, year = %s, semster = %s,"
                                  "dep = %s, name = %s, division = %s, cne = %s, gender = %s, phone = %s,"
                                  "address = %s, teacher = %s, photo = %s WHERE student_id = %s", (
                                      self.var_course.get(),
                                      self.var_year.get(),
                                      self.var_sem.get(),
                                      self.var_dep.get(),
                                      self.var_std_name.get(),
                                      self.var_div.get(),
                                      self.var_cne.get(),
                                      self.var_gender.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(),
                                      self.var_teacher.get(),
                                      self.var_radio1.get(),
                                      self.var_std_id.get() == id + 1,
                                  ))
                conn.commit()
                self.fetch_data()
                self.rest_data()
                conn.close()

                # === Load predefined data on face frontal from opencv ===
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Results", "Generating Datasets sets completed")

            except Exception as es:
                messagebox.showerror("Error", f"Something went wrong, beacause -->{str(es)}", parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)

    root.mainloop()
