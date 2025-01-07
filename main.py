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

newiptvlist_button = ctk.CTkButton(toolbar, text="New IPTV List", width=70, command=on_newiptvlist)
newiptvlist_button.pack(side=tk.LEFT, padx=2, pady=2)

openfile_button = ctk.CTkButton(toolbar, text="Open File", width=70, command=on_open_file)
openfile_button.pack(side=tk.LEFT, padx=2, pady=2)

openurl_button = ctk.CTkButton(toolbar, text="Open Url", width=70, command=on_open_url)
openurl_button.pack(side=tk.LEFT, padx=2, pady=2)

save_button = ctk.CTkButton(toolbar, text="Save", width=70, command=on_save)
save_button.pack(side=tk.LEFT, padx=2, pady=2)

addchannel_button = ctk.CTkButton(toolbar, text="Add Channel", width=70, command=on_add_channel)
addchannel_button.pack(side=tk.LEFT, padx=2, pady=2)

deletechannel_button = ctk.CTkButton(toolbar, text="Delete Channel", width=70, command=on_delete_channel)
deletechannel_button.pack(side=tk.LEFT, padx=2, pady=2)

duplicatechannel_button = ctk.CTkButton(toolbar, text="Duplicate Channel", width=70, command=on_duplicate_channel)
duplicatechannel_button.pack(side=tk.LEFT, padx=2, pady=2)

copynametoepg_button = ctk.CTkButton(toolbar, text="Copy Name to EPG", width=70, command=on_copy_name_to_epg)
copynametoepg_button.pack(side=tk.LEFT, padx=2, pady=2)

clearduplicatesofhosts_button = ctk.CTkButton(toolbar, text="Clear Duplicates of Hosts", width=70, command=on_clear_duplicates_of_hosts)
clearduplicatesofhosts_button.pack(side=tk.LEFT, padx=2, pady=2)

checklinks_button = ctk.CTkButton(toolbar, text="Check Links", width=70, command=on_checklinks)
checklinks_button.pack(side=tk.LEFT, padx=2, pady=2)

deletedeadlinks_button = ctk.CTkButton(toolbar, text="Delete Dead Links", width=70, command=on_deletedeadlinks)
deletedeadlinks_button.pack(side=tk.LEFT, padx=2, pady=2)

exporttohostsvalidation_button = ctk.CTkButton(toolbar, text="Exports to Hosts Validation", width=70, command=on_exports_to_hosts_validation)
exporttohostsvalidation_button = ctk.CTkButton(side=tk.LEFT, padx=2, pady=2)


new_icon = ImageTk.PhotoImage(Image.open("newlist.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=newlist, text="", width=30, command=on_newlist)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("open-file.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=open-file, text="", width=30, command=on_open_file)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("openurl.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=openurl, text="", width=30, command=on_openurl)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("save.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=save, text="", width=30, command=on_save)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("channeladd.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=channeladd, text="", width=30, command=on_add_channel)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("deletechannel.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=deletechannel, text="", width=30, command=on_deletechannel)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("duplicatechannel.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=duplicatechannel, text="", width=30, command=on_duplicatechannel)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("copynametoepg.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=copynametoepg, text="", width=30, command=on_copynametoepg)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("clearduplicatehosts.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=clearduplicatehosts, text="", width=30, command=on_clearduplicatehosts)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("checklinks.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=checklinks, text="", width=30, command=on_checklinks)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("deletedeadlinks.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=deletedeadlinks, text="", width=30, command=on_deletedeadlinks)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

new_icon = ImageTk.PhotoImage(Image.open("exporthostsvalidation.png").resize((20, 20)))
new_button = ctk.CTkButton(toolbar, image=, text="exporthostsvalidation", width=30, command=on_exporthosts_validation)
new_button.pack(side=tk.LEFT, padx=2, pady=2)

root.mainloop()
