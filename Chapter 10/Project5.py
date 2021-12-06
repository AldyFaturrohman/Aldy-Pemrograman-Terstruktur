file = open("File PROTEK/Data3.txt", "r")
isiData = file.read().splitlines()
file.close()

for i in range(0,len(isiData)):
    pemisah = isiData[i].split("|")
    del isiData[i]
    isiData.insert(i, pemisah)

ubahData = open("File PROTEK/Data3.txt", "w")
for i in range(0,len(isiData)):
    ubahData.write("{}\n".format((int(isiData[i][0])+int(isiData[i][1]))))
ubahData.close()
