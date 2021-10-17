print("---------------------Status Kelulusan Mahasiswa----------------------")
a= (input("Nama : "))
m= int(input("Nilai Matematika : "))
Ind= int(input("Nilai Bahasa Indonesia : "))
IPA= int(input("Nilai IPA : "))
if(m < 0) or (Ind < 0) or (IPA<0) or (m > 100) or (Ind > 100) or (IPA > 100):
    print("Maaf input ada yang tidak valid")
elif(m > 70) and (Ind > 60) and (IPA > 60):
    print("Status Kelulusan : ", a,"DINYATAKAN LULUS")
else:
    print("Status Kelulusan : ", a,"DINYATAKAN TIDAK LULUS")
    print("SEBAB")
    if(m < 70):
        print("Nilai Matematika anda kurang dari 70")
    if(Ind < 60):
        print("Nilai Bahasa Indonesia anda kurang dari 60")
    if(IPA < 60):
        print("Nilai IPA anda kurang dari 60")
