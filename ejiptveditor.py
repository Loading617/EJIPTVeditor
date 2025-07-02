import tkinter as tk
import customtkinter as CTk
import os
from PIL import Image, ImageDraw
from CTkMenuBar import *
from tkinter import PhotoImage
import pywinstyles
from tkinter import filedialog, simpledialog

def new_list_action():
    print("Action: New List (Ctrl+N)")

def open_file_action():
    print("Action: Open List (Ctrl+O)")

def open_url_action():
    print("Action: Open URL (Ctrl+U)")

def save_file_action():
    print("Action: Save As (Ctrl+S)")

def exit_app_action():
    print("Action: Exiting Application (Ctrl+Q)")
    root.quit()

def add_channel_action():
    print("Action: Add Channel (Ctrl+A)")

def delete_channel_action():
    print("Action: Delete Channel (Delete Key)")

def duplicate_channel_action():
    print("Action: Duplicate Channel (Ctrl+D)")

def copy_name_to_epg_action():
    print("Action: Copy Name to EPG (Ctrl+E)")

def clear_duplicates_action():
    print("Action: Clear Duplicates (Ctrl+Shift+C)")

def verify_links_action():
    print("Action: Verify Links (Ctrl+V)")

def delete_dead_links_action():
    print("Action: Delete Dead Links (Ctrl+Shift+D)")

def export_hosts_action():
    print("Action: Export Hosts (Ctrl+H)")

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
about_img = PhotoImage(file="icons/info.png").subsample(5, 5)

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
dropdown6.add_option(option="Info", command=lambda: print("Info"), image=about_img, compound="left")

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

toolbar_frame = CTk.CTkFrame(root, height=50, corner_radius=0)
toolbar_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

toolbar_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=0)
toolbar_frame.grid_columnconfigure(12, weight=1)

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")

new_iptv_list_image = None
open_file_image = None
open_url_image = None
save_image = None
add_channel_image = None
delete_channel_image = None
duplicate_channel_image = None
copy_name_to_epg_image = None
clear_duplicates_image = None
verify_links_image = None
delete_dead_links_image = None
export_hosts_image = None

try:
    new_iptv_list_image = PhotoImage(file=os.path.join(image_path, "newiptvlist.png")).subsample(3, 3)
    open_file_image = PhotoImage(file=os.path.join(image_path, "openfile.png")).subsample(3, 3)
    open_url_image = PhotoImage(file=os.path.join(image_path, "openurl.png")).subsample(3, 3)
    save_image = PhotoImage(file=os.path.join(image_path, "save.png")).subsample(3, 3)
    add_channel_image = PhotoImage(file=os.path.join(image_path, "addchannel.png")).subsample(3, 3)
    delete_channel_image = PhotoImage(file=os.path.join(image_path, "deletechannel.png")).subsample(3, 3)
    duplicate_channel_image = PhotoImage(file=os.path.join(image_path, "duplicatechannel.png")).subsample(3, 3)
    copy_name_to_epg_image = PhotoImage(file=os.path.join(image_path, "copynametoepg.png")).subsample(3, 3)
    clear_duplicates_image = PhotoImage(file=os.path.join(image_path, "clearduplicates.png")).subsample(3, 3)
    verify_links_image = PhotoImage(file=os.path.join(image_path, "verifylinks.png")).subsample(3, 3)
    delete_dead_links_image = PhotoImage(file=os.path.join(image_path, "deletedeadlinks.png")).subsample(3, 3)
    export_hosts_image = PhotoImage(file=os.path.join(image_path, "exporthosts.png")).subsample(3, 3)
except Exception as e:
    print(f"Error loading images: {e}")


new_iptv_list_button = CTk.CTkButton(toolbar_frame, image=new_iptv_list_image,
                                      compound="left", command=new_list_action,
                                      width=80, height=30, corner_radius=5, text="New")
new_iptv_list_button.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")

open_file_button = CTk.CTkButton(toolbar_frame, image=open_file_image,
                                  compound="left", command=open_file_action,
                                  width=80, height=30, corner_radius=5, text="Open")
