buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print('Diketahui list buah dengan harganya sebagai berikut:')
print(buah)

def hargaTermahal(buah):
    termahal=max(buah.values())
    keys = list(buah.keys())
    valus = list(buah.values())
    print('Dari list buah-buahan tersebut diketahui harga buah dengan harga paling mahal adalah:', keys[valus.index(termahal)])
    

hargaTermahal(buah)


