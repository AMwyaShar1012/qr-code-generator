import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Function to generate the QR code
def generate_qr():
    data = data_entry.get()
    size = size_entry.get()
    
    # Validate input
    if not data.strip():
        messagebox.showerror("Error", "Data cannot be empty.")
        return
    
    try:
        width, height = map(int, size.split('x'))
        if width > 750 or height > 750 or width <= 0 or height <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid dimensions. Please enter in format 'widthxheight' (max 750x750).")
        return
    
    # Send GET request
    url = f'https://api.qrserver.com/v1/create-qr-code/?size={size}&data={data}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        
        # Save the QR code as a PNG image
        img.save('qrcode.png')
        
        qr_img = ImageTk.PhotoImage(img)
        
        qr_label.config(image=qr_img)
        qr_label.image = qr_img
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch QR code: {e}")

# Animation effect for buttons
def on_enter(e):
    e.widget.config(bg="#45aaf2", relief="raised")

def on_leave(e):
    e.widget.config(bg="#1e90ff", relief="flat")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")
root.config(bg="#f7f1e3")

# Header
header = tk.Label(root, text="QR Code Generator", font=("Helvetica", 20, "bold"), bg="#f7f1e3", fg="#1e90ff")
header.pack(pady=10)

# Data entry field
tk.Label(root, text="Enter Data:", font=("Helvetica", 14), bg="#f7f1e3").pack(pady=5)
data_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
data_entry.pack(pady=5)

# Size entry field
tk.Label(root, text="Enter Dimensions (e.g., 300x300):", font=("Helvetica", 14), bg="#f7f1e3").pack(pady=5)
size_entry = tk.Entry(root, font=("Helvetica", 14), width=15)
size_entry.insert(0, "150x150")
size_entry.pack(pady=5)

# Generate button
generate_btn = tk.Button(root, text="Generate QR Code", font=("Helvetica", 14, "bold"), bg="#1e90ff", fg="white", relief="flat", command=generate_qr)
generate_btn.pack(pady=20)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)

# QR code display area
qr_label = tk.Label(root, bg="#f7f1e3")
qr_label.pack(pady=10)

# Run the app
root.mainloop()
