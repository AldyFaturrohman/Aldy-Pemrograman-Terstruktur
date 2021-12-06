fileEnskripsi= open("File PROTEK/Data4.txt", "r")
n=2

container=[]
while True:
    bacaTeks= fileEnskripsi.read(1)
    if not bacaTeks:
        break
    keOrd= ord(bacaTeks)
    container.append(keOrd)

for i in range(0,len(container)):
    if container[i]!=32:
        if (container[i]>=65) and (container[i]<=90) :
            penambahan=(container[i]-n+65)%26+65
        else:
            penambahan=(container[i]-n+97)%26+97
        del container[i]
        container.insert(i, chr(penambahan))
    else:
        container.insert(i, chr(container[i]))
        del container[i+1]
        continue

hasilAkhir=''.join(container)
fileAsli= open("File PROTEK/Data4.txt", "w")
fileAsli.write(hasilAkhir)

fileAsli.close()
fileEnskripsi.close()
