buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Diketahui list buah dengan harganya sebagai berikut:')
print(buah)

def hargaTermahal(buah):
    termahal=max(buah.values())
    keys = list(buah.keys())
    valus = list(buah.values())
    print('Dari list buah-buahan tersebut diketahui harga buah dengan harga paling mahal adalah:', keys[valus.index(termahal)])
    

hargaTermahal(buah)

def rataHargaBuah(buah):
    hargaBuah= list(buah.values())
    return sum(hargaBuah)/len(hargaBuah)

print('Rata-rata harga buah yang di beli adalah:', rataHargaBuah(buah))
print(' ')

try:
    print("Menghitung harga buah per kilogramnya")
    print('-----------------------------------------------------------')
    beliBuah= input("Nama buah yang dibeli 	:")
    if beliBuah in buah:
        kg=int(input("Berapa Kg		:"))
        print('-------------------------------------------------')
        print("Total Harga: ", buah[beliBuah]*kg)
except KeyError:
    print("maaf buah tidak tersedia")
except ValueError:
    print("Maaf hanya masukan angka")
