import random

#Alfabè n ap itilize pou jenere kod yo
alfabe = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabe_nimerik = alfabe + "0123456789"


def kod_inik(longe: int, alfabe: str):
    """Sa a s on fonksyon jeneral, l ap ede n nan 2 lot fonksyon n ap gen pou n
    ekri yo."""
    
    lis_karakte = []
    for i in range(longe):
        karakte = random.choice(alfabe)
        while karakte in lis_karakte:
            karakte = random.choice(alfabe)
        lis_karakte.append(karakte)
    
    return "".join(lis_karakte)

#3
def kod_alfabetik_inik(longe: int):
    """Fonksyon sa a ap jenere yon kòd aleyatwa 
    ki gen n karaktè alfabetik, san repetisyon.
    longe endike konbye karakte kod sa a ap gen ladan"""

    return kod_inik(longe, alfabe)

#4
def kod_alfanimerik_inik(longe: int):
    """kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen
    n karaktè alafanimerik, san repetisyon.
    longe endike konbye karakte kod sa a ap gen ladan"""

    return kod_inik(longe, alfabe_nimerik)

#5
def jenere_slug(chenn: str):
    """Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan.
    Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak -"""

    return "".join([i for i in chenn if i.upper() in (alfabe_nimerik + "-")])

#6
def separe_pa_vigil(mo: str):
    """Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil"""
    
    return ",".join([letter for index, letter in enumerate(mo)])

#7
def kripte(mo: str):
    """Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a.
    Chak karaktè dwe separe ak yon tirè."""
    
    return "-".join([str(alfabe.index(i.upper())) for i in mo])

#8
def dekripte(mo: str):
    """Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak 
    endèks chak lèt nan alfabè a, separe ak yon tirè."""

    return "".join([alfabe[int(i)] for i in mo.split("-")])

#9
def pemite(a, b):
    """Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo.
    Answit li retounen tou 2 valè yo sou fòm Tuple."""

    temp = a
    a = b
    b = temp

    return a, b

#10
def inisyal_nom(mo: str):
    """Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo.
    Atansyon ak non konpoze ak tirè yo."""

    return "".join([ini[0] for ini in mo.replace("-", " ").split()])

print(inisyal_nom("Jean-Baptiste JEAN"))