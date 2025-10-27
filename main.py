import functions
import random

#addig megy game ameddig ki nem lépsz belőle
#exit ?
#kezdo menu (elmagyarazza mi történik)

print("----------------\nAkasztófa: 11 tipped van hogy kitaláld a szót, ha hibás a tipped, a gép megad még egy karaktert.\nAddig meg a játék ameddig ki nem lépsz 0-val\n----------------")
#roadmap
#1. megjelenites
#2. tipp checkolas
#3. hibas tipp és kigyo megjelenites

tipp = input("Tippelj egy betűt: ")
while tipp != "0":
    szo = functions.szo()
    titkos = functions.titkos(szo)
    segitsegek = []
    hibak = 0
    max_tippek = 11
    tippek = []
    i = 0
    while i < len(szo):
        segitsegek.append(i)
        i+=1
    while tipp != szo:
        if tipp in szo:
            pass

print("Játék vége")

# karakterek = []
# i = 0
# while i < len(szo):
#     karakterek.append(i)
#     i+=1
# ki = random.randint(0, len(karakterek)-1)
# karakterek.pop(karakterek[ki])
# print(functions.jelenites(ki,szo,titkos))
# ki = random.randint(0, len(karakterek)-1)
# karakterek.pop(karakterek[ki])