import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import numpy as np

class WebcamApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Webcam with Rounded Corners")

        self.video_frame = tk.Label(self.window)
        self.video_frame.pack(padx=10, pady=10)

        # Open the webcam
        self.cap = cv2.VideoCapture(0)
        self.show_frame()

    def show_frame(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to ImageTk format
        img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

        # Update the video frame
        self.video_frame.img = img
        self.video_frame.config(image=img)

        # Schedule the next update in 10 milliseconds
        self.window.after(10, self.show_frame)


if __name__ == "__main__":
    root = tk.Tk()
    app = WebcamApp(root)
    root.mainloop()