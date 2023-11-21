from tkinter import *
import threading
import cv2
import mediapipe as mp
import pyautogui

class VirtualMouseApp:
    def __init__(self):
        master = Tk()
        self.master = master
        master.title("Virtual Mouse")
        master.geometry("600x400")  # Set the GUI size
        master.configure(bg="#2c3e50")  # Set the background color of the GUI

        # Main Heading
        self.heading_label = Label(master, text="VIRTUAL MOUSE", font=("Helvetica", 24), bg="#4CAF50", fg="white")
        self.heading_label.pack(pady=10, fill=X)

        # Description
        self.description_label = Label(master, text="Control your mouse using eye movements", font=("Helvetica", 12), bg="#2c3e50", fg="white")
        self.description_label.pack(pady=10, fill=X)

        # Buttons Frame
        buttons_frame = Frame(master, bg="#2c3e50")
        buttons_frame.pack()

        # Start Button
        self.start_button = Button(buttons_frame, text="Start", command=self.start_virtual_mouse, bg="#3498db", fg="white")
        self.start_button.pack(side=LEFT, padx=10)

        # Stop Button
        self.stop_button = Button(buttons_frame, text="Stop", command=self.stop_virtual_mouse, bg="#e74c3c", fg="white")
        self.stop_button.pack(side=LEFT, padx=10)

        # Variable to track if the virtual mouse is running
        self.is_running = False

        # Copyright Label
        self.copyright_label = Label(master, text="© 2023 IPD Project | All Rights Reserved.", font=("Helvetica", 8), bg="#2c3e50", fg="white")
        self.copyright_label.pack(side=BOTTOM, anchor=CENTER)

    def start_virtual_mouse(self):
        if not self.is_running:
            self.is_running = True
            self.eye_control_thread = threading.Thread(target=self.eye_control)
            self.eye_control_thread.start()

    def stop_virtual_mouse(self):
        if self.is_running:
            self.is_running = False

    def eye_control(self):
        cam = cv2.VideoCapture(0)
        face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        screen_w, screen_h = pyautogui.size()

        while self.is_running:
            _, frame = cam.read()
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = face_mesh.process(rgb_frame)
            landmark_points = output.multi_face_landmarks
            frame_h, frame_w, _ = frame.shape

            if landmark_points:
                landmarks = landmark_points[0].landmark
                for id, landmark in enumerate(landmarks[474:478]):
                    x = int(landmark.x * frame_w)
                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 0))
                    if id == 1:
                        screen_x = screen_w * landmark.x
                        screen_y = screen_h * landmark.y
                        pyautogui.moveTo(screen_x, screen_y)

                left = [landmarks[145], landmarks[159]]
                for landmark in left:
                    x = int(landmark.x * frame_w)
                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 255))

                if abs(left[0].y - left[1].y) < 0.002:  # Adjust the sensitivity by changing the threshold
                    pyautogui.click()
                    pyautogui.sleep(1)

            cv2.imshow('Eye Controlled Mouse', frame)
            cv2.waitKey(1)

        # Release the camera when the loop is stopped
        cam.release()

# root = tk.Tk()
# VirtualMouseApp()
# mainloop()