bil = 0
count = 0
hasil = 0
while(bil <= 100):
    if(bil % 2 == 1):
        count += 1
        hasil += bil
        print(bil)
    bil += 1
print('Banyaknya bilangan ganjil :', count)
print('Jumlah seluruh bilangan :', hasil)
