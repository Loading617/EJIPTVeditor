import tkinter as tk
from tkinter import filedialog

class IPTVEditor:
 def init(self, root):
self.root = root
self.root.title('EJ IPTV Editor')
self.playlist = []

    # Create GUI components
self.file_label = tk.Label(self.root, text='Select IPTV Playlist:')
self.file_label.pack(padx=10, pady=10)

self.file_entry = tk.Entry(self.root, width=50)
self.file_entry.pack(padx=10, pady=10)

self.browse_button = tk.Button(self.root, text='Browse', command=self.browse_file)
self.browse_button.pack(padx=10, pady=10)

self.add_button = tk.Button(self.root, text='Add Channel', command=self.add_channel)
self.add_button.pack(padx=10, pady=10)

self.save_button = tk.Button(self.root, text='Save Playlist', command=self.save_playlist)
self.save_button.pack(padx=10, pady=10)

def browse_file(self):
    file_path = filedialog.askopenfilename(title='Select IPTV Playlist', filetypes=[('M3U8 Files', '*.m3u8')])
    self.file_entry.delete(0, tk.END)
    self.file_entry.insert(0, file_path)

def add_channel(self):
    channel_name = input('Enter channel name: ')
    channel_url = input('Enter channel URL: ')
    self.playlist.append({'name': channel_name, 'url': channel_url})

def save_playlist(self):
    file_path = self.file_entry.get()
    with open(file_path, 'w') as f:
        for channel in self.playlist:
            f.write(f'#EXTINF:-1,{channel["name"]}\n{channel["url"]}\n')

if name == 'main':
root = (link unavailable)()
iptv_editor = IPTVEditor(root)
root.mainloop()