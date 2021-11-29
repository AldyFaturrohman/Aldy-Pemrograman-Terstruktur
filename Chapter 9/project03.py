def bintang(n):
    space = n
    if space % 2 == 0:
        print('Maaf, jumlah baris harus bernilai ganjil.')
    else:
        for i in range(n//2+1):
            print(('*'*(2*i+1)).center(space))

        for i in range(n//2, 0, -1):
            print(('*'*(2*i-1)).center(space))

hasil = int(input('Masukan banyaknya baris:'))
bintang(hasil)
