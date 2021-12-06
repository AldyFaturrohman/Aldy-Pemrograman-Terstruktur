File = open("File PROTEK/Data1.txt", "r")
genap = 0
ganjil = 0

try:
    angka = File.readline()
    for data in File:
        if(int(data) % 2 == 0):
            genap += 1
        else:
            ganjil += 1

    print('Jumlah bilangan genap:', genap)
    print('Jumlah bilangan ganjil:', ganjil)
except FileNotFoundError:
    print("Maaf tidak dapat ditemukan file tersebut")
    

        
    
