import random
def szo() -> str:
    lista = [
        "alma", "kutya", "ház", "asztal", "ablak", "tenger", "hegy", "könyv", "iskola", "kert",
        "fa", "víz", "nap", "hold", "csillag", "szél", "ember", "madár", "vonat", "autó",
        "bicikli", "kenyér", "tej", "sajt", "kalap", "cipő", "zokni", "kabát", "nadrág", "ing",
        "telefon", "óra", "számítógép", "egér", "billentyűzet", "füzet", "ceruza", "toll", "radír", "asztalos",
        "tanár", "diák", "főnök", "titkár", "orvos", "nővér", "kórház", "bolt", "pénz", "bank",
        "repülő", "híd", "út", "lámpa", "szék", "kanapé", "tükör", "függöny", "padló", "fal",
        "tető", "kapu", "kerítés", "virág", "rózsa", "tulipán", "levél", "gyökér", "gyümölcs", "zöldség",
        "krumpli", "répa", "paradicsom", "uborka", "hagyma", "bab", "borsó", "almafa", "körtefa", "szilva",
        "erdő", "mező", "domb", "patak", "folyó", "híd", "sziget", "csónak", "vitorla", "hal",
        "béka", "kígyó", "róka", "medve", "szarvas", "nyúl", "ló", "tehén", "malac", "csirke"
    ]
    return lista[random.randint(0,99)]

def titkos(szo : str) -> str:
    szoveg = []
    i = 0
    while i < len(szo):
        szoveg.append("_")
        i+=1
    return szoveg

def jelenites(szam: list , szo:str, titkos: list) -> str:
    i=0
    while i < len(szam):
        index = szam[i]
        titkos[index] = szo[index]
        i+=1
    szoveg = "".join(titkos)
    return szoveg

def tippcheck(karakter : str, szo : str):  #tipp, szó bemenet -> int[]
    tipp = karakter
    szo_ = szo
    i: int = 0
    indexek = []
    while i < len(szo_):
        if tipp == szo_[i]:
            indexek.append(i)
        i += 1
    if indexek == []:
        return -1
    return indexek
#todo: kigyó megjelenítés, kap egy intet mennyi hibánk van
#*""""""""""|
#***********| rossz tipek száma > 11 -> gatya
#rossz tippeket is tároljuk
#no error handling
def hiba_kigyo(hibak : int, maxhiba : int) -> str:
    max_hiba = maxhiba
    i=0
    szoveg = ""
    while i < max_hiba:
        if i < hibak:
            szoveg+="*"
        else:
            szoveg+="-"
        i+=1
    szoveg+="|"
    return szoveg

#_____
#index = random.randint(0, len(szo) -1)
#felfedett = []
#i=0
#while i < len(szo)
#   felfedett.append("*")
#   i +=1
#rossz_tippek = []
#segitsegek = []
#hibak_szama = 0
#rossz_tippek = 0
#
