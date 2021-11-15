sayur = ["bayam", "kangkung", "wortel", "selada"]
print("Daftar sayur-sayuran yang anda miliki sekarang.")
print(sayur)
print(' ')

lagi = 'y'
while lagi == 'y':
    
    print("A. Tambah data sayur")
    print("B. Hapus data sayur")
    print("C. Tampilkan data sayur")

    choose = input("Pilihan Anda : ")
    if (choose.lower() == 'a') or (choose.lower() == 'A'):
        append = input('data sayur yang ingin dimasukkan : ')
        sayur.append(append)

    elif (choose.lower() == 'b') or (choose.lower() == 'B'):
        delete = input('data sayur yang ingin dihapus : ')

    elif (choose.lower() == 'c') or (choose.lower() == 'C'):
        print("data sayur : {0}".format(sayur))

    else:
        print("Mohon maaf pilihan tersebut tidak ada")

    lagi = input('ingin mengolah data lagi (y/n)? ')



    
