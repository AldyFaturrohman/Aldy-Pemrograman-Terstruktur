from random import randint
print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
score = 100
bil = randint(0, 100)
while True:
    if(score < 1):
        print("Anda sudah tidak diperbolehkan bermain karena score sudah habis")
        break
    tebak = int(input("Tebakan Anda: "))
    if(tebak > bil):
        print("Bilangan tebakan anda terlalu besar")
    elif(tebak < bil):
        print("Bilangan tebakan anda terlalu kecil")
    else:
        print("Yeayyy.... Bilangan tebakan anda BENAR")
        print("Score Anda: ", score)
        break
    score -= 2
