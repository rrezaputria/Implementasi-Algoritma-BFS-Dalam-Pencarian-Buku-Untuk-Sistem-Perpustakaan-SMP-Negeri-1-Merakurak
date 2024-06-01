import customtkinter as ctk
import tkinter.ttk as ttk
from Backend.Controller.PengelolaanBuku import PengelolaanBuku

class Pencarian:
    def __init__(self, master, isAnggota):
        self.master = master
        if(isAnggota):
            self.state = "disabled"
        else:
            self.state = "normal"  
        self.pengelolaan_buku = PengelolaanBuku("Dataset/DatasetBukuPerpustakaan.xlsx","Dataset_Buku_Perpustakaan")
        
    #menampilkan tampilan di GUI
    def show(self):
        self.tabview = ctk.CTkTabview(master=self.master, height=10)
        self.tabview.pack(padx=20, pady=20)

        perpustakaan_tab = self.tabview.add("Perpustakaan")  

        self.tabview.set("Perpustakaan")
        

        self.button2 = ctk.CTkButton(master=self.tabview.tab("Perpustakaan"),text="Edit Lokasi Buku",command=self.goto_edit,state=self.state)
        self.button2.pack(padx=20, pady=5)
        self.button3 = ctk.CTkButton(master=self.tabview.tab("Perpustakaan"),text="Tambah Stok",command=self.goto_tambah,state=self.state)
        self.button3.pack(padx=20, pady=5)
        self.button4 = ctk.CTkButton(master=self.tabview.tab("Perpustakaan"),text="Hapus Buku",command=self.goto_hapus,state=self.state)
        self.button4.pack(padx=20, pady=5)


        self.fr = ctk.CTkFrame(master=self.master)
        self.fr.pack( pady=50, padx=100, fill="both", expand=False)

        self.label = ctk.CTkLabel(master=self.fr, width=120, height=5, text="Halaman Pencarian", font=('Helvetica', 20, "bold"))
        self.label.pack(pady=12, padx=10)

        self.entry = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Masukkan Judul Buku")
        self.entry.pack(pady=12, padx=10)

        self.button = ctk.CTkButton(master=self.fr, width=240, height=32, text="Cari", command=self.cari,fg_color="green")
        self.button.pack(pady=12, padx=10)

        self.result = ctk.CTkLabel(master=self.fr, width=120, height=5, text="", font=('Helvetica', 15))
        self.result.pack(pady = 20, padx = 10)
        
    #menampilkan cetak pesan
    def debug(self,event):
        print("Pencarian Buku tab diklik")
        
    #melakukan pengeditan
    def goto_edit(self):
        self.tabview.destroy()
        self.fr.destroy()
        self.master.goto_edit()
        
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
        
    #menampilkan bagian pencarian
    def cari(self):
        judul = self.entry.get()  
        book = self.pengelolaan_buku.search("Judul",judul)
        
        if(book == None):
            self.result.configure(text="Buku tidak ditemukan!")  #mengubah teks pada self.result  
        else:
            self.result.configure(text="Hasil pencarian: \n" + book.info())  #mengubah teks pada self.result  

        self.entry.delete(0, ctk.END)
        