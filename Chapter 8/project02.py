def dataStat(x):
    a= sum(x)/len(x)
    b= max(x)
    c= min(x)
    listABC=[a,b,c]
    return listABC

list = [10,20,3]
print(dataStat(list))
