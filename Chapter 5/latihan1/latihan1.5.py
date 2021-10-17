print("---------------------Slip Gaji----------------------")
Kode= (input("Kode Karyawan:"))
Nama= (input("Nama Karyawan:"))
Golo= (input("Golongan:"))
if (Golo == "A") or (Golo == "a"):
    GajiPokok= 10000000
    Potongan= 2.5/100
    GajiPotongan= GajiPokok*Potongan
elif (Golo == "B") or (Golo == "b"):
    GajiPokok= 8500000
    Potongan= 1/50
    GajiPotongan= GajiPokok*Potongan
elif (Golo == "C") or (Golo == "c"):
    GajiPokok= 7000000
    Potongan= 1.5/100
    GajiPotongan= GajiPokok*Potongan
elif (Golo == "D") or (Golo == "d"):
    GajiPokok= 5500000
    Potongan= 1/100
    GajiPotongan= GajiPokok*Potongan
else:
    Golo = False
    print("tidak masuk golongan")

if(Golo != False):
    status = int(input("Masukan Status (1:menikah, 2:blm) : "))
if(status == 1):
    tunjanganNikah = GajiPokok * 10/100
    anak = int(input("Masukkan Jumlah Anak : "))
    tunjanganAnak = GajiPokok * 5/100 * anak
elif(status == 2):
    tunjanganNikah = 0
    tunjanganAnak = 0
else:
    print("Input ada yang tidak valid")
    status = False

GajiKotor = GajiPokok + tunjanganNikah + tunjanganAnak
GajiBersih = GajiKotor - Potongan

if(status != False):
    print("=======================================")
    print("STRUK RINCIAN GAJI KARYAWAN")
    print("---------------------------------------")
    print("Nama Karyawan         : ",Nama, " ( Kode:",Kode,")")
    print("Golongan              : ", Golo)

if(status == 1):
    print("Status                : Menikah")
    print("Jumlah Anak           : ", anak)
else:
    print("Status                : Belum Menikah")

print("----------------------STRUK RINCIAN GAJI KARYAWAN----------------------")
print("Kode Karyawan:", Kode)
print("Golongan     :", Golo)
print("-----------------------------------------------------------------------")
print("Gaji Pokok   : Rp.", GajiKotor)
print("Potongan     : Rp.", GajiPotongan)
print("-----------------------------------------------------------------------")
print("Gaji Bersih  : Rp.", GajiBersih)
