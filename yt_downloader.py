import os
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

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
    format_choice = format_var.get()  # Obtenemos el valor seleccionado
    folder = download_folder.get()

    if not url:
        messagebox.showerror("Error", "Por favor, ingrese una URL.")
        return

    if not folder:
        messagebox.showerror("Error", "Por favor, seleccione una carpeta de destino.")
        return

    download_video(url, format_choice, folder)

# Configuración
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("600x200")  
root.resizable(False, False)  
root.config(bg="#f7f7f7") 

# Estilo de fuente
font_style = ('Helvetica Neue', 12)

frame = tk.Frame(root, padx=10, pady=10, bg="#f7f7f7")
frame.pack(padx=15, pady=10, fill="both", expand=True)  

# Reajuste de la ventana
frame.grid_columnconfigure(0, weight=0)  
frame.grid_columnconfigure(1, weight=1)  
frame.grid_columnconfigure(2, weight=0)  

frame.grid_rowconfigure(0, weight=0) 
frame.grid_rowconfigure(1, weight=0) 
frame.grid_rowconfigure(2, weight=0)  
frame.grid_rowconfigure(3, weight=0)  

# Campo URL
url_label = tk.Label(frame, text="URL del video de YouTube:", font=font_style, bg="#f7f7f7")
url_label.grid(row=0, column=0, sticky="w", pady=3)
url_entry = ttk.Entry(frame, width=40, font=font_style)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Opciones de formato en Combobox
format_label = tk.Label(frame, text="Formato de descarga:", font=font_style, bg="#f7f7f7")
format_label.grid(row=1, column=0, sticky="w", pady=3)

format_var = tk.StringVar(root, value="mp4")  # Valor por defecto en el StringVar
format_options = ["mp4", "mp3"]  

# Cambiar OptionMenu por un Combobox para mostrar ambas opciones
format_menu = ttk.Combobox(frame, textvariable=format_var, values=format_options, state="readonly", width=10)
format_menu.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Estilo para quitar el subrayado y el borde
style = ttk.Style()
style.configure("TCombobox", 
                fieldbackground="#f7f7f7",  
                background="#f7f7f7",       
                relief="flat",            
                padding=5)                 

# Aplicamos el estilo al Combobox
format_menu.configure(style="TCombobox")

# Carpeta de destino
folder_label = tk.Label(frame, text="Carpeta de destino:", font=font_style, bg="#f7f7f7")
folder_label.grid(row=2, column=0, sticky="w", pady=3)
download_folder = tk.StringVar()
folder_entry = ttk.Entry(frame, textvariable=download_folder, width=35, font=font_style)
folder_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

browse_button = tk.Button(frame, text="Examinar", command=browse_folder)
browse_button.grid(row=2, column=2, padx=5, pady=5)

# Botón de descarga
download_button = tk.Button(frame, text="Descargar", command=start_download, relief="flat", bg="#34b7f1", fg="white", font=font_style)
download_button.grid(row=3, column=1, pady=10)

root.mainloop()
