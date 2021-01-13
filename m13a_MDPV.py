#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m13a_MDPV.py
"""
Dokumentační komentář modulu.
"""
print(f'===== Modul {__name__} ===== START')
############################################################################

from utils import prSK

class Matka():
    """Protože třída nedeklaruje explicitně předka,
    je bezprostředním potomkem třídy object.
    """
    cam = 'Třídní atribut matky'

    def __init__(self, argm='M', argm2='', **kwds):
        prSK(1, Matka, f'{argm=}, {argm2=}, {kwds=}')
        super().__init__(**kwds)
        self.iam = f'Instanční atribut matky ({argm})'
        prSK(0, Matka)

    def mtd(self):
        print(f'Instanční metoda třídy Matka\n'
              f'   pro instanci typu {type(self)}.\n'
              f'   {self.cam = }\n   {self.iam = }')


class Dcera(Matka):
    """Třída je bezprostředním potomkem třídy Matka.
    """
    cad = 'Třídní atribut dcery'

    def __init__(self, argd='D', **kwds):
        prSK(1, Dcera, f'{argd=}, {kwds=}')
        super().__init__(argm2='dm', **kwds)
        self.iad = f'Instanční atribut dcery ({argd})'
        prSK(0, Dcera)

    def mtd(self):
        print(f'Instanční metoda třídy Dcera\n'
              f'   pro instanci typu {type(self)}.\n'
              f'   {self.cad = }\n   {self.iad = }\n'
              f'   {self.cam = }\n   {self.iam = }')
        super().mtd()


############################################################################

class Přítelkyně():
    """Třída je bezprostředním potomkem třídy object.
    """
    def __init__(self, argp='P', **kwds):
        prSK(1, Přítelkyně, f'{argp=}, {kwds=}')
        super().__init__(**kwds)
        self.ipr = 'Instanční atribut přítelkyně'
        prSK(0, Přítelkyně)


class VnučkaDP(Dcera, Přítelkyně):
    """Třída je bezprostředním potomkem tříd Dcera a Přítelkyně.
    """
    def __init__(self, argv='DP', **kwds):
        prSK(1, VnučkaDP, f'{argv=}, {kwds=}')
        super().__init__(**kwds)
        self.iav = f'Instanční atribut první vnučky ({argv})'
        prSK(0, VnučkaDP)


class VnučkaPD(Přítelkyně, Dcera):
    """Třída je bezprostředním potomkem tříd Přítelkyně a Dcera.
    """
    def __init__(self, argv='PD', **kwds):
        prSK(1, VnučkaPD, f'{argv=}, {kwds=}')
        super().__init__(**kwds)
        self.iav = f'Instanční atribut druhé vnučky ({argv})'
        prSK(0, VnučkaPD)


############################################################################
print(f'===== Modul {__name__} ===== STOP')
