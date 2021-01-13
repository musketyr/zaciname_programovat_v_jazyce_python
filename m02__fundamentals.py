#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m02__fundamentals.py
"""
Příkazy a záznamy odpovědí zadávané ve výpisech kapitoly:
2  Superzáklady
"""



#Výpis 2.1: Počáteční mezery a komentáře
############################################################################
123 + 456 #Před zadáním příkazu nesmí být zbytečná mezera
# 579
#!# 432 - 10 #Tady jedna byla

# SyntaxError: unexpected indent
# >>>



#Výpis 2.2: Možnosti zápisu celých čísel
############################################################################
#!# 012
# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
123_456_789
# 123456789
1_23_456_7890_12345
# 123456789012345
# >>>



#Výpis 2.3: Zadávání a zobrazování reálných čísel
############################################################################
123_456_789_0_123_456_789_0_123_456_789.
# 1.2345678901234568e+28
123e-3
# 0.123
123.
# 123.0
123e3
# 123000.0
# >>>



#Výpis 2.4: Zápis Zápis jednořádkového textu
############################################################################
"Text v uvozovkách"
# 'Text v uvozovkách'
'Text v apostrofech'        # SYNC
# 'Text v apostrofech'
"Potřebuji 'apostrof'"      # SYNC
# "Potřebuji 'apostrof'"
'Potřebuji "uvozovky"'      # SYNC
# 'Potřebuji "uvozovky"'
# >>>



#Výpis 2.5: Znak # ve stringu představuje sám sebe
############################################################################
'Ve stringu představuje znak # sám za sebe.'        # SYNC
# 'Ve stringu představuje znak # sám za sebe.'
# >>>



#Výpis 2.6: Zápis víceřádkového textu
############################################################################
#!# "Neukončený text
# SyntaxError: EOL while scanning string literal
"""několikařádkový
text"""
# 'několikařádkový\ntext'
'''
    Jiný způsob\
    'zápisu'
    '''
# "\n    Jiný způsob    'zápisu'\n    "
#!# '''Musí být 'odděleny''''
# SyntaxError: EOL while scanning string literal
''''Apostrof'.'''
# "'Apostrof'."
""     #Dvojice uvozovek či apostrofů označuje prázdný string
# ''
"Bezprostředně 'sousedící' stringy"  'Python "automaticky" sloučí'
# 'Bezprostředně \'sousedící\' stringyPython "automaticky" sloučí'
# >>>



#Výpis 2.7: Definice a použití proměnných
############################################################################
a = 123     #Vytvářím a současně inicializuji novou proměnnou
a           #Nechávám zobrazit její hodnotu
# 123
#!# a = a + x   #Proměnná x ještě není vytvořena
# Traceback (most recent call last):
#   File "<pyshell#27>", line 1, in <module>
#     a = a + x   #Proměnná x ještě není vytvořena
# NameError: name 'x' is not defined
x = 456     #Vytvářím a současně inicializuji proměnnou x
a = a + x   #Proměnná x je již použitelná
a           #Obsah proměnné a se změnil
# 579
# >>>



#Výpis 2.8: Nebezpečné změny hodnot
############################################################################
a = "Sto dvacet tři"  #Opět měním hodnotu proměnné a
#!# x = a + x             #String není možné sčítat s číslem
# Traceback (most recent call last):
#   File "<pyshell#20>", line 1, in <module>
#     x = a + x             #String není možné sčítat s číslem
# TypeError: can only concatenate str (not "int") to str
b = 'miliónů'    #Vytvářím a inicializuji proměnnou b
a + b            #Dva stringy již sčítat mohu
# 'Sto dvacet třimiliónů'
a + ' ' + b
# 'Sto dvacet tři miliónů'
mezera = ' '
a + mezera + b
# 'Sto dvacet tři miliónů'
# >>>



#Výpis 2.9: Použití funkcí
############################################################################
str(x) + mezera + b
# '456 miliónů'
print(x, b)
# 456 miliónů
print("Proměnná b má", len(b), "znaků:", b)
# Proměnná b má 7 znaků: miliónů
print('Prázdný string má', len(''), 'znaků')
# Prázdný string má 0 znaků
print('První řádek\n Druhý řádek\n  Třetí řádek')
# První řádek
#  Druhý řádek
#   Třetí řádek
print('Při tisku se jak \'apostrofy\', tak \"uvozovky\" zobrazují normálně')
# Při tisku se jak 'apostrofy', tak "uvozovky" zobrazují normálně
# >>>



#Výpis 2.10: Hodnota None a její zobrazení
############################################################################
z = None     #Vytvořím proměnnou z, ale současně říkám, že v ní nic není
z            #Je li hodnotou proměnné None, interpret ji netiskne
print(z)     #Funkce print ale tiskne i hodnotu None
# None
print(print('Tisknu 1'), "Funkce print() vrací:", print('Tisknu 2'))
# Tisknu 1
# Tisknu 2
# None Funkce print() vrací: None
# >>>



#Výpis 2.11: Ukázka použití funkce input() a implicitní proměnné
############################################################################
_ = input('Jak vás mám oslovovat? ')
# Jak vás mám oslovovat? Vaše blahorodí
# 'Vaše blahorodí'
print('Dobrý den,', _)
# Dobrý den, Vaše blahorodí
# >>>



#Výpis 2.12: Použití formátovaných stringů
############################################################################
print(f'''Sčítání:{  6 + 4 = }, {'AB'+"CD"=};   Odčítání: {4-6=};
Násobení: {6 * 4 = }, {3*'21' = },{ '21' * 3 = };
Dělení:   {6/4=};  Celočíselné: {6//4=};  Zbytek: {6%4=};
Mocnění:  {6**4 = },  {36**2 = }''')
# Sčítání:  6 + 4 = 10, 'AB'+"CD"='ABCD';   Odčítání: 4-6=-2;
# Násobení: 6 * 4 = 24, 3*'21' = '212121', '21' * 3 = '212121';
# Dělení:   6/4=1.5;  Celočíselné: 6//4=1;  Zbytek: 6%4=2;
# Mocnění:  6**4 = 1296,  36**2 = 1296
# >>>



#Výpis 2.13: Více příkazů na jednom řádku
############################################################################
x = 'Přiřazovaná hodnota';   x
# 'Přiřazovaná hodnota'
a = 1; b = 10; c = 100; print(a, b, c)
# 1 10 100
# >>>



############################################################################
##### KONEC #####
