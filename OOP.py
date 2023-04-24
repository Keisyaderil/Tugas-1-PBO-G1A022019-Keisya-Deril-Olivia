# definisi kelas
class Mahasiswa:
    # konstruktor kelas
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm

    # method untuk menampilkan data mahasiswa
    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("NPM:", self.npm)

# membuat objek dari kelas Mahasiswa
mhs1 = Mahasiswa("Keisya Deril Olivia", "G1A022019")
mhs2 = Mahasiswa("Julita Rahma Yanti", "D1A022055")

# memanggil method untuk menampilkan data mahasiswa
mhs1.tampilkan_data()
mhs2.tampilkan_data()




