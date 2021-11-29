mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('==============================================================')
print('NIM     NAMA MHS               TGL LAHIR          TEMPAT LAHIR')
print('--------------------------------------------------------------')

for data in mhs:
    datalist = data.split(":")
    nim      = datalist[0]
    nama     = datalist[1]

    tanggallahir = datalist[2]
    datatanggallahir = tanggallahir.split('-')
    formattanggallahir = "{0}/{1}/{2}".format(datatanggallahir[2], datatanggallahir[1],datatanggallahir[0])

    tempatlahir = datalist[3]

    print(nim.ljust(8), end='')
    print(nama.ljust(23), end='')
    print(formattanggallahir.ljust(19), end='')
    print(tempatlahir.ljust(12))

print('---------------------------------------------------------------')

