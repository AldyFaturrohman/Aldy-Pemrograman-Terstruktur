try:
    hitung = int(input("Berapa banyak bilangan bulat yang dibutuhkan?"))
    loop = 0
    data = []
    while loop < hitung:
        number = int(input("Masukkan bilangan bulat ke-{0} : ".format(loop+1)))
        data.append(number)
        loop += 1

    data.sort(reverse=True)
    print("Hasil data dengan urutan dari angka besar ke kecil", data)
except ValueError:
    print("data yang anda masukan bukan angka / salah")
