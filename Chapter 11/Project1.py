from datetime import *

def diffDate(x):
    try:
        search = datetime.strptime(x, '%Y-%m-%d')
        tlHariIni = datetime.now()
        selisih = search-tlHariIni
        selisihHari = selisih.days+1
        return selisihHari
    except TypeError:
        print('Maaf ada yang salah')
