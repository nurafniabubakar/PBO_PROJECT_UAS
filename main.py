from perpustakaan import Perpustakaan

perpus = Perpustakaan()

while True:
    print("\n=== MENU ===")
    print("1. Tambah Buku")
    print("2. Tampilkan Buku")
    print("3. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        judul = input("Judul   : ")
        penulis = input("Penulis : ")
        perpus.tambah_buku(judul, penulis)

    elif pilih == "2":
        perpus.tampilkan_buku()

    elif pilih == "3":
        break