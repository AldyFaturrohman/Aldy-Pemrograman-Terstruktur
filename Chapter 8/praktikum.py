# 1.
print("Buatlah list a = [1, 5, 6, 3, 6, 9, 11, 20, 12] dan b = [7, 4, 5, 6, 7, 1, 12, 5, 9]")
a = [1, 5, 6, 3, 9, 11, 20, 12]
b = [ 7, 4, 5, 6, 7, 1, 12, 5, 9]
print(' ')

# 2.
print("Sisipkan nilai 10 ke dalam indeks ke 3 dari a, dan 15 ke dalam indeks ke 2 dari b")
a.insert(3,10)
b.insert(2,15)
print(' ')

# 3.
print("Sisipkan nilai 4 ke indeks terakhir dari a, dan 8 ke indeks terakhir dari b")
a.append(4)
b.append(8)
print(' ')

# 4.
print("Kemudian lakukan sorting secara ascending pada list a dan b")
a.sort()
b.sort()
print(' ')

# 5.
print("Buatlah list c yang elemennya merupakan sublist dari a (mulai dari indeks ke 0 s/d 7), dan list d yang elemennya merupakan sublist dari b (mulai indeks ke 2 s/d 9)")
c = a[:8]
d = b[2:10]
print(' ')

# 6.
print("Buatlah serangkaian langkah untuk mendapatkan list e yang elemennya merupakan hasil penjumlahan dari setiap elemen c dan d yang bersesuaian indeksnya.")
e = []
for i in range(len(d)):
    e += [c[i] + d[i]]
print(' ')

# 7.
print("Ubahlah list e ke dalam tuple")
e = tuple(e)
print(' ')

# 8.
print("Carilah nilai min, maks, dan jumlahan seluruh elemen dari e")
min = min(e)
max = max(e)
sum = sum(e)
print(' ')

# 9.
print('Buatlah sebuah string myString = “python adalah bahasa pemrograman yang menyenangkan”')
myString = "python adalah bahasa pemrograman yang menyenangkan"
print(' ')

# 10.
print("Dengan menggunakan set() tentukan karakter huruf apa saja yang menyusun string tersebut")
myStringSet = set(myString)
print(' ')

# 11.
print("Urutkan secara alfabet himpunan karakter huruf yang diperoleh dari langkah 10, dengan terlebih dahulu mengubahnya ke list.")
myStringSetList = list(myStringSet)
myStringSetList.sort()

# hasil
print('------------------------------------------------------------------------------------------------------------------------------------')
print("Hasil")
print("s",a)
print("b",b)
print("c", c)
print("d", d)
print("myString", myStringSetList)
