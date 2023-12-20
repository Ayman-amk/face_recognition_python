from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
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

        title_lbl = Label(self.root, text="Train Data", font=("poppins", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=130, width=1530, height=55)

        # Button to train Data
        b1_1 = Button(self.root, text="Train Data Now", command=self.train_classifier, cursor="hand2",
                      font=("poppins", 15, "bold"), bg="green", fg="white")
        b1_1.place(x=550, y=380, width=500, height=60)

    def train_classifier(self):
        data_dir = "data"
        classifier_file = "classifier.xml"

        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data directory '{data_dir}' not found!", parent=self.root)
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            try:
                with Image.open(image).convert('L') as img:
                    image_np = np.array(img, 'uint8')
                    id = int(os.path.split(image)[1].split('.')[1])

                    faces.append(image_np)
                    ids.append(id)

                    cv2.imshow("Training...", image_np)
                    cv2.waitKey(1) == 13
            except Exception as e:
                print(f"Error processing image {image}: {e}")

        ids = np.array(ids)

        if len(faces) == 0:
            messagebox.showerror("Error", "No training data found!", parent=self.root)
            return

        try:
            # Training
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write(classifier_file)
            cv2.destroyAllWindows()
            messagebox.showinfo("Results", "Training completed!", parent=self.root)

        except cv2.error as e:
            messagebox.showerror("Error", f"OpenCV error: {e}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
