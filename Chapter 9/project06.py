nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('==============================================================')
print('NIM     NAMA MHS          MID   UAS   N. AKHIR   STATUS')
print('--------------------------------------------------------------')

for i in range (len(nilai)):
    print(nilai[i]['nim'].ljust(8), end='')
    print(nilai[i]['nama'].ljust(14).ljust(14), end='')
    print(str(nilai[i]['mid']).rjust(6), end='')
    print(str(nilai[i]['uas']).rjust(6), end='')
    nilaiakhir = (nilai[i]['mid'] + 2*nilai[i]['uas'])/3
    status = "LULUS"
    if(nilaiakhir < 60):
        status = "TIDAK LULUS"
    print(str(round(nilaiakhir)). rjust(11), end='')
    print(status.rjust(9))


print('==============================================================')
