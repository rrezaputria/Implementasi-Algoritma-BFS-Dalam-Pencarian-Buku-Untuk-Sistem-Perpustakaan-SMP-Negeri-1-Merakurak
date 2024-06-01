from Backend.Structs.Pengguna import Pengguna

class Pegawai(Pengguna):
    def __init__(self, id_num, nama, email,  status, password, jabatan):
        super().__init__(id_num, nama, email, status, password)
        self.jabatan = jabatan
        
    #menampilkan informasi dari class pegawai (petugas) yang merupakan turunan dari class pengguna
    def display_info(self):
        super().display_info()
        print(f"Jabatan: {self.jabatan}")