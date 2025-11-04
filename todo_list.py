import tkinter as tk
from tkinter import messagebox
import os

# membuat window utama
root = tk.Tk()
root.title("To-Do List Sederhana")
root.geometry("400x400")

# nama file untuk menyimpan tugas
TASKS_FILE = "tasks.txt"

# daftar tugas disimpan di list Python
tasks = []

# Fungsi untuk memuat tugas dari file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
                    listbox_tasks.insert(tk.END, task)

# Fungsi untuk menyimpan tugas ke file
def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

# Fungsi untuk menambah tugas
def add_task():
    task = entry_task.get()
    if task != "":
        tasks.append(task)
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Peringatan", "Tugas tidak boleh kosong!")

# Fungsi untuk menghapus tugas
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
        tasks.pop(selected_task_index)
        save_tasks()
    except:
        messagebox.showwarning("Peringatan", "Pilih tugas yang ingin dihapus!")

# Fungsi untuk menghapus semua tugas
def clear_all():
    if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus semua tugas?"):
        listbox_tasks.delete(0, tk.END)
        tasks.clear()
        save_tasks()

# Judul
label_title = tk.Label(root, text="📝 To-Do List", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Input task
entry_task = tk.Entry(root, width=35)
entry_task.pack(pady=5)

# Tombol tambah tugas
button_add = tk.Button(root, text="Tambah Tugas", width=15, command=add_task)
button_add.pack(pady=5)

# Listbox untuk menampilkan tugas
listbox_tasks = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
listbox_tasks.pack(pady=10)

# Tombol hapus dan hapus semua
button_delete = tk.Button(root, text="Hapus Tugas", width=15, command=delete_task)
button_delete.pack(pady=3)

button_clear = tk.Button(root, text="Hapus Semua", width=15, command=clear_all)
button_clear.pack(pady=3)

# muat tugas saat aplikasi dibuka
load_tasks()

# jalankan GUI
root.mainloop()
