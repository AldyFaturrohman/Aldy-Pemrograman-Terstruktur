try:
    banyak = int(input('Masukkan jumlah nama: '))
    listNama = []
    
    for i in range(banyak):
        nama = input('Masukkan nama ke-' + str(i+1) + ': ')
        listNama.append(nama)

    listNama.sort

    for nama in listNama:
        print(nama, '(', len(nama), 'karakter )')
        

except ValueError:
    print("Maaf input anda tidak valid, silahkan coba lagi")
