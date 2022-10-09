import tkinter
from tkinter import *
import tkinter.messagebox as mb
import cv2
import mysql.connector as ms

w=tkinter.Tk()
w.title("Automated Cheque Processing System")
w.geometry("1350x600")
w.config(bg='black')
img=PhotoImage(file="IMG_20200309_181431 (1).png")
label=Label(w,image=img)
label.place(x=0,y=0)



def Image_processing():  #Capturing Image
  mb.showinfo("Alert",'Opening scaning windows')
  key = cv2. waitKey(1)
  webcam = cv2.VideoCapture(0)
  while True:
        try:
            check, frame = webcam.read()
            #print(frame) #prints matrix values of each frames 
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 400*400 scale...")
            img_ = cv2.resize(gray,(400,400))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
            mb.showinfo("Alert",'Image Scanned proceed further')
            image_ml()
            break
            
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyroyAllWindows()
            break


def image_ml():
    MyDB =ms.connect(host="localhost", user= "root", password="sarbesh", database="image_processing")
    MyCursor = MyDB.cursor()
    MyCursor.execute("CREATE TABLE IF NOT EXISTS `Images` ( `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT, `Photo` LONGBLOB NOT NULL,PRIMARY KEY(`id`))")

    
    
    def InsertBlob(FilePath): #insert image in mysql server/database
       
        with open(FilePath, "rb") as File:
            BinaryData =File.read()
        SQLStatement = "INSERT INTO Images (Photo) VALUES (%s)"
        MyCursor.execute(SQLStatement, (BinaryData, ))
        MyDB.commit()
        

    def RetrieveBlob(ID): # retrive image from mysql to local system
        SQLStatement2= "SELECT * FROM Images WHERE id = '{0}'"
        MyCursor.execute(SQLStatement2.format(str(ID)))
        MyResult= MyCursor.fetchone()[1]
        StoreFilePath ="Image/img{0}.jpg".format(str(ID))
        print(MyResult)
        with open(StoreFilePath, "wb") as File:
            File.write(MyResult)
            File.close()

    print("1. Insert Image\n2. Read Image")
    MenuInput =input()
    if int(MenuInput) == 1:
        UserFilePath =input("Enter File Path:")
        InsertBlob(UserFilePath)
    elif int(MenuInput) == 2:
        UserIDChoice = input("Enter ID:")
        RetrieveBlob(UserIDChoice)
    else:
        print("Byeeeee")


def home():
    
    button1=Button(w, text='Continue', width=10, font=("Arial Bold",12),\
       command=Image_processing).grid(row=1, column=1, sticky='w', padx=120, pady=100)
    

home()

