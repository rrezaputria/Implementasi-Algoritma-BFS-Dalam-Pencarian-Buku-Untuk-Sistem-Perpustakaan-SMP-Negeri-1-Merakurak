import customtkinter as ctk
import tkinter.ttk as ttk
from Backend.Controller.PengelolaanBuku import PengelolaanBuku


class Edit:
    def __init__(self, master):
        self.master = master
        self.pengelolaan_buku = PengelolaanBuku("Dataset/DatasetBukuPerpustakaan.xlsx","Dataset_Buku_Perpustakaan")

    #menampilkan tampilan di GUI
    def show(self):
        self.tabview = ctk.CTkTabview(master=self.master, height=10)
        self.tabview.pack(padx=20, pady=20)

        perpustakaan_tab = self.tabview.add("Perpustakaan")  

        self.tabview.set("Perpustakaan")
        

        self.button2 = ctk.CTkButton(master=self.tabview.tab("Perpustakaan"),text="Pencarian Buku",command=self.goto_pencarian)
        self.button2.pack(padx=20, pady=5)
        self.button3 = ctk.CTkButton(master=self.tabview.tab("Perpustakaan"),text="Tambah Stok",command=self.goto_tambah)
        self.button3.pack(padx=20, pady=5)
        self.button4 = ctk.CTkButton(master=self.tabview.tab("Perpustakaan"),text="Hapus Buku",command=self.goto_hapus)
        self.button4.pack(padx=20, pady=5)


        self.fr = ctk.CTkFrame(master=self.master)
        self.fr.pack( pady=50, padx=100, fill="both", expand=False)

        self.label = ctk.CTkLabel(master=self.fr, width=120, height=5, text="Edit Lokasi Buku", font=('Helvetica', 20, "bold"))
        self.label.pack(pady=12, padx=10)

        self.entry1 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Nama Buku")
        self.entry1.pack(pady=12, padx=10)

        self.entry2 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Rak Buku Baru")
        self.entry2.pack(pady=12, padx=10)

        self.button = ctk.CTkButton(master=self.fr, width=240, height=32, text="Submit", command=self.edit,fg_color="green")
        self.button.pack(pady=12, padx=10)

        self.result = ctk.CTkLabel(master=self.fr, width=120, height=5, text="", font=('Helvetica', 15))
        self.result.pack(pady = 20, padx = 10)

    #melakukan pencarian
    def goto_pencarian(self):
        self.tabview.destroy()
        self.fr.destroy()
        self.master.goto_pencarian()

    #melakukan penambahan
    def goto_tambah(self):
        self.tabview.destroy()
        self.fr.destroy()
        self.master.goto_tambah()

    #melakukan penghapusan
    def goto_hapus(self):
        self.tabview.destroy()
        self.fr.destroy()
        self.master.goto_hapus()

    #menampilkan bagian pengeditan
    def edit(self):
        judul = self.entry1.get()
        book = self.pengelolaan_buku.search("Judul",judul)

        if(book == None):
            self.result.configure(text="Buku tidak ditemukan!")  #mengubah teks pada self.result  
        else:
            try:
                self.pengelolaan_buku.update("Judul",book.judul,"rak_buku",int(self.entry2.get()))
                self.result.configure(text=f"Buku {book.judul} berhasil diubah lokasinya!")  #mengubah teks pada self.result  
            except:
                self.result.configure(text=f"Format masukkan tidak valid!")

        self.entry1.delete(0, ctk.END)
        self.entry2.delete(0, ctk.END)
