import customtkinter as ctk
from CTkMenuBar import CTkMenuBar

root = ctk.CTk()
root.title("EJ IPTV editor")

menubar = CTkMenuBar(root)
menubar.pack(side="top", fill="x")

file_menu = menubar.add_cascade("File")
file_menu.add_command(label="New List", command=lambda: print("New"))
file_menu.add_command(label="Open List", command=lambda: print("Open"))
file_menu.add_command(label="Open URL", command=lambda: print("Open"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit, print("Exit"))

import_menu = menubar.add_cascade("Import")
import_menu.add_command(label="Import Kodi IPTV List", command=lambda: print("Import"))
import_menu.add_command(label="Import Simple IPTV List", command=lambda: print("Import"))

export_menu = menubar.add_cascade("Export")
export_menu.add_command(label="Export Kodi IPTV List", command=lambda: print("Export"))
export_menu.add_command(label="Export Simple IPTV List", command=lambda: print("Export"))

about_menu = menubar.add_cascade("About")
about_menu.add_command(label="About EJ IPTV Editor", command=lambda: print("About"))

help_menu = menubar.add_cascade("Help")
help_menu.add_command(label="How to", command=lambda: print("How to"))

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Import", menu=import_menu)
menubar.add_cascade(label="Export", menu=export_menu)
menubar.add_cascade(label="About", menu=about_menu)
menubar.add_cascade(label="Help", menu=help_menu)

root.geometry("920x570")

root.mainloop()
