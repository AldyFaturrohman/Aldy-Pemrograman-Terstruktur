def faktorial(n):
    hasil = 1
    while (n > 1):
        hasil = hasil * n
        n = n - 1
    return hasil

def C(n, r):
    return faktorial(n)/(faktorial(r)*faktorial(n-r))

def P(n, r):
    return faktorial(n)/(faktorial(n-r))

print(C(5, 3))
print(P(10, 7))
