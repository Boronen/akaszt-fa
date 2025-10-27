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
    szoveg = ""
    i = 0
    while i < len(szo):
        szoveg += "_"
        i+=1
    return szoveg
def jelenites(szam : int, szo : str, titkos : str) -> str:
    szo_ = szo
    titkos_ = titkos
    szam_ = szam
    i = 0
    szoveg = ""
    while i < len(szo_):
        if i != szam_:
            szoveg += titkos[i]
        else:
            szoveg += szo_[i]
        i+=1
    return szoveg
#***********| rossz tipek száma > 11 -> gatya
#rossz tippeket is tároljuk
#no error handling

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
