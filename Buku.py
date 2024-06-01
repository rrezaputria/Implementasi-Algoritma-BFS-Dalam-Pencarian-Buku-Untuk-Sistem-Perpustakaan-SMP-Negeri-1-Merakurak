class Buku:    
    def __init__(self, judul,kategori,jumlah_buku,pengarang,penerbit,tahun_terbit,isbn,rak_buku):
        self.judul = judul
        self.kategori = kategori
        self.jumlah_buku = jumlah_buku
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.isbn = isbn
        self.rak_buku = rak_buku

    #menampilkan dan mengembalikan data buku dalam bentuk daftar
    def get_data(self):
        return [self.judul,self.kategori,self.jumlah_buku,self.pengarang,self.penerbit,self.tahun_terbit,self.isbn,self.rak_buku]
    
    #mencetak informasi debug mengenai data buku
    def debug(self):
        print("Debug Informasi Buku:")
        print(f"Judul: {self.judul}")
        print(f"Kategori: {self.kategori}")
        print(f"Jumlah Buku: {self.jumlah_buku}")
        print(f"Pengarang: {self.pengarang}")
        print(f"Penerbit: {self.pengarang}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"ISBN: {self.isbn}")
        print(f"Rak Buku: {self.rak_buku}")

    #mencetak informasi string mengenai data buku
    def info(self):
        debug_info = ""
        debug_info += f"Judul: {self.judul}\n"
        debug_info += f"Kategori: {self.kategori}\n"
        debug_info += f"Jumlah Buku: {self.jumlah_buku}\n"
        debug_info += f"Pengarang: {self.pengarang}\n"
        debug_info += f"Penerbit: {self.penerbit}\n"
        debug_info += f"Tahun Terbit: {self.tahun_terbit}\n"
        debug_info += f"ISBN: {self.isbn}\n"
        debug_info += f"Rak Buku: {self.rak_buku}\n"

        return debug_info
