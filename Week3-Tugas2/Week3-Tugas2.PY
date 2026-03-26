# ==========================================
# Nama  : Septian Dwi Saputra
# NIM   : F1D022160
# Kelas : D
# ==========================================

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Fungsi konversi
def konversi(jenis):
    try:
        c = float(entry_suhu.get())
    except:
        messagebox.showerror("Error", "Input harus berupa angka!")
        return

    if jenis == "F":
        hasil = (c * 9/5) + 32
        teks = f"{c:.2f} Celsius = {hasil:.2f} Fahrenheit"

    elif jenis == "K":
        hasil = c + 273.15
        teks = f"{c:.2f} Celsius = {hasil:.2f} Kelvin"

    elif jenis == "R":
        hasil = c * 4/5
        teks = f"{c:.2f} Celsius = {hasil:.2f} Reamur"

    hasil_label.configure(text=teks)

app = ctk.CTk()
app.title("Konversi Suhu")
app.geometry("480x420")

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=20, fill="both", expand=True)

judul = ctk.CTkLabel(
    frame,
    text="KONVERSI SUHU",
    font=("Poppins", 18, "bold"),
    text_color="white",
    fg_color="#3b82f6",
    corner_radius=10,
    height=45
)
judul.grid(row=0, column=0, columnspan=3, sticky="ew", padx=15, pady=(15,10))


label_input = ctk.CTkLabel(frame, text="Masukkan Suhu (Celsius):")
label_input.grid(row=1, column=0, columnspan=3, sticky="w", padx=20)

entry_suhu = ctk.CTkEntry(frame)
entry_suhu.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

btn_f = ctk.CTkButton(frame, text="Fahrenheit", command=lambda: konversi("F"))
btn_f.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

btn_k = ctk.CTkButton(frame, text="Kelvin", command=lambda: konversi("K"))
btn_k.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

btn_r = ctk.CTkButton(frame, text="Reamur", command=lambda: konversi("R"))
btn_r.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

hasil_frame = ctk.CTkFrame(frame, fg_color="#dbeafe", corner_radius=10)
hasil_frame.grid(row=4, column=0, columnspan=3, padx=20, pady=15, sticky="ew")

judul_hasil = ctk.CTkLabel(
    hasil_frame,
    text="Hasil Konversi:",
    font=("Poppins", 14, "bold"),
    text_color="#1e3a8a"
)
judul_hasil.pack(anchor="w", padx=10, pady=(10,5))

hasil_label = ctk.CTkLabel(
    hasil_frame,
    text="",
    text_color="#1e3a8a"
)
hasil_label.pack(anchor="w", padx=10, pady=(0,10))


frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

app.mainloop()