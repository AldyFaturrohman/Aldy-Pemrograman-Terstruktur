def kuadrat(bil):
    try:
        hasilKuadrat=[]
        for i in bil:
            hasilBilangan=i**2
            hasilKuadrat.append(hasilBilangan)
        print(hasilKuadrat)
    except TypeError:
        print("Maaf data ada yang bukan bilangan")

bil=[1,8,3,9,4]
kuadrat(bil)
