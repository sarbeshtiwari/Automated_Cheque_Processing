import tkinter
from tkinter import *
import tkinter.messagebox as mb
import cv2

w=tkinter.Tk()
w.title("Automated Cheque Processing System")
w.geometry("1350x600")



def Image_processing():
  mb.showinfo("Alert",'Opening scaning windows')
  key = cv2. waitKey(1)
  webcam = cv2.VideoCapture(0)
  while True:
        try:
            check, frame = webcam.read()
            print(frame) #prints matrix values of each framecd 
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
    print("Hello")

def home():
    
    Button(w, text='Continue', width=10, font=("Arial Bold",12),\
       command=Image_processing).grid(row=1, column=1, sticky='w', pady=4)

home()

