import random
def shuffleString(x, n):
    result = []
    i = 0
    while i < n:
        acak = ''.join(random.sample(x, len(x)))
        if(acak not in result):
            result += [acak]
            i += 1
    print(result)

banyakRandom = int(input('Masukan banyaknya kata yang akan di random:'))
shuffleString('aku', banyakRandom)
