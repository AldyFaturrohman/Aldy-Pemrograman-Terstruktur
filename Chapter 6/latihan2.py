def startFormation1(n):
    kolom = 1
    i = 0
    while(i < n):
        j = 0
        while(j < kolom):
            print('*', end=' ')
            j += 1
        kolom += 1
        print(' ')
        i += 1

def startFormation2(n):
    kolom = n
    i = 0
    while(i < n):
        j = 0
        while(j < kolom):
            print('*', end=' ')
            j += 1
        kolom -= 1
        print(' ')
        i += 1

def startFormation3(n):
    startFormation1(n//2)
    if(n % 2 == 0):
        startFormation2(n//2)
    else:
        startFormation2(n//2+1)
        
startFormation1(4)
print(' ')
startFormation2(4)
print(' ')
startFormation3(7)
        
