import functions
import random

#addig megy game ameddig ki nem lépsz belőle
#exit ?
#kezdo menu (elmagyarazza mi történik)

print("----------------\nAkasztófa: 11 tipped van hogy kitaláld a szót, ha hibás a tipped, a gép megad még egy karaktert.\nAddig meg a játék ameddig ki nem lépsz 0-val\n----------------")
#roadmap
#1. megjelenites (tippek után)
#2. tipp checkolas
#3. hibas tipp és kigyo megjelenites
tipp = ""
while tipp != "0":
    szo = functions.szo()
    titkos = functions.titkos(szo)
    print(szo)
    hibak = 0
    max_tippek = 11
    tippek = []
    segitsegek = []
    i = 0
    while i < len(szo):
        segitsegek.append(i)
        i += 1
    segitseg_index = []
    segitseg_index.append(random.choice(segitsegek))
    print(functions.jelenites(segitseg_index, szo, titkos))
    segitsegek.remove(segitseg_index[0])
    tipp = input("Tippelj egy betűt: ")
    index = 0
    while segitsegek != [] and tipp != "0" and hibak < 11:
        if functions.tippcheck(tipp,szo) == -1:
            hibak += 1
            if hibak % 3 == 0:
                segitseg_index.append(random.choice(segitsegek))
                index += 1
                segitsegek.remove(segitseg_index[index])
            print(functions.jelenites(segitseg_index, szo, titkos))
        else:
            lista = functions.tippcheck(tipp,szo)
            print(functions.jelenites(lista,szo,titkos))
            j = 0
            while j < len(lista):
                if lista[j] in segitsegek:
                    segitsegek.remove(lista[j])
                j+=1
        print(functions.hiba_kigyo(hibak,max_tippek))
        print(segitsegek)
        if segitsegek != []:
            tipp = input("Tippelj egy betűt: ")
    if hibak < max_tippek:
        print("nyertél")
    else:
        print("vesztettél")
print("Játék vége")