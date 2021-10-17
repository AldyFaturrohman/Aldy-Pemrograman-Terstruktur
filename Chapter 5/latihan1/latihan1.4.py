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
    golo = False
    print("tidak masuk golongan")

GajiBersih= GajiPokok - GajiPotongan

print("----------------------STRUK RINCIAN GAJI KARYAWAN----------------------")
print("Kode Karyawan:", Kode)
print("Golongan     :", Golo)
print("-----------------------------------------------------------------------")
print("Gaji Pokok   : Rp.", GajiPokok)
print("Potongan     : Rp.", GajiPotongan)
print("-----------------------------------------------------------------------")
print("Gaji Bersih  : Rp.", GajiBersih)
