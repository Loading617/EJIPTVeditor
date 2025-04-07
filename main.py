import tkinter as tk  
import customtkinter
from CTkMenuBar import *
from tkinter import PhotoImage
from tkinter import filedialog, simpledialog
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

new_img = PhotoImage(file="icons/newiptvlist.png")
open_img = PhotoImage(file="icons/openfile.png")
url_img = PhotoImage(file="icons/openurl.png")
save_img = PhotoImage(file="icons/save.png")
exit_img = PhotoImage(file="icons/exit.png")

dropdown1 = CustomDropdownMenu(widget=button_1)
dropdown1.add_option(option="New List", command=lambda: print("New List"), image=new_img, compound="left")
dropdown1.add_option(option="Open List", command=lambda: print("Open List"), image=open_img, compound="left")
dropdown1.add_option(option="Open URL", command=lambda: print("Open URL"), image=url_img, compound="left")
dropdown1.add_separator()
dropdown1.add_option(option="Save As", command=lambda: print("Save As"), image=save_img, compound="left")
dropdown1.add_separator()
dropdown1.add_option(option="Exit", command=root.quit, image=exit_img, compound="left")

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

self.img1 = ctk.CTkImage(Image.open("icons/newiptvlist.png"), size=(20, 20))
self.img2 = ctk.CTkImage(Image.open("icons/openfile.png"), size=(20, 20))
self.img3 = ctk.CTkImage(Image.open("icons/openurl.png"), size=(20, 20))
self.img4 = ctk.CTKImage(Image.open("icons/save.png"), size=(20, 20))
self.img5 = ctk.CTKImage(Image.open("icons/exit.png"), size=(20, 20))

self.options = [
            ("New IPTV List", self.img1),
            ("Open File", self.img2),
            ("Open URL", self.img3),
            ("Save", self.img4),
            ("Exit", self.img5)
        ]

frame = customtkinter.CTkFrame(root, width=920, height=570, corner_radius=0)
frame.place(x=620, y=35)

label1 = customtkinter.CTkLabel(frame, text="Name:")
label1.place(x=10, y=10)
entry1 = customtkinter.CTkEntry(frame, width=280)
entry1.place(x=10, y=35)

label2 = customtkinter.CTkLabel(frame, text="Number of Channel:")
label2.place(x=10, y=75)
entry2 = customtkinter.CTkEntry(frame, width=280)
entry2.place(x=10, y=100)

label3 = customtkinter.CTkLabel(frame, text="Category:")
label3.place(x=10, y=140)
entry3 = customtkinter.CTkEntry(frame, width=280)
entry3.place(x=10, y=165)

label4 = customtkinter.CTkLabel(frame, text="URL Stream:")
label4.place(x=10, y=205)
entry4 = customtkinter.CTkEntry(frame, width=280)
entry4.place(x=10, y=230)

label5 = customtkinter.CTkLabel(frame, text="Logo:")
label5.place(x=10, y=270)
entry5 = customtkinter.CTkEntry(frame, width=280)
entry5.place(x=10, y=295)

label6 = customtkinter.CTkLabel(frame, text="EPG ID:")
label6.place(x=10, y=335)
entry6 = customtkinter.CTkEntry(frame, width=280)
entry6.place(x=10, y=360)

def create_toolbar(self):
        toolbar = ctk.CTkFrame(self)
        toolbar.pack(pady=10, padx=10, fill="x")

        buttons = [
            ("New IPTV List", self.new_iptv_list, "Ctrl-n"),
            ("Open File", self.open_file, "Ctrl-o"),
            ("Open URL", self.open_url, "Ctrl-u"),
            ("Save", self.save, "Ctrl-s"),
            ("Add Channel", self.add_channel, "Ctrl-a"),
            ("Delete Channel", self.delete_channel, "Delete"),
            ("Duplicate Channel", self.duplicate_channel, "Ctrl-d"),
            ("Copy Name to EPG", self.copy_name_to_epg, "Ctrl-e"),
            ("Clear Duplicate Hosts", self.clear_duplicates, "Ctrl-h"),
            ("Verify Links", self.verify_links, "Ctrl-v"),
            ("Delete Dead Links", self.delete_dead_links, "Ctrl-x"),
            ("Export Hosts", self.export_hosts, "Ctrl-p"),
        ]

        for text, command, _ in buttons:
            btn = ctk.CTkButton(toolbar, text=text, command=command)
            btn.pack(side="left", padx=5)

def bind_keys(self):
        bindings = {
            "<Control-n>": self.new_iptv_list,
            "<Control-o>": self.open_file,
            "<Control-u>": self.open_url,
            "<Control-s>": self.save,
            "<Control-a>": self.add_channel,
            "<Delete>": self.delete_channel,
            "<Control-d>": self.duplicate_channel,
            "<Control-e>": self.copy_name_to_epg,
            "<Control-h>": self.clear_duplicates,
            "<Control-v>": self.verify_links,
            "<Control-x>": self.delete_dead_links,
            "<Control-p>": self.export_hosts,
        }

        for key, func in bindings.items():
            self.bind(key, lambda event, f=func: f())

def new_iptv_list(self):
        print("New IPTV list created")

def open_file(self):
        file_path = filedialog.askopenfilename(title="Open IPTV File")
        print(f"Opened file: {file_path}")

def open_url(self):
        url = simpledialog.askstring("Open URL", "Enter IPTV URL:")
        if url:
            print(f"Opened URL: {url}")

def save(self):
        print("Saved IPTV list")

def add_channel(self):
        print("Channel added")

def delete_channel(self):
        print("Channel deleted")

def duplicate_channel(self):
        print("Channel duplicated")

def copy_name_to_epg(self):
        print("Copied name to EPG")

def clear_duplicates(self):
        print("Cleared duplicate hosts")

def verify_links(self):
        print("Verified links")

def delete_dead_links(self):
        print("Deleted dead links")

def export_hosts(self):
        print("Exported hosts for validation")

root.mainloop()
