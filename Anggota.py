from Backend.Structs.Pengguna import Pengguna

class Anggota(Pengguna):
    def __init__(self, id_num, nama, email, status, password, status_keanggotaan):
        super().__init__(id_num, nama, email, status, password)
        self.status_keanggotaan = status_keanggotaan

    #menampilkan informasi dari class anggota yang merupakan turunan dari class pengguna
    def display_info(self):
        super().display_info()
        print(f"Status Keanggotaan: {self.status_keanggotaan}")
