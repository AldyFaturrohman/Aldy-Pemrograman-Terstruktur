from datetime import *

dataPeminjam= open("File/Data Peminjam.txt", "a")
def data():

    kode = input("Masukkan Kode Member : ")
    nama = input("Masukkan Nama Member : ")
    judulBuku= input("Masukkan Judul Buku   : ")
    hariIni=datetime.now()
    hariPengembalian= hariIni+timedelta(days=7)
    dataPeminjam.write("{}|{}|{}|{}|{}\n".format(kode,nama,judulBuku,datetime.date(hariIni), datetime.date(hariPengembalian)))

while True:
    data()
    lanjut= input("Lagi? (y/n)")
    if lanjut in ('n', 'no', 'N', 'NO'):
        break

dataPeminjam.close()
