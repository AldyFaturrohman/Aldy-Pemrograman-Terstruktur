File = open("File PROTEK/Data2.txt", "w")
while True:
    nim = input('Masukan NIM:')
    nama = input('Masukan Nama:')
    alamat = input('Masukan Alamat:')
    print('')

    File.write(nim + '|' + nama + '|' + alamat + '\n')

    repeat = input('Apakah ingin memasukan data lagi?(y/n):')
    print('')
    if(repeat in {'n','N'}):
        File.close()
        break
