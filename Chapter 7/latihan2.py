try:
    file = open(input('Masukan nama file:'), "a")
    lagi = 'y'
    while lagi == 'y': 
        append = input("Data yang mau ditambahkan :")
        file.write(append)
        lagi = input("Mau lagi (y/n)?")
    file.close()
except FileNotFoundError:
    print('file tidak ada/ salah penulisan')
