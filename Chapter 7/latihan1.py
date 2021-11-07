try:
    file = open(input("Masukan Nama File:"), "r")
    print(file.read())
except FileNotFoundError:
    print('Mohon maaf tolong masukan lokasi filenya dan ekstensinya seperti D:/anyfiles.txt, atau file tersebut memang tidak ada')
