import os
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video(url, format_choice, download_folder):
    ydl_opts = {}

    if format_choice == "mp4":
        ydl_opts = {
            'format': 'bestvideo+bestaudio',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        }
    elif format_choice == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        }
    else:
        messagebox.showerror("Error", "Formato no soportado.")
        return

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Éxito", f"Descarga completada en: {download_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al descargar: {e}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        download_folder.set(folder_selected)

def start_download():
    url = url_entry.get().strip()
    format_choice = format_var.get()
    folder = download_folder.get()

    if not url:
        messagebox.showerror("Error", "Por favor, ingrese una URL.")
        return

    if not folder:
        messagebox.showerror("Error", "Por favor, seleccione una carpeta de destino.")
        return

    download_video(url, format_choice, folder)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("YouTube Downloader")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Campo de URL
url_label = tk.Label(frame, text="URL del video de YouTube:")
url_label.grid(row=0, column=0, sticky="w")
url_entry = tk.Entry(frame, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Opciones de formato
format_label = tk.Label(frame, text="Formato de descarga:")
format_label.grid(row=1, column=0, sticky="w")
format_var = tk.StringVar(value="mp4")
mp4_radio = tk.Radiobutton(frame, text="MP4", variable=format_var, value="mp4")
mp4_radio.grid(row=1, column=1, sticky="w")
mp3_radio = tk.Radiobutton(frame, text="MP3", variable=format_var, value="mp3")
mp3_radio.grid(row=2, column=1, sticky="w")

# Selección de carpeta de destino
folder_label = tk.Label(frame, text="Carpeta de destino:")
folder_label.grid(row=3, column=0, sticky="w")
download_folder = tk.StringVar()
folder_entry = tk.Entry(frame, textvariable=download_folder, width=40)
folder_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
browse_button = tk.Button(frame, text="Examinar", command=browse_folder)
browse_button.grid(row=3, column=2, padx=5, pady=5)

# Botón de descarga
download_button = tk.Button(frame, text="Descargar", command=start_download)
download_button.grid(row=4, column=1, pady=10)

root.mainloop()
