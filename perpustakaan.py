from buku import Buku

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, judul, penulis):
        buku = Buku(judul, penulis)
        self.daftar_buku.append(buku)

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku")
        for i, buku in enumerate(self.daftar_buku):
            print(f"\n[{i}]")
            buku.info()
