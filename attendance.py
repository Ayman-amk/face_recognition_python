from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk, filedialog
import os
import csv


mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Engineering Cycle Management")
        self.root.resizable(False, False)

        # Vars
        self.var_attend_id = StringVar()
        self.var_cne = StringVar()
        self.var_name = StringVar()
        self.var_semester = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_attend = StringVar()

        # Logo
        img = Image.open(r"images/logo_fst.png")
        img = img.resize((500, 120), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=500, y=0, width=500, height=120)

        # Background
        img1 = Image.open(r"images/bg.png")
        img1 = img1.resize((1530, 710), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(self.root, text="Presence List", font=("poppins", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=130, width=1530, height=55)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=60, width=1480, height=600)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Presence Details",
                                font=("poppins", 12, "bold"), bg="white")
        left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"images/attendance.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        left_inside_frame.place(x=0, y=150, width=725, height=400)

        # Inputs

        # Attend ID
        attendanceId_label = Label(left_inside_frame, text="Attnd ID :", bg="white",
                                   font=("poppins", 12, "bold"))
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_attend_id,
                                       font=("poppins", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, pady=5, sticky=W)

        # Name ID
        attendanceName_label = Label(left_inside_frame, text="Attnd Name :", bg="white",
                                     font=("poppins", 12, "bold"))
        attendanceName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        attendanceName_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_name,
                                        font=("poppins", 12, "bold"))
        attendanceName_entry.grid(row=0, column=3, pady=5, sticky=W)

        # CNE ID
        attendanceName_label = Label(left_inside_frame, text="Attnd CNE :", bg="white",
                                     font=("poppins", 12, "bold"))
        attendanceName_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        attendanceName_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_cne,
                                        font=("poppins", 12, "bold"))
        attendanceName_entry.grid(row=1, column=1, pady=5, sticky=W)

        # Semester ID
        semesterName_label = Label(left_inside_frame, text="Attnd Semster :", bg="white",
                                   font=("poppins", 12, "bold"))
        semesterName_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        semesterName_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_semester,
                                        font=("poppins", 12, "bold"))
        semesterName_entry.grid(row=1, column=3, pady=5, sticky=W)

        # Date
        attendanceDate_label = Label(left_inside_frame, text="Attnd Date :", bg="white",
                                     font=("poppins", 12, "bold"))
        attendanceDate_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        attendanceDate_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_date,
                                        font=("poppins", 12, "bold"))
        attendanceDate_entry.grid(row=2, column=1, pady=5, sticky=W)

        # Time
        attendanceTime_label = Label(left_inside_frame, text="Attnd Time :", bg="white",
                                     font=("poppins", 12, "bold"))
        attendanceTime_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        attendanceTime_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_time,
                                        font=("poppins", 12, "bold"))
        attendanceTime_entry.grid(row=2, column=3, pady=5, sticky=W)

        # Attendance
        attendanceTime_label = Label(left_inside_frame, text="Attnd Status :", bg="white",
                                     font=("poppins", 12, "bold"))
        attendanceTime_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_attend,
                                         font=("poppins", 12, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Buttons Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=715, height=35)

        Import_btn = Button(btn_frame, text="Import CSV", width=17, command=self.importCsv, font=("poppins", 12, "bold"),
                            bg="blue", fg="white")
        Import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv, width=17, font=("poppins", 12, "bold"),
                            bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=17, command=self.update_data, font=("poppins", 12, "bold"),
                            bg="cyan", fg="dark green")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, command=self.reste_data, font=("poppins", 12, "bold"),
                           bg="yellow", fg="green")
        reset_btn.grid(row=0, column=3)

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Presence Details", font=("poppins", 12, "bold"),
                                 bg="white")
        right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=5, width=700, height=480)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,
                                                  columns=("id", "cne", "name", "semester", "time", "date", "attend"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attnd ID")
        self.AttendanceReportTable.heading("cne", text="Attnd CNE")
        self.AttendanceReportTable.heading("name", text="Attnd Name")
        self.AttendanceReportTable.heading("semester", text="Attnd Semester")
        self.AttendanceReportTable.heading("time", text="Attnd Time")
        self.AttendanceReportTable.heading("date", text="Attnd date")
        self.AttendanceReportTable.heading("attend", text="Attnd Status")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("cne", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("semester", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attend", width=100)
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # Fetch Data
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )

        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No Data Found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Open CSV",
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                parent=self.root
            )
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success", "CSV Data "+os.path.basename(fln)+" Successfully Exported",
                                    parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Something went wrong, Due to : {str(es)}",
                                 parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']

        self.var_attend_id.set(rows[0])
        self.var_cne.set(rows[1])
        self.var_name.set(rows[2])
        self.var_semester.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attend.set(rows[6])

    def update_data(self):
        if self.var_attend_id.get() == "" or self.var_cne.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "Select Attendance Record to Update", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Are you sure you want to update this data?", parent=self.root)

                if update > 0:
                    for i in mydata:
                        if i[0] == self.var_attend_id.get():
                            i[1] = self.var_cne.get()
                            i[2] = self.var_name.get()
                            i[3] = self.var_semester.get()
                            i[4] = self.var_time.get()
                            i[5] = self.var_date.get()
                            i[6] = self.var_attend.get()

                    self.fetchData(mydata)
                    self.reste_data()

                    # Write the updated data back to the CSV file
                    self.exportCsv()

                    messagebox.showinfo("Success", "Data Updated Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Something went wrong, Due to: {str(es)}", parent=self.root)

    def reste_data(self):
        self.var_attend_id.set("")
        self.var_cne.set("")
        self.var_name.set("")
        self.var_semester.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("")


if __name__ == "__main__":
    root = Tk()
    obj = (Attendance(root))

    root.mainloop()
