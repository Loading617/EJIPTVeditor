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

def on_new_iptv_list():
    print("New List created")
    
def open_file():
    print("File opened")
    
def open_url():
    print("URL opened")
    
def save_as():
    print("Save As")
    
def add_new_channel():
    print("Channel added")
    
def delete_channel():
    print("Channel deleted")
    
def duplicate_channel():
    print("Channel duplicated")
    
def copy_name_to_epg():
    print("EPG copied to name")
    
def clear_duplicates_of_hosts():
    print("Duplicates of hosts removed")
    
def check_links():
    print("Links checked")
    
def delete_dead_links():
    print("Dead links deleted")
    
def exports_to_hosts_validation():
    print("Validations to hosts exported")
    
toolbar = tk.frame(app, bg="#333333", height=30)
toolbar.pack(side=tk.TOP, fill=tk.x)

new_button = ctk.CTkButton(toolbar, text="New", width=70, command=on_new)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

open_button = ctk.CTkButton(toolbar, text="Open", width=70, command=on_open)
open_button.pack(side=tk.LEFT, padx=2, pady=2)

save_button = ctk.CTkButton(toolbar, text="Save", width=70, command=on_save)
save_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("newlist.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=newlist, text="", width=30, command=on_new)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("open-file.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=open-file, text="", width=30, command=on_new)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("saveas.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=saveas, text="", width=30, command=on_new)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

root.mainloop()
