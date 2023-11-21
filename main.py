from tkinter import *
from ttkthemes import ThemedStyle
import mousecontrol as ms
import handcontrol as hd

root = Tk()
root.config(bg="#394240") 
style = ThemedStyle(root)
style.theme_use('clam')

root.geometry("700x500")
root.title("IPD-2023 | Gurmehar and Amanpreet")

heading_label = Label(root, text="IPD-2023 | Gurmehar and Amanpreet", font=('Helvetica', 14, 'bold'), bg="#1E2B2E", fg="white", padx=10, pady=5)
heading_label.place(relx=0.5, rely=0.1, anchor=CENTER)

description_label = Label(root, text="Mouse control without actually using the mouse", font=('Helvetica', 10), bg="#394240", fg="white")
description_label.place(relx=0.5, rely=0.2, anchor=CENTER)

button_bg_color = "#61C0BF"

eys_control_button = Button(root, text="Eyes Control", width=15, bd='2', command=ms.VirtualMouseApp, bg=button_bg_color)
eys_control_button.place(relx=0.35, rely=0.5, anchor=CENTER)

hand_control_button = Button(root, text="Hand Control", width=15, bd='2', command=lambda: hd.GestureController(root), bg=button_bg_color)
hand_control_button.place(relx=0.65, rely=0.5, anchor=CENTER)

copyright_label = Label(root, text="© 2023 IPD Project | All Rights Reserved.", font=('Helvetica', 8), bg="#394240", fg="white")
copyright_label.place(relx=0.5, rely=0.95, anchor=CENTER)

mainloop()