import customtkinter as ctk
import tkinter.ttk as ttk
from Pages.Edit import Edit
from Backend.Controller.PengelolaanBuku import PengelolaanBuku
from Backend.Structs.Buku import Buku

class Tambah:
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
        self.button3 = ctk.CTkButton(master=self.tabview.tab("Perpustakaan"),text="Edit Lokasi Buku",command=self.goto_edit)
        self.button3.pack(padx=20, pady=5)
        self.button4 = ctk.CTkButton(master=self.tabview.tab("Perpustakaan"),text="Hapus Buku",command=self.goto_hapus)
        self.button4.pack(padx=20, pady=5)


        self.fr = ctk.CTkFrame(master=self.master)
        self.fr.pack( pady=10, padx=100, fill="both", expand=False)

        self.label = ctk.CTkLabel(master=self.fr, width=120, height=5, text="Tambah Buku", font=('Helvetica', 20, "bold"))
        self.label.pack(pady=12, padx=10)

        self.entry0 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Judul")
        self.entry0.pack(pady=0, padx=10)
        self.entry1 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Kategori")
        self.entry1.pack(pady=0, padx=10)
        self.entry2 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Jumlah Buku")
        self.entry2.pack(pady=0, padx=10)
        self.entry3 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Pengarang")
        self.entry3.pack(pady=0, padx=10)
        self.entry4 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Penerbit")
        self.entry4.pack(pady=0, padx=10)
        self.entry5 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Tahun Terbit")
        self.entry5.pack(pady=0, padx=10)
        self.entry6 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="ISBN")
        self.entry6.pack(pady=0, padx=10)
        self.entry7 = ctk.CTkEntry(master=self.fr, width=240, height=32, placeholder_text="Rak Buku")
        self.entry7.pack(pady=0, padx=10)

        self.button = ctk.CTkButton(master=self.fr, width=240, height=32, text="+ Tambah", command=self.add,fg_color="green")
        self.button.pack(pady=10, padx=10)

        self.result = ctk.CTkLabel(master=self.fr, width=120, height=5, text="", font=('Helvetica', 15))
        self.result.pack(pady = 0, padx = 10)



    #melakukan pencarian
    def goto_pencarian(self):
        self.tabview.destroy()
        self.fr.destroy()
        self.master.goto_pencarian()
        
    #melakukan pengeditan
    def goto_edit(self):
        self.tabview.destroy()
        self.fr.destroy()
        self.master.goto_edit()
        
    #melakukan penghapusan
    def goto_hapus(self):
        self.tabview.destroy()
        self.fr.destroy()
        self.master.goto_hapus()
        
    #melakukan penambahan
    def add(self):
        if(self.entry0.get() != "" and self.entry1.get() != "" and self.entry2.get() != "" and self.entry3.get() != ""
            and self.entry4.get() != "" and self.entry5.get() != "" and self.entry6.get() != "" and self.entry7.get() != ""):
            try:
                self.pengelolaan_buku.add(Buku(self.entry0.get(),self.entry1.get(),int(self.entry2.get()),self.entry3.get(),
                                            self.entry4.get(),int(self.entry5.get()),self.entry6.get(),int(self.entry7.get())))
                self.result.configure(text="Buku Berhasil Ditambah!") 
                self.entry0.delete(0, ctk.END)
                self.entry1.delete(0, ctk.END)
                self.entry2.delete(0, ctk.END)
                self.entry3.delete(0, ctk.END)
                self.entry4.delete(0, ctk.END)
                self.entry5.delete(0, ctk.END)
                self.entry6.delete(0, ctk.END)
                self.entry7.delete(0, ctk.END)
            except:
                self.result.configure(text="Input Format Error!") 
        else:
            self.result.configure(text="Pastikan Semua Kolom Diisi!") 
