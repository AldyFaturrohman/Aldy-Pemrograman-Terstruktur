print("---------------------Status Kelulusan Mahasiswa----------------------")
a= (input("Nama : "))
m= int(input("Nilai Matematika : "))
Ind= int(input("Nilai Bahasa Indonesia : "))
IPA= int(input("Nilai IPA : "))
if(m > 70) and (Ind > 60) and (IPA > 60):
    print("Status Kelulusan : ", a,"DINYATAKAN LULUS")
else:
    print("Status Kelulusan : ", a,"DINYATAKAN TIDAK LULUS")



    
