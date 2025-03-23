import tkinter as tk  
import customtkinter
from CTkMenuBar import *
from PIL import Image, ImageTk

root = customtkinter.CTk()
root.geometry("920x570")
root.title("EJ IPTV editor")

menu = CTkTitleMenu(root)
button_1 = menu.add_cascade("File")
button_2 = menu.add_cascade("Import")
button_3 = menu.add_cascade("Export")
button_4 = menu.add_cascade("Preferences")
button_5 = menu.add_cascade("Help")
button_6 = menu.add_cascade("About")

dropdown1 = CustomDropdownMenu(widget=button_1)
dropdown1.add_option(option="New List", command=lambda: print("New List"))
dropdown1.add_option(option="Open List", command=lambda: print("Open List"))
dropdown1.add_option(option="Open URL", command=lambda: print("Open URL"))
dropdown1.add_separator()
dropdown1.add_option(option="Save As", command=lambda: print("Save As"))
dropdown1.add_separator()
dropdown1.add_option(option="Exit", command=root.quit)

dropdown2 = CustomDropdownMenu(widget=button_2)
dropdown2.add_option(option="Import Kodi IPTV List")
dropdown2.add_option(option="Import Simple IPTV List")

dropdown3 = CustomDropdownMenu(widget=button_3)
dropdown3.add_option(option="Export Kodi IPTV List")
dropdown3.add_option(option="Export Simple IPTV List")

dropdown4 = CustomDropdownMenu(widget=button_4)
dropdown4.add_option(option="Report Duplicates")

dropdown5 = CustomDropdownMenu(widget=button_5)
dropdown5.add_option(option="Documentation(How To)")

dropdown6 = CustomDropdownMenu(widget=button_6)
dropdown6.add_option(option="Info")

frame = customtkinter.CTkFrame(root, width=920, height=570, corner_radius=0)
frame.place(x=620, y=35)

label1 = customtkinter.CTkLabel(frame, text="Name:")
label1.place(x=10, y=10)
entry1 = customtkinter.CTkEntry(frame, width=200)
entry1.place(x=10, y=35)

label2 = customtkinter.CTkLabel(frame, text="Number of Channel:")
label2.place(x=10, y=75)
entry2 = customtkinter.CTkEntry(frame, width=200)
entry2.place(x=10, y=100)

label3 = customtkinter.CTkLabel(frame, text="Category:")
label3.place(x=10, y=140)
entry3 = customtkinter.CTkEntry(frame, width=200)
entry3.place(x=10, y=165)

label4 = customtkinter.CTkLabel(frame, text="URL Stream:")
label4.place(x=10, y=205)
entry4 = customtkinter.CTkEntry(frame, width=200)
entry4.place(x=10, y=230)

label5 = customtkinter.CTkLabel(frame, text="Logo:")
label5.place(x=10, y=270)
entry5 = customtkinter.CTkEntry(frame, width=200)
entry5.place(x=10, y=295)

label6 = customtkinter.CTkLabel(frame, text="EPG ID:")
label6.place(x=10, y=335)
entry6 = customtkinter.CTkEntry(frame, width=200)
entry6.place(x=10, y=360)

root.mainloop()
