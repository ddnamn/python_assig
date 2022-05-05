# bissmillah 

class Cls :
    def __init__(self,n,no):
        self.name=n
        self.no=no

    @property
    def act (self):
        return 'ini aksi dari method yang otomatis dipanggil untuk dijalankan'

pertama=Cls('ucup',82324)
print(pertama.name)
print(pertama.no)
print(pertama.act)
# melihat isi objek satu.__dict__