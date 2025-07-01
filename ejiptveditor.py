import tkinter as tk
import customtkinter as CTk
import os
from PIL import Image, ImageDraw
from CTkMenuBar import *
from tkinter import PhotoImage
import pywinstyles
from tkinter import filedialog, simpledialog

from PIL import Image

root = CTk.CTk()
pywinstyles.apply_style(root, "acrylic")
root.geometry("920x570")
root.title("EJ IPTV editor")

menu = CTkTitleMenu(root)
button_1 = menu.add_cascade("File")
button_2 = menu.add_cascade("Import")
button_3 = menu.add_cascade("Export")
button_4 = menu.add_cascade("Preferences")
button_5 = menu.add_cascade("Help")
button_6 = menu.add_cascade("About")

new_img = PhotoImage(file="icons/newiptvlist.png").subsample(5, 5)
open_img = PhotoImage(file="icons/openfile.png").subsample(5, 5)
url_img = PhotoImage(file="icons/openurl.png").subsample(5, 5)
save_img = PhotoImage(file="icons/save.png").subsample(5, 5)
exit_img = PhotoImage(file="icons/exit.png").subsample(5, 5)

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

about_img = PhotoImage(file="icons/info.png").subsample(5, 5)

dropdown6 = CustomDropdownMenu(widget=button_6)
dropdown6.add_option(option="Info", command=lambda: print("Info"), image=about_img, compound="left")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

toolbar_frame = ctk.CTKFrame(app, height=50, corner_radius=0)
toolbar_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
toolbar_frame.grid_columnconfigure((0, 1, 2, 3), weight=0)
toolbar_frame.grid_columnconfigure(4, weight=1)

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
new_iptv_list_image, open_file_image, open_url_image, save_image, add_channel_image, delete_channel_image, duplicate_channel_image, copy_name_to_epg_image, clear_duplicates_image, verify_links_image, delete_dead_links_image, export_hosts_image = None, None, None, None, None, None, None, None, None, None, None, None

try:
                new_iptv_list_image = PhotoImage(file=os.path.join(image_path, "newiptvlist.png"))
                open_file_image = PhotoImage(file=os.path.join(image_path, "openfile.png"))
                open_url_image = PhotoImage(file=os.path.join(image_path, "openurl.png"))
                save_image = PhotoImage(file=os.path.join(image_path, "save.png"))
                add_channel_image = PhotoImage(file=os.path.join(image_path, "addchannel.png"))
                delete_channel_image = PhotoImage(file=os.path.join(image_path, "deletechannel.png"))
                duplicate_channel_image = PhotoImage(file=os.path.join(image_path, "duplicatechannel.png"))
                copy_name_to_epg_image = PhotoImage(file=os.path.join(image_path, "copynametoepg.png"))
                clear_duplicates_image = PhotoImage(file=os.path.join(image_path, "clearduplicates.png"))
                verify_links_image = PhotoImage(file=os.path.join(image_path, "verifylinks.png"))
                delete_dead_links_image = PhotoImage(file=os.path.join(image_path, "deletedeadlinks.png"))
                export_hosts_image = PhotoImage(file=os.path.join(image_path, "exporthosts.png"))

new_iptv_list_button = ctk.CTkButton(toolbar_frame, image=new_iptv_list_image,
                                     compound="left", command=lambda: new_iptv_list(new_iptv_list),
                                     width=80, height=30, corner_radius=5)
new_iptv_list_button.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")

open_file_button = ctk.CTkButton(toolbar_frame, image=open_file_image,
                                 compound="left", command=lambda: open_file(open_file),
                                 width=80, height=30, corner_radius=5)
open_file_button.grid(row=0, column=1, padx=5, pady=5 sticky="w")

open_url_button = ctk.CTkButton(toolbar_frame, image=open_url_image,
                                compound="left", command=lambda: open_url(open_url),
                                width=80, height=30, corner_radius=5)
open_url_button.grid(row=0, column=2, padx=5, pady=5 sticky="w")

save_button = ctk.CTkButton(toolbar_frame, image=save_img,
                            compound="left", command=lambda: save_file(save_file),
                            width=80, height=30, corner_radius=5)
