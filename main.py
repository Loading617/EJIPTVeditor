import customtkinter as ctk
from CTkMenuBar import CTkMenuBar

root = ctk.CTk()
root.title("EJ IPTV Editor")

menubar = CTkMenuBar(root)
menubar.pack(side="top", fill="x")

file_menu = menubar.add_menu("File")
file_menu.add_command(label="New List", command=lambda: print("New"))
file_menu.add_command(label="Open List", command=lambda: print("Open"))
file_menu.add_command(label="Open URL", command=lambda: print("Open URL"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=lambda: (print("Exit"), root.quit()))

import_menu = menubar.add_menu("Import")
import_menu.add_command(label="Import Kodi IPTV List", command=lambda: print("Import Kodi"))
import_menu.add_command(label="Import Simple IPTV List", command=lambda: print("Import Simple"))

export_menu = menubar.add_menu("Export")
export_menu.add_command(label="Export Kodi IPTV List", command=lambda: print("Export Kodi"))
export_menu.add_command(label="Export Simple IPTV List", command=lambda: print("Export Simple"))

about_menu = menubar.add_menu("About")
about_menu.add_command(label="About EJ IPTV Editor", command=lambda: print("About"))

help_menu = menubar.add_menu("Help")
help_menu.add_command(label="How to", command=lambda: print("How to"))

root.geometry("920x570")

root.mainloop()
