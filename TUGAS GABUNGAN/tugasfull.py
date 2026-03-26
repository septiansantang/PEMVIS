# ==========================================
# Nama  : Septian Dwi Saputra
# NIM   : F1D022160
# Kelas : D
# ==========================================

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Aplikasi Mahasiswa")
app.geometry("400x520")

frames = {}

def show_frame(name):
    for f in frames.values():
        f.pack_forget()
    frames[name].pack(fill="both", expand=True)

# ================= LOGIN =================
login = ctk.CTkFrame(app)
frames["login"] = login

container = ctk.CTkFrame(login, fg_color="transparent")
container.pack(expand=True)

ctk.CTkLabel(container, text="LOGIN",
             font=("Poppins", 26, "bold")).pack(pady=20)

entry_user = ctk.CTkEntry(container, width=250, placeholder_text="Username")
entry_user.pack(pady=5)

entry_pass = ctk.CTkEntry(container, width=250, placeholder_text="Password", show="*")
entry_pass.pack(pady=5)

def toggle_pass():
    entry_pass.configure(show="" if entry_pass.cget("show")=="*" else "*")

ctk.CTkCheckBox(container, text="Show Password",
                command=toggle_pass).pack()

def login_func():
    if entry_user.get()=="admin" and entry_pass.get()=="123":
        show_frame("menu")
    else:
        messagebox.showerror("Error","Login gagal!")

ctk.CTkButton(container, text="Login", width=200,
              command=login_func).pack(pady=15)

# ================= MENU =================
menu = ctk.CTkFrame(app)
frames["menu"] = menu

container = ctk.CTkFrame(menu, fg_color="transparent")
container.pack(expand=True)

ctk.CTkLabel(container, text="MENU UTAMA",
             font=("Poppins", 26, "bold")).pack(pady=20)

ctk.CTkButton(container, text="Form Biodata", width=250,
              command=lambda: show_frame("bio")).pack(pady=10)

ctk.CTkButton(container, text="Konversi Suhu", width=250,
              command=lambda: show_frame("suhu")).pack(pady=10)

ctk.CTkButton(container, text="Logout", width=250,
              fg_color="red",
              command=lambda: show_frame("login")).pack(pady=10)

# ================= BIODATA =================
bio = ctk.CTkFrame(app)
frames["bio"] = bio

container = ctk.CTkFrame(bio, fg_color="transparent")
container.pack(expand=True)

ctk.CTkLabel(container, text="FORM BIODATA",
             font=("Poppins", 22, "bold")).pack(pady=15)

entry_nama = ctk.CTkEntry(container, width=300, placeholder_text="Nama")
entry_nama.pack(pady=5)

entry_nim = ctk.CTkEntry(container, width=300, placeholder_text="NIM")
entry_nim.pack(pady=5)

entry_kelas = ctk.CTkEntry(container, width=300, placeholder_text="Kelas")
entry_kelas.pack(pady=5)

combo_jk = ctk.CTkComboBox(container,
                           values=["Laki-laki", "Perempuan"],
                           state="readonly",
                           width=300)
combo_jk.pack(pady=5)
combo_jk.set("Pilih Jenis Kelamin")

# Card hasil
hasil_card = ctk.CTkFrame(container, corner_radius=12, width=400, height=150)
hasil_card.pack(pady=20)
hasil_card.pack_propagate(False)

ctk.CTkLabel(hasil_card, text="DATA BIODATA",
             font=("Poppins", 16, "bold")).pack(pady=10)

val_nama = ctk.CTkLabel(hasil_card, text="")
val_nama.pack(anchor="w", padx=20)

val_nim = ctk.CTkLabel(hasil_card, text="")
val_nim.pack(anchor="w", padx=20)

val_kelas = ctk.CTkLabel(hasil_card, text="")
val_kelas.pack(anchor="w", padx=20)

val_jk = ctk.CTkLabel(hasil_card, text="")
val_jk.pack(anchor="w", padx=20)

def tampil_bio():
    if (entry_nama.get()=="" or entry_nim.get()=="" or
        entry_kelas.get()=="" or combo_jk.get()=="Pilih Jenis Kelamin"):
        messagebox.showwarning("Validasi","Isi semua field!")
        return

    data = [
        f"Nama: {entry_nama.get()}",
        f"NIM: {entry_nim.get()}",
        f"Kelas: {entry_kelas.get()}",
        f"Jenis Kelamin: {combo_jk.get()}"
    ]

    labels = [val_nama, val_nim, val_kelas, val_jk]

    def anim(i=0):
        if i < len(labels):
            labels[i].configure(text=data[i])
            app.after(120, anim, i+1)

    anim()

def reset_bio():
    entry_nama.delete(0,"end")
    entry_nim.delete(0,"end")
    entry_kelas.delete(0,"end")
    combo_jk.set("Pilih Jenis Kelamin")

    val_nama.configure(text="")
    val_nim.configure(text="")
    val_kelas.configure(text="")
    val_jk.configure(text="")

ctk.CTkButton(container, text="Tampilkan", width=200,
              command=tampil_bio).pack(pady=5)

ctk.CTkButton(container, text="Reset", width=200,
              command=reset_bio).pack(pady=5)

ctk.CTkButton(container, text="Kembali", width=200,
              command=lambda: show_frame("menu")).pack(pady=10)

# ================= SUHU =================
suhu = ctk.CTkFrame(app)
frames["suhu"] = suhu

container = ctk.CTkFrame(suhu, fg_color="transparent")
container.pack(expand=True)

ctk.CTkLabel(container, text="KONVERSI SUHU",
             font=("Poppins", 22, "bold")).pack(pady=15)

entry_suhu = ctk.CTkEntry(container, width=300)
entry_suhu.pack(pady=10)

hasil_suhu = ctk.CTkLabel(container, text="")
hasil_suhu.pack(pady=10)

def konversi(j):
    try:
        c=float(entry_suhu.get())
    except:
        messagebox.showerror("Error","Harus angka!")
        return

    if j=="F": h=(c*9/5)+32; s="Fahrenheit"
    elif j=="K": h=c+273.15; s="Kelvin"
    else: h=c*4/5; s="Reamur"

    hasil_suhu.configure(text=f"{c:.2f}°C = {h:.2f} {s}")

btn = ctk.CTkFrame(container, fg_color="transparent")
btn.pack()

ctk.CTkButton(btn, text="Fahrenheit",
              command=lambda: konversi("F")).pack(side="left", padx=5)

ctk.CTkButton(btn, text="Kelvin",
              command=lambda: konversi("K")).pack(side="left", padx=5)

ctk.CTkButton(btn, text="Reamur",
              command=lambda: konversi("R")).pack(side="left", padx=5)

ctk.CTkButton(container, text="Kembali",
              command=lambda: show_frame("menu")).pack(pady=10)

# ================= START =================
show_frame("login")
app.mainloop()