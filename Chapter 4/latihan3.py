import math
jarak = 795
konsumsi_bensin = 1/12
hasil = jarak * konsumsi_bensin
isi_bensin = math.ceil(hasil/50)

print ('Apabila kapasitas tangki bbm mobil pak Budi adalah 50 lt')
print ('Tentukan berapa kali minimal pak Budi harus mengisi bensin hingga penuh supaya bisa menyelesaikan perjalanannya!')
print ('Jawaban : ')
print ('Karena mobil membutuhkan bensin sebanyak',hasil, 'liter')
print ('Maka Pak Budi akan mengisi bensin sebanyak',isi_bensin, 'kali')
