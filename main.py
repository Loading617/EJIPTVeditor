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
dropdown1.add_option(option="Open List")
dropdown1.add_option(option="Open URL")
dropdown1.add_separator()
dropdown1.add_option(option="Save As")
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

frame_width = 280
frame_height = 960

frame = customtkinter.CTkFrame(root, width=frame_width, height=frame_height, corner_radius=0)
frame.place(x=950 - frame_width, y=51)

fields = ["Name", "Number of Channel", "Category", "URL Stream", "Logo", "EPG ID"]

for field in fields:
    label = customtkinter.CTkLabel(frame, text=f"{field}:", font=("Akzidenz Grotesk", 14))
    label.pack(pady=10, anchor="w")

    entry = customtkinter.CTkEntry(frame, width=250)
    entry.pack(pady=5)

root.mainloop()
