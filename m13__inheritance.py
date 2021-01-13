#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m13__inheritance.py
"""
Příkazy a záznamy odpovědí zadávané ve výpisech kapitoly:
13  Dědění
"""



#Výpis 13.1: Definice tříd Matka a Dcera v modulu m13a_MDPV
############################################################################
#
# Zdrojový kód v modulu m13a_MDPV
#
from m13a_MDPV import *


#Výpis 13.2: Záznam vytvoření instancí tříd Matka a Dcera a volání jejich metod
############################################################################
import m13a_MDPV as mdpv
# ===== Modul m13a_MDPV ===== START
# ===== Modul m13a_MDPV ===== STOP
m = mdpv.Matka()
# Matka - START - argm='M', argm2='', kwds={}
# Matka - KONEC
d = mdpv.Dcera()
# Dcera - START - argd='D', kwds={}
#    Matka - START - argm='M', argm2='dm', kwds={}
#    Matka - KONEC
# Dcera - KONEC
m.mtd()
# Instanční metoda třídy Matka
#    pro instanci typu <class 'm13a_MDPV.Matka'>.
#    self.cam = 'Třídní atribut matky'
#    self.iam = 'Instanční atribut matky (M)'
d.mtd()
# Instanční metoda třídy Dcera
#    pro instanci typu <class 'm13a_MDPV.Dcera'>.
#    self.cad = 'Třídní atribut dcery'
#    self.iad = 'Instanční atribut dcery (D)'
#    self.cam = 'Třídní atribut matky'
#    self.iam = 'Instanční atribut matky (M)'
# Instanční metoda třídy Matka
#    pro instanci typu <class 'm13a_MDPV.Dcera'>.
#    self.cam = 'Třídní atribut matky'
#    self.iam = 'Instanční atribut matky (M)'
# >>>



#Výpis 13.3: Definice tříd Přítelkyně a VnučkaDP v modulu m13a_MDPV
############################################################################
#
# Zdrojový kód v modulu m13a_MDPV
#



#Výpis 13.4: Záznam vytvoření instance třídy Vnučka a volání její metody
############################################################################
vDP = mdpv.VnučkaDP(argm='vM', argd='vD', argp='vP')
# VnučkaDP - START - argv='DP', kwds={'argm': 'vM', 'argd': 'vD', 'argp': 'vP'}
#    Dcera - START - argd='vD', kwds={'argm': 'vM', 'argp': 'vP'}
#       Matka - START - argm='vM', argm2='dm', kwds={'argp': 'vP'}
#          Přítelkyně - START - argp='vP', kwds={}
#          Přítelkyně - KONEC
#       Matka - KONEC
#    Dcera - KONEC
# VnučkaDP - KONEC
vPD = mdpv.VnučkaPD(argm='vM', argd='vD', argp='vP')
# VnučkaPD - START - argv='PD', kwds={'argm': 'vM', 'argd': 'vD', 'argp': 'vP'}
#    Přítelkyně - START - argp='vP', kwds={'argm': 'vM', 'argd': 'vD'}
#       Dcera - START - argd='vD', kwds={'argm': 'vM'}
#          Matka - START - argm='vM', argm2='dm', kwds={}
#          Matka - KONEC
#       Dcera - KONEC
#    Přítelkyně - KONEC
# VnučkaPD – KONEC
# >>>



############################################################################
##### KONEC #####
