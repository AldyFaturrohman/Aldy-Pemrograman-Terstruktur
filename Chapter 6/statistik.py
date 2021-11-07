def sum(*number):
    hasil = 0
    for data in number:
        hasil += data
    return hasil

def average(*number):
    hasil = sum(*number)
    jumlah = 0
    for data in number:
        jumlah += 1
    return hasil / jumlah

def maks(*number):
    maks = number[0]
    for data in number:
        if maks < data:
            maks = data
    return maks

def min(*number):
    min = number[0]
    for data in number:
        if min > data:
            min = data
    return min
