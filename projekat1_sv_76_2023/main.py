
PvP_PvC = ''
OBAVEZNO_UKLANJANJE = False
TEZINA_IGRE = ''

def meni():
    global PvP_PvC
    while True:
        print('Vrsta igre')
        print('1. Player vs Player')
        print('2. Player vs Computer')
        print('3. Izlazak iz igre')
        value = input('>>> ')

        if value=='1':
            PvP_PvC = 'PVP'
            pravila_igre_meni()
        elif value=='2':
            PvP_PvC = 'PVC'
            pravila_igre_meni()
        elif value=='3':
            exit()

def pravila_igre_meni():
    global OBAVEZNO_UKLANJANJE
    while True:
        print('Pravila igre')
        print('1. Obavezno uklanjanje')
        print('2. Slobodno kretanje')
        print('3. Izlazak iz igre')
        value = input('>>> ')

        if value=='1':
            OBAVEZNO_UKLANJANJE = True
            if PvP_PvC == 'PVC':
                tezina_igre()
            igra()
            
        elif value=='2':
            if PvP_PvC == 'PVC':
                tezina_igre()
            igra()
        elif value=='3':
            exit()

def tezina_igre():
    global TEZINA_IGRE
    while True:
        print('Tezina igre')
        print('1. Easy')
        print('2. Medium')
        print('3. Hard')
        print('4. Izlazak iz igre')
        value = input('>>> ')

        if value=='1':
            TEZINA_IGRE = 'EASY'
            igra()
        elif value=='2':
            TEZINA_IGRE = 'MEDIUM'
            igra()
        elif value=='3':
            TEZINA_IGRE = 'HARD'
            igra()
        elif value=='4':
            exit()

def igra():
    print(PvP_PvC, OBAVEZNO_UKLANJANJE, TEZINA_IGRE)

if __name__ == '__main__':
    meni()
    pass

