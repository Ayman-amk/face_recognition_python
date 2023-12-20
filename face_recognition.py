from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
from datetime import datetime

class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Engineering Cycle Management")
        self.root.resizable(False, False)

        img = Image.open(r"images/logo_fst.png")
        img = img.resize((500, 120), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=500, y=0, width=500, height=120)

        title_lbl = Label(self.root, text="Face Recognintion", font=("poppins", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=130, width=1530, height=55)

        img2 = Image.open(r"images/face_detect.jpg")
        img2 = img2.resize((650, 700), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl1 = Label(self.root, image=self.photoimg2)
        f_lbl1.place(x=0, y=200, width=1530, height=700)

        # Button pour trainer Data
        b1_1 = Button(f_lbl1, text="Face Recognition", cursor="hand2", command=self.face_recog,
                      font=("poppins", 18, "bold"),
                      bg="cyan", fg="blue")
        b1_1.place(x=615, y=520, width=300, height=50)

    # Presence
    def mark_attendance(self, ids, cne, name, sem):
        with open("data.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if (ids not in name_list) and (cne not in name_list) and (name not in name_list) and (sem not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d / %m / %Y")
                dtString = now.strftime("%H : %M : %S")
                f.writelines(f"\n{ids}, {cne}, {name}, {sem}, {dtString}, {d1}, Present")

    # Face Recognition
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="", database="python_projet")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT name FROM student WHERE student_id = " + str(id))
                name = my_cursor.fetchone()
                name = "+".join(name)

                my_cursor.execute("SELECT cne FROM student WHERE student_id = " + str(id))
                cne = my_cursor.fetchone()
                cne = "+".join(cne)

                my_cursor.execute("SELECT semster FROM student WHERE student_id = " + str(id))
                sem = my_cursor.fetchone()
                sem = "+".join(sem)

                my_cursor.execute("SELECT student_id FROM student WHERE student_id = " + str(id))
                ids = my_cursor.fetchone()

                if ids:
                    # Convert each element to string before joining
                    ids = "+".join(map(str, ids))

                if confidence > 77:
                    cv2.putText(img, f"ID : {ids}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 0, 0), 3)
                    cv2.putText(img, f"CNE : {cne}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 0, 0), 3)
                    cv2.putText(img, f"Name : {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 0, 0), 3)
                    cv2.putText(img, f"Semester : {sem}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 0, 0), 3)
                    self.mark_attendance(ids, cne, name, sem)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unkown Face !", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 255, 255), 3)

                coord = [x, y, w, y]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = (Face_recognition(root))

    root.mainloop()
