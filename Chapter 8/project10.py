def tampilkan_data(buah):
    print('Daftar Buah: ')
    for key, value in buah.items():
        print('-', key, ': ', value)


buah = {'apel': 5000,
        'jeruk': 8500,
        'mangga': 7800,
        'duku': 6500}

tampilkan_data(buah)
total_semua = 0
while True:
    try:
        nama = input('Masukkan nama buah: ')
        harga = buah[nama]
        jumlah = int(input('Berapa KG     : '))
        total_harga = harga * jumlah
        total_semua += total_harga
        tambah = input('Beli buah yang lain (y/n)? ')
        if tambah == 'n' or tambah == 'N':
            print('Total harga  :', total_semua)
            break
    except KeyError:
        print('DATA TIDAK DITEMUKAN!!')