open_file_button.grid(row=0, column=1, padx=5, pady=5, sticky="w")

open_url_button = CTk.CTkButton(toolbar_frame, image=open_url_image,
                                 compound="left", command=open_url_action,
                                 width=80, height=30, corner_radius=5, text="URL")
open_url_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")

save_button = CTk.CTkButton(toolbar_frame, image=save_image,
                            compound="left", command=save_file_action,
                            width=80, height=30, corner_radius=5, text="Save")
save_button.grid(row=0, column=3, padx=5, pady=5, sticky="w")

add_channel_button = CTk.CTkButton(toolbar_frame, image=add_channel_image,
                                   compound="left", command=add_channel_action,
                                   width=80, height=30, corner_radius=5, text="Add")
add_channel_button.grid(row=0, column=4, padx=5, pady=5, sticky="w")

delete_channel_button = CTk.CTkButton(toolbar_frame, image=delete_channel_image,
                                      compound="left", command=delete_channel_action,
                                      width=80, height=30, corner_radius=5, text="Delete")
delete_channel_button.grid(row=0, column=5, padx=5, pady=5, sticky="w")

duplicate_channel_button = CTk.CTkButton(toolbar_frame, image=duplicate_channel_image,
                                         compound="left", command=duplicate_channel_action,
                                         width=80, height=30, corner_radius=5, text="Duplicate")
duplicate_channel_button.grid(row=0, column=6, padx=5, pady=5, sticky="w")

copy_name_to_epg_button = CTk.CTkButton(toolbar_frame, image=copy_name_to_epg_image,
                                         compound="left", command=copy_name_to_epg_action,
                                         width=80, height=30, corner_radius=5, text="Copy EPG")
copy_name_to_epg_button.grid(row=0, column=7, padx=5, pady=5, sticky="w")

clear_duplicates_button = CTk.CTkButton(toolbar_frame, image=clear_duplicates_image,
                                         compound="left", command=clear_duplicates_action,
                                         width=80, height=30, corner_radius=5, text="Clear Dups")
clear_duplicates_button.grid(row=0, column=8, padx=5, pady=5, sticky="w")

verify_links_button = CTk.CTkButton(toolbar_frame, image=verify_links_image,
                                         compound="left", command=verify_links_action,
                                         width=80, height=30, corner_radius=5, text="Verify Links")
verify_links_button.grid(row=0, column=9, padx=5, pady=5, sticky="w")

delete_dead_links_button = CTk.CTkButton(toolbar_frame, image=delete_dead_links_image,
                                         compound="left", command=delete_dead_links_action,
                                         width=80, height=30, corner_radius=5, text="Del Dead")
delete_dead_links_button.grid(row=0, column=10, padx=5, pady=5, sticky="w")

export_hosts_button = CTk.CTkButton(toolbar_frame, image=export_hosts_image,
                                         compound="left", command=export_hosts_action,
                                         width=80, height=30, corner_radius=5, text="Export Hosts")
export_hosts_button.grid(row=0, column=11, padx=5, pady=5, sticky="w")

root.bind("<Control-n>", lambda event: new_list_action())
root.bind("<Control-o>", lambda event: open_file_action())
root.bind("<Control-u>", lambda event: open_url_action())
root.bind("<Control-s>", lambda event: save_file_action())
root.bind("<Control-q>", lambda event: exit_app_action())

root.bind("<Control-a>", lambda event: add_channel_action())
root.bind("<Delete>", lambda event: delete_channel_action())
root.bind("<Control-d>", lambda event: duplicate_channel_action())
root.bind("<Control-e>", lambda event: copy_name_to_epg_action())
root.bind("<Control-Shift-c>", lambda event: clear_duplicates_action())
root.bind("<Control-v>", lambda event: verify_links_action())
root.bind("<Control-Shift-d>", lambda event: delete_dead_links_action())
root.bind("<Control-h>", lambda event: export_hosts_action())

frame = CTk.CTkFrame(root, width=920, height=570, corner_radius=0)
frame.place(x=620, y=52)

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


root.mainloop()
