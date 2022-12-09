import random

#Alfabè n ap itilize pou jenere kod yo
alfabe = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabe_nimerik = alfabe + "0123456789"


def kod_inik(longe: int, alfabe: list):
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

print(kod_alfanimerik_inik(4))