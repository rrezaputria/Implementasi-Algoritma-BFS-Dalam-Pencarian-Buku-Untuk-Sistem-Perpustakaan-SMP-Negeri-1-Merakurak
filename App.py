import customtkinter as ctk
from PIL import Image
from PIL import ImageTk
import os
from Backend.Controller.PengelolaanPengguna import PengelolaanPengguna
from Pages.Pencarian import Pencarian
from Pages.Edit import Edit
from Pages.Hapus import Hapus
from Pages.Tambah import Tambah



class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")
        

        self.rt = self
        self.rt.geometry("1000x700")
        self.rt.attributes("-topmost", True)  # Mengatur agar tampilan tetap di depan
        self.manyusers = PengelolaanPengguna("Dataset/DatasetPengguna.xlsx","Pengguna")
        self.useremail = None
        self.title = "SISTEM PEMINJAMAN BUKU SPENSAMER"
        self.icon = "Dataset/lib.png"
        self.create_widgets()

    #mengimport dan menampilkan gambar
    def create_widgets(self):

        self.title = ctk.CTkLabel(master=self.rt, width=120, height=5, text="SISTEM PEMINJAMAN BUKU SPENSAMER", font=('Verdana', 35, "bold"))
        self.title.pack(pady=12, padx=10)

        image = Image.open("img/login.jpg")
        image = image.resize((int(image.width * 1.5), int(image.height * 1.5)))

        self.img = ImageTk.PhotoImage(image)

        self.img_label = ctk.CTkLabel(master=self.rt, image=self.img, text="")
        self.img_label.pack(pady=0, padx=120, fill="both", expand=True)

        self.fr = ctk.CTkFrame(master=self.rt)
        self.fr.pack(ipady=100, pady=0, padx=100, fill="both", expand=False)

        self.label = ctk.CTkLabel(master=self.fr, width=120, height=5, text="Halaman Login", font=('Helvetica', 20, "bold"))
        self.label.pack(pady=12, padx=10)

        self.entry1 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Email")
        self.entry1.pack(pady=12, padx=10)

        self.entry2 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Password", show="*")
        self.entry2.pack(pady=12, padx=10)

        self.button = ctk.CTkButton(master=self.fr, width=240, height=32, text="Login", command=self.first_login)
        self.button.pack(pady=12, padx=10)

        self.label2 = ctk.CTkLabel(master=self.fr, width=120, height=5, text="", font=('Helvetica', 15, "bold"))
        self.label2.pack(pady=15, padx=10)

    #menampilkan halaman login
    def first_login(self):
        if(self.manyusers.isMatch(self.entry1.get(),self.entry2.get())):
            self.useremail = self.entry1.get()
            self.img_label.destroy()
            self.fr.destroy()
            self.title.destroy()
            self.goto_pencarian()
        else:
            self.label2.configure(text = "Username atau Password Salah!")
        

    #menampilkan halaman pencarian
    def goto_pencarian(self):
        pencarian = Pencarian(self.rt,self.manyusers.isAnggota(self.useremail))
        pencarian.show()

    #menampilkan halaman edit
    def goto_edit(self):
        edit = Edit(self.rt)
        edit.show()
    
    #menampilkan halaman penambahan
    def goto_tambah(self):
        self.fr.destroy()
        tambah = Tambah(self.rt)
        tambah.show()

    #menampilkan halaman pengahpusan
    def goto_hapus(self):
        self.fr.destroy()
        hapus = Hapus(self.rt)
        hapus.show()

    #menjalankan aplikasi
    def run(self):
        self.rt.mainloop()

#menjalankan objek aplikasi
if __name__ == "__main__":
    app = App()
    app.run()
