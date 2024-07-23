from ultralytics import YOLO
import cv2
import math
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

class ASLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ASL Identifier")

        # Create canvas for video feed
        self.canvas = tk.Canvas(root, width=416, height=416)
        self.canvas.pack()

        # Create a button to switch cameras
        self.switch_camera_button = tk.Button(root, text="Switch Camera", command=self.switch_camera)
        self.switch_camera_button.pack()

        self.model = YOLO("model-data/exp2/weights/best.pt")
        self.class_names = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
            'W', 'X', 'Y', 'Z'
        ]

        self.camera_index = 0
        self.cap = self.initialize_camera()

        self.update_frame()

    def initialize_camera(self):
        cap = cv2.VideoCapture(self.camera_index)
        if not cap.isOpened():
            messagebox.showerror("Camera Error", f"Failed to open camera {self.camera_index}.")
            return None
        cap.set(3, 416) 
        cap.set(4, 416)
        return cap

    def switch_camera(self):
        if self.cap:
            self.cap.release()  # Release the current camera
        
        self.camera_index = (self.camera_index + 1) % 2  # Change to the next camera
        self.cap = self.initialize_camera()

        if not self.cap:
            # If camera initialization failed, stay on the current camera
            self.camera_index = (self.camera_index - 1) % 2
            self.cap = self.initialize_camera()
        
    def update_frame(self):
        if not self.cap:
            # If the camera is not initialized, skip updating frames
            self.root.after(10, self.update_frame)
            return

        ret, img = self.cap.read()
        if not ret:
            print("Failed to grab frame")
            self.cap.release()
            self.cap = None
            self.root.after(10, self.update_frame)
            return

        results = self.model(img, stream=True)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                confidence = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])

                org = (x1, y1 - 10)
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (0, 0, 0)
                thickness = 2

                cv2.putText(img, f'{self.class_names[cls]} {confidence}', org, font, fontScale, color, thickness)

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(image=img_pil)

        # Use a tag to update the image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.canvas.image = img_tk  # Keep a reference to avoid garbage collection

        # Schedule the next frame update
        self.root.after(10, self.update_frame)  # Refresh frame every 10 ms

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ASLApp(root)
    app.run()
