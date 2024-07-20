import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import numpy as np

class WebcamApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Webcam")

        self.video_frame = tk.Label(self.window)
        self.video_frame.pack(padx=10, pady=10)

        self.switch_button = tk.Button(self.window, text="Switch Camera", command=self.switch_camera)
        self.switch_button.pack(pady=5)

        self.camera_index = 0  # Start with default camera index

        # Open the default webcam
        self.cap = cv2.VideoCapture(self.camera_index)
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

    def switch_camera(self):
        # Release the current camera capture
        self.cap.release()

        # Increment the camera index
        self.camera_index += 1

        # Try to open the new webcam
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            print(f"Cannot open camera {self.camera_index}, falling back to default camera.")
            self.camera_index = 0  # Fall back to default camera index
            self.cap = cv2.VideoCapture(self.camera_index)
        else:
            print(f"Switched to camera {self.camera_index}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WebcamApp(root)
    root.mainloop()