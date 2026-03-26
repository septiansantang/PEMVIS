# ==========================================
# Nama  : Septian Dwi Saputra
# NIM   : F1D022160
# Kelas : D
# ==========================================

import customtkinter as ctk
from tkinter import messagebox


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

def tampilkan():
    nama = entry_nama.get()
    nim = entry_nim.get()
    kelas = entry_kelas.get()
    jk = combo_jk.get()

    if nama == "" or nim == "" or kelas == "" or jk == "" or jk == "Pilih Jenis Kelamin":
        messagebox.showwarning("Validasi", "Semua field harus diisi!")
        return

    val_nama.configure(text=nama)
    val_nim.configure(text=nim)
    val_kelas.configure(text=kelas)
    val_jk.configure(text=jk)

def reset():
    entry_nama.delete(0, "end")
    entry_nim.delete(0, "end")
    entry_kelas.delete(0, "end")
    combo_jk.set("Pilih Jenis Kelamin")

    val_nama.configure(text="")
    val_nim.configure(text="")
    val_kelas.configure(text="")
    val_jk.configure(text="")

app = ctk.CTk()
app.title("Form Biodata Mahasiswa")
app.geometry("500x600")

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=20, fill="both", expand=True)


ctk.CTkLabel(frame,
             text="Form Biodata Mahasiswa",
             font=("Poppins", 18, "bold")).pack(pady=10)

ctk.CTkLabel(frame, text="Nama Lengkap").pack(anchor="w", padx=20)
entry_nama = ctk.CTkEntry(frame, placeholder_text="Masukkan nama lengkap")
entry_nama.pack(padx=20, pady=5, fill="x")

ctk.CTkLabel(frame, text="NIM").pack(anchor="w", padx=20)
entry_nim = ctk.CTkEntry(frame, placeholder_text="Masukkan NIM")
entry_nim.pack(padx=20, pady=5, fill="x")

ctk.CTkLabel(frame, text="Kelas").pack(anchor="w", padx=20)
entry_kelas = ctk.CTkEntry(frame, placeholder_text="Contoh: TI-2A")
entry_kelas.pack(padx=20, pady=5, fill="x")

ctk.CTkLabel(frame, text="Jenis Kelamin").pack(anchor="w", padx=20)
combo_jk = ctk.CTkComboBox(
    frame,
    values=["Laki-laki", "Perempuan"],
    state="readonly"
)
combo_jk.pack(padx=20, pady=5, fill="x")
combo_jk.set("Pilih Jenis Kelamin") 


btn_frame = ctk.CTkFrame(frame, fg_color="transparent")
btn_frame.pack(pady=10)

ctk.CTkButton(btn_frame, text="Tampilkan", command=tampilkan)\
    .pack(side="left", padx=10)

ctk.CTkButton(btn_frame, text="Reset", fg_color="gray", command=reset)\
    .pack(side="left", padx=10)

hasil_frame = ctk.CTkFrame(frame, corner_radius=12, fg_color="#a9b5e8")
hasil_frame.pack(padx=20, pady=15, fill="both", expand=True)

left_bar = ctk.CTkFrame(hasil_frame, width=5, fg_color="#2e31cc")
left_bar.pack(side="left", fill="y")

content = ctk.CTkFrame(hasil_frame, fg_color="transparent")
content.pack(side="left", fill="both", expand=True, padx=15, pady=15)

ctk.CTkLabel(content,
             text="DATA BIODATA",
             font=("Poppins", 16, "bold"),
             text_color="#1b5e20")\
    .grid(row=0, column=0, columnspan=3, sticky="w", pady=(0,7))

ctk.CTkLabel(content, text="Nama").grid(row=1, column=0, sticky="w", pady=0)
ctk.CTkLabel(content, text="NIM").grid(row=2, column=0, sticky="w", pady=0)
ctk.CTkLabel(content, text="Kelas").grid(row=3, column=0, sticky="w", pady=0)
ctk.CTkLabel(content, text="Jenis Kelamin").grid(row=4, column=0, sticky="w", pady=0)

ctk.CTkLabel(content, text=":").grid(row=1, column=1)
ctk.CTkLabel(content, text=":").grid(row=2, column=1)
ctk.CTkLabel(content, text=":").grid(row=3, column=1)
ctk.CTkLabel(content, text=":").grid(row=4, column=1)

val_nama = ctk.CTkLabel(content, text="", anchor="w", wraplength=250)
val_nama.grid(row=1, column=2, sticky="w")

val_nim = ctk.CTkLabel(content, text="", anchor="w")
val_nim.grid(row=2, column=2, sticky="w")

val_kelas = ctk.CTkLabel(content, text="", anchor="w")
val_kelas.grid(row=3, column=2, sticky="w")

val_jk = ctk.CTkLabel(content, text="", anchor="w")
val_jk.grid(row=4, column=2, sticky="w")


content.grid_columnconfigure(0, weight=1)
content.grid_columnconfigure(1, weight=0)
content.grid_columnconfigure(2, weight=3)


app.mainloop()