import requests
import tkinter as tk
from tkinter import filedialog, messagebox

SERVER_URL = "http://127.0.0.1:5000/upload"  # Замінити на IP сервера


def upload_photo():
    file_path = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return

    try:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(SERVER_URL, files=files)

        result = response.json()
        if "file_url" in result:
            messagebox.showinfo("Успіх", f"Фото завантажено!\nURL: {result['file_url']}")
        else:
            messagebox.showerror("Помилка", result.get("error", "Невідома помилка"))
    except Exception as e:
        messagebox.showerror("Помилка", str(e))


# Інтерфейс
root = tk.Tk()
root.title("Завантаження фото")

btn_upload = tk.Button(root, text="Вибрати та завантажити фото", command=upload_photo)
btn_upload.pack(pady=20)

root.mainloop()
