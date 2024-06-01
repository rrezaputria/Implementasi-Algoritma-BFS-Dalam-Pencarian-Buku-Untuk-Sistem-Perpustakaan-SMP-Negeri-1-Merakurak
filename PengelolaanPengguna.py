import openpyxl
from Backend.Structs.Pengguna import Pengguna
from Backend.Structs.Anggota import Anggota
from Backend.Structs.Pegawai import Pegawai

class PengelolaanPengguna:
    def __init__(self,file, sheet):
        self.file = file
        self.sheet = sheet
        self.header = None
        self.users = []
        self.read()
    
    #membaca data buku dan menginisialisasi user dan header
    def read(self):
        print('aaaaaaaaaaa')
        sheet = openpyxl.load_workbook(self.file)[self.sheet]
        inc = 0

        for row in sheet.iter_rows():
            inc += 1
            if inc > 1:
                if row[0].value is None:
                    break
                val = [""] * 20
                inc = 0
                for cell in row:
                    if cell.value is None:
                        break
                    val[inc] = str(cell.value)
                    inc += 1
                if val[inc-1] == "Petugas":
                    self.users.append(Pegawai(val[0],val[1],val[2],val[3],val[4],"Karyawan"))
                else:
                    self.users.append(Anggota(val[0],val[1],val[2],val[3],val[4],"Aktif"))
            else:
                buffer = []
                for cell in row:
                    if cell.value is None:
                        break
                    buffer.append(cell.value)
                self.header = buffer

    #memeriksa user memiliki email=param         
    def isEmailExist(self, param):
        for user in self.users:
            if user.email == param:
                return True
        return False
    
    #memeriksa kecocokan email dan password
    def isMatch(self,param_email,param_pw):
        if not (self.isEmailExist(param_email)):
            return False
        
        for user in self.users:
            if user.email == param_email and user.password == param_pw:
                return True
        return False

    #memeriksa apakah pengguna tersebut apakah anggota
    def isAnggota(self,param_email):
        if not (self.isEmailExist(param_email)):
            return False
        
        for user in self.users:
            if user.email == param_email:
                return user.status == "Anggota"