from datetime import *
from Project1 import diffDate

file = open("File/Data Peminjam.txt", "r")
dateSekarang = datetime.date(datetime.now())
penalty =2000
memberCode = input('Masukan kode member:')


while True:
    read_file = file.readline()
    split_data = read_file.split('|')

    if memberCode == split_data[0]:
        diff = diffDate(split_data[4].replace('\n', ''))
        if diff < 0:
            diff = 0

        print('\nData Peminjaman Buku')
        print('\nKode Member\t\t:', split_data[0],
              '\nNama Member\t\t:', split_data[1],
              '\nJudul Buku\t\t:', split_data[2],
              '\nTanggal Mulai Pinjam\t:', split_data[3],
              '\nTanggal Maks Pinjam\t:', split_data[4].replace('\n', ''),
              '\nTanggal Pengembalian\t:', dateSekarang,
              '\nTerlambat\t\t:', str(diff) + ' hari',
              '\nDenda\t\t\t: Rp.', penalty * diff)
        break

    if not read_file:
        file.close()
        print('\nDATA TIDAK DITEMUKAN!!')
        break
