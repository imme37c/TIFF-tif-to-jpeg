import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import webbrowser

url = "https://i.postimg.cc/3wjK1PqL/gaga.png"

def convert_to_jpeg():
    file_paths = filedialog.askopenfilenames(
        title="Select TIFF/TIF files",
        filetypes=[("TIFF files", "*.tif *.tiff")]
    )
    
    if not file_paths:
        return
    
    saved_files = []  
    
    for file_path in file_paths:
        try:
            
            img = Image.open(file_path)
            
            base = os.path.splitext(file_path)[0]
            output_path = f"{base}.jpeg"
            
            img.convert("RGB").save(output_path, "JPEG")
            saved_files.append(output_path)
            print(f"converted: {file_path} -> {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not convert {file_path}.\n{e}")
    
    if saved_files:
        saved_files_str = "\n".join(saved_files)
        messagebox.showinfo("Klaar", f"All selected file(s) are converted to JPEG:\n{saved_files_str}")
        webbrowser.open(url)



root = tk.Tk()
root.title("TIFF to JPEG Converter")
root.geometry("300x150")

label = tk.Label(root, text="Click the button to convert TIFF/TIF to JPEG")
label.pack(pady=20)

convert_button = tk.Button(root, text="Select TIFF/TIF files", command=convert_to_jpeg)
convert_button.pack(pady=10)

root.mainloop()