save_button.grid(row=0, column=3, padx=5, pady=5 sticky="w")

add_channel_button = ctk.CTkButton(toolbar_frame, image=add_channel_image,
                                   compound="left", command=lambda: add_channel(add_channel),
                                   width=80, height=30, corner_radius=5)
add_channel_button.grid(row=0, column=4, padx=5, pady=5 sticky="w")

delete_channel_button = ctk.CTkButton(toolbar_frame, image=delete_channel_image,
                                      compound="left", command=lambda: delete_channel(delete_channel),
                                      width=80, height=30, corner_radius=5)
delete_channel_button.grid(row=0, column=5, padx=5, pady=5 sticky="w")

duplicate_channel_button = ctk.CTkButton(toolbar_frame, image=duplicate_channel_image,
                                         compound="left", command=lambda: duplicate_channel(duplicate_channel),
                                         width=80, height=30, corner_radius=5)
duplicate_channel_button.grid(row=0, column=6, padx=5, pady=5 sticky="w")

copy_name_to_epg_button = ctk.CTkButton(toolbar_frame, image=copy_name_to_epg_image,
                                         compound="left", command=lambda: copy_name_to_epg(copy_name_to_epg),
                                         width=80, height=30, corner_radius=5)
copy_name_to_epg_button.grid(row=0, column=7, padx=5, pady=5 sticky="w")

clear_duplicates_button = ctk.CTkButton(toolbar_frame, image=clear_duplicates_image,
                                         compound="left", command=lambda: clear_duplicates(clear_duplicates),
                                         width=80, height=30, corner_radius=5)
clear_duplicates_button.grid(row=0, column=8, padx=5, pady=5 sticky="w")

verify_links_button = ctk.CTkButton(toolbar_frame, image=verify_links_image,
                                         compound="left", command=lambda: verify_links(verify_links),
                                         width=80, height=30, corner_radius=5)
verify_links_button.grid(row=0, column=9, padx=5, pady=5 sticky="w")

delete_dead_links_button = ctk.CTkButton(toolbar_frame, image=delete_dead_links_image,
                                         compound="left", command=lambda: delete_dead_links(delete_dead_links),
                                         width=80, height=30, corner_radius=5)
delete_dead_links_button.grid(row=0, column=10, padx=5, pady=5 sticky="w")

export_hosts_button = ctk.CTkButton(toolbar_frame, image=export_hosts_image,
                                         compound="left", command=lambda: export_hosts(export_hosts),
                                         width=80, height=30, corner_radius=5)
export_hosts_button.grid(row=0, column=11, padx=5, pady=5 sticky="w")

frame = CTk.CTkFrame(root, width=920, height=570, corner_radius=0)
frame.place(x=620, y=35)

label1 = CTk.CTkLabel(frame, text="Name:")
label1.place(x=10, y=10)
entry1 = CTk.CTkEntry(frame, width=280)
entry1.place(x=10, y=35)

label2 = CTk.CTkLabel(frame, text="Number of Channel:")
label2.place(x=10, y=75)
entry2 = CTk.CTkEntry(frame, width=280)
entry2.place(x=10, y=100)

label3 = CTk.CTkLabel(frame, text="Category:")
label3.place(x=10, y=140)
entry3 = CTk.CTkEntry(frame, width=280)
entry3.place(x=10, y=165)

label4 = CTk.CTkLabel(frame, text="URL Stream:")
label4.place(x=10, y=205)
entry4 = CTk.CTkEntry(frame, width=280)
entry4.place(x=10, y=230)

label5 = CTk.CTkLabel(frame, text="Logo:")
label5.place(x=10, y=270)
entry5 = CTk.CTkEntry(frame, width=280)
entry5.place(x=10, y=295)

label6 = CTk.CTkLabel(frame, text="EPG ID:")
label6.place(x=10, y=335)
entry6 = CTk.CTkEntry(frame, width=280)
entry6.place(x=10, y=360)

def create_toolbar(self):
        toolbar = CTk.CTkFrame(self)
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
            btn = CTk.CTkButton(toolbar, text=text, command=command)
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
