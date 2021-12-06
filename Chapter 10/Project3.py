File = open("File PROTEK/Data2.txt", "r")

dataMhs = {}

i = 1
for data in File:
    dictsiji = {}
    dataDict = data.split("|")
    dictsiji['NIM'] = dataDict[0]
    dictsiji['Nama'] = dataDict[1]
    dictsiji['Alamat'] = dataDict[2].rstrip("\n")

dataMhs[i] = dictsiji
i += 1

print(dataMhs)
