import customtkinter as ctk
from CTkMenuBar import CTkMenuBar

root = ctk.CTk()
root.title("EJ IPTV Editor")

menubar = CTkMenuBar(root)
menubar.pack(side="top", fill="x")

file_menu = ctk.CTkMenu(root)
file_menu.add_command(label="New List", command=lambda: print("New"))
file_menu.add_command(label="Open List", command=lambda: print("Open"))
file_menu.add_command(label="Open URL", command=lambda: print("Open URL"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=lambda: (print("Exit"), root.quit()))

menubar.add_cascade(label="File", menu=file_menu)

import_menu = ctk.CTkMenu(root)
import_menu.add_command(label="Import Kodi IPTV List", command=lambda: print("Import Kodi"))
import_menu.add_command(label="Import Simple IPTV List", command=lambda: print("Import Simple"))
menubar.add_cascade(label="Import", menu=import_menu)

export_menu = ctk.CTkMenu(root)
export_menu.add_command(label="Export Kodi IPTV List", command=lambda: print("Export Kodi"))
export_menu.add_command(label="Export Simple IPTV List", command=lambda: print("Export Simple"))
menubar.add_cascade(label="Export", menu=export_menu)

about_menu = ctk.CTkMenu(root)
about_menu.add_command(label="About EJ IPTV Editor", command=lambda: print("About"))
menubar.add_cascade(label="About", menu=about_menu)

help_menu = ctk.CTkMenu(root)
help_menu.add_command(label="How to", command=lambda: print("How to"))
menubar.add_cascade(label="Help", menu=help_menu)

root.geometry("920x570")

root.mainloop()
