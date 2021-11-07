print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')

lagi = 'y'
awal = 0
total = 0
while lagi == 'y':
    try:
        bil = int(input("Masukkan bilangan bulat : "))
        total += bil
        awal += 1
        lagi = input("Lagi (y/n)?")
    except ValueError:
        print("Bukan bilangan bulat")

if(awal != 0):
    print('Rata-ratanya adalah', total/awal)
else:
    print('data tidak ada salah')
