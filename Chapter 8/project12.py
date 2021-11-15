buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def showData(buah):
    print("\nDaftar Bauh :")
    number = 1
    for x,y in buah.items():
        print("{0}. {1} - {2}".format(number,x,y))
        number += 1


showData(buah)
lagiOlahData = 'y'
while lagiOlahData == 'y':
    print('-----------------------------------------------------')
    print('A. Tambah data buah')
    print('B. Beli buah')
    print('C. Hapus buah')
    print('D. Keluar dari program')
    pilihOlahData = input("pilihan menu : ")
    if(pilihOlahData == 'A') or (pilihOlahData == 'a'):
        newDataBuah  = input('Masukkan nama buah    : ')
        if(newDataBuah in buah):
            print('buah sudah ada dalam daftar')
        else:
            while True:
                try:
                    newDataPrice = int(input('Masukkan harga satuan	: '))
                    buah[newDataBuah] = newDataPrice
                    showData(buah)    
                    break
                except ValueError:
                    print('data yang anda masukan bukan angka / salah')
                


    elif(pilihOlahData == 'B') or (pilihOlahData == 'b'):
        showData(buah)
        total = 0
        lagiBeli = 'y'
        while lagiBeli == 'y':
            choose = input("Nama buah yang dibeli : ")
            if(choose in buah):
                while True:
                    try:
                        kg = float(input('Berapa Kg             : '))
                        total += (buah[choose] * kg)
                        lagiBeli = input("Beli buah yang lain (y/n) ? ")
                        break
                    except ValueError:
                        print('data yang anda masukan bukan angka / salah')
                
            else:
                print('{0} tidak ada dalam daftar buah'.format(choose))

        print('-'*30)
        print("Total harga           :",total)
    elif(pilihOlahData == 'C'):
        delDataBuah  = input('Masukkan nama buah yang ingin dihapus : ')
        if(delDataBuah not in buah):
            print('buah {0} tidak ada dalam daftar'.format(delDataBuah))
        else:
            del(buah[delDataBuah])
            print('buah {0} berhasil dihapus dalam daftar'.format(delDataBuah))
            showData(buah)
    else:
        break
