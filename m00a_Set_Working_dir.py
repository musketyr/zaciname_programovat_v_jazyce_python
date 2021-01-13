#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#P:/64_PGM/64_PYT/m00a_Set_Working_dir.py
"""
Dokumentační komentář modulu.
"""

# print(f'===== Modul {__name__} ===== START')

import os

os.getcwd()     # Zjištění aktuálního pracovního adresáře

os.chdir(r'P:\64_PGM\64_PYT')    # Nastavení pracovního adresáře
os.chdir( 'P:/64_PGM/64_PYT')    # Akceptuje i lomítka

# os.curdir     # je aktuální adresář a má proto hodnotu "."

os.listdir(os.curdir)

def lcd():
    """List current working directory"""
    print('cwd = «', os.getcwd(), '»', sep='')
    for f in os.listdir(os.getcwd()):
        print(f)


# print(f'===== Modul {__name__} ===== STOP')
