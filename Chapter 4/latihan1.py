#Sebuah rental mobil menyewakan memberikan tarif sewa Rp 200.000 untuk 12 jam pertama, dan untuk berikutnya adalah Rp 10.000/jam. Jika seorang customer menyewa mobil di rental tersebut dari jam 06.00 sampai dengan jam 23.50 (pada hari yang sama), maka tentukan total tarif yang harus dia bayarkan kepada rental mobil!

#Harga rental mobil
print('Harga rental mobil')
Hargapokok=int(input('Harga sewa 12 jam pertama: Rp.'))
Hargatambahan=int(input('Harga sewa per jamnya: Rp.'))
print('-------------------------------------------------------------------------')

#Waktu sewa mobil yang dipakai
print('Waktu peminjaman:')
jam1=float(input('Jam:'))
menit1=float(input('menit:'))
print('Waktu pengembalian:')
jam2=float(input('Jam:'))
menit2=float(input('menit:'))
SelisihJam=jam2-jam1
SelisihMenit=menit2-menit1
print('Total waktu:',round(SelisihJam),'jam',round(SelisihMenit),'menit')
print('-------------------------------------------------------------------------')

#Pembayaran rental mobil
if(SelisihJam > 12):
    print('Harga sewa total: Rp.',Hargapokok+(Hargatambahan*(SelisihJam-12)+Hargatambahan*(SelisihMenit/60)))
elif(SelisihJam < 12):
    print('Harga sewa total: Rp.',(Hargapokok/12*(selisihJam)+Hargapokok/12/60*(SelisihMenit)))
else:
    print('Harga sewa total: Rp.',Hargapokok)
