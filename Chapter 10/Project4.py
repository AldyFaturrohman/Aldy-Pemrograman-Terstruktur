file = open("File PROTEK/Data2.txt", "r")

cari = input('Masukan nomor NIM yang ingin dicari:')

while True:
    read_file = file.readline()
    split_data = read_file.split('|')

    if (cari == split_data[0]):
        print("Data Mahasiswa")
        print("NIM         :", split_data[0])
        print("Nama        :", split_data[1])
        print("Alamat      :", split_data[2])
        break

    else:
        print('Mohon maaf data tidak ditemukan')
        break
