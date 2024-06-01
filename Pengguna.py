class Pengguna:
    def __init__(self, id_num, nama, email, status, password):
        self.id_num = id_num
        self.nama = nama
        self.email = email
        self.status = status
        self.password = password
    
    #menampilkan informasi pengguna dari class pengguna
    def display_info(self):
        print(f"ID: {self.id_num}")
        print(f"Nama: {self.nama}")
        print(f"Email: {self.email}")
        print(f"Status: {self.status}")
        print(f"Password: {self.password}")