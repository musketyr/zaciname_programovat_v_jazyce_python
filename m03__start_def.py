#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m03__start_def.py
"""
Příkazy a záznamy odpovědí zadávané ve výpisech kapitoly:
3  Začínáme programovat
"""



#Výpis 3.1: Definice funkce pozdrav()
############################################################################
def pozdrav():
    """Zjistí požadované oslovení uživatele a popřeje mu dobrý den."""
    oslovení = input('Jak vás mám oslovovat? ')
    print('Dobrý den,', oslovení)

pozdrav()
# Jak vás mám oslovovat? šéfe
# Dobrý den, šéfe
help(pozdrav)
# Help on function pozdrav in module __main__:

# pozdrav()             # SYNC
#     Zjistí požadované oslovení uživatele a popřeje mu dobrý den.

pozdrav.__doc__
# 'Zjistí požadované oslovení uživatele a popřeje mu dobrý den.'
# >>>



#Výpis 3.2: Odsazování pokračovacích řádků složených příkazů v konzolovém okně
############################################################################
# Microsoft Windows [Version 10.0.18362.900]
# (c) 2019 Microsoft Corporation. Všechna práva vyhrazena.
#
# Q:\65_PGM\65_PYT>python
# Python 3.9.0b3 (tags/v3.9.0b3:b484871, Jun  9 2020, 20:36:59) [MSC v.1924 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> def funkce():
# ...     print('Takto to Python řeší v konzolovém okně.')
# ...
# >>> funkce()
# Takto to Python řeší v konzolovém okně.
# >>>



#Výpis 3.3: Upravená definice funkce pozdrav()
############################################################################
# >>> \
def pozdrav():
    """Zjistí požadované oslovení uživatele, popřeje mu dobrý den
    a požadované oslovení vrátí jako svoji návratovou hodnotu.
    """
    oslovení = input('Jak vás mám oslovovat? ')
    print('Dobrý den,', oslovení)
    return oslovení

oslovení = pozdrav()
# Jak vás mám oslovovat? kolego
# Dobrý den, kolego
oslovení
# 'kolego'
# >>>



#Výpis 3.4: Definice a použití metody bmi
############################################################################
def bmi(výška, hmotnost):
    """Spočte BMI index osoby se zadanou váhou a výškou."""
    return hmotnost / (výška * výška)

bmi(1.85, 90)
# 26.296566837107374
# >>>



#Výpis 3.5: Používání pozičních a pojmenovaných argumentů
############################################################################
def pos_key_demo(p1, p2, p3, p4='Nezadán', p5='Nezadán'):
    """Pomocná funkce pro demonstraci možností zadávání argumentů."""
    print(f'{p1=}, {p2=}, {p3=}, {p4=}, {p5=}')

pos_key_demo('a1', 'a2', 'a3', 'a4')
# p1='a1', p2='a2', p3='a3', p4='a4', p5='Nezadán'
pos_key_demo(10, 20, p5=55, p3=33)
# p1=10, p2=20, p3=33, p4='Nezadán', p5=55
# >>>



#Výpis 3.6: Možné podoby definice prázdné funkce
############################################################################
def prázdná_funkce():
    """Dokumentační komentář."""

def funkce_s_prázdným_příkazem():
    pass

...
# Ellipsis
def funkce_s_výpustkou():
    ...

prázdná_funkce()
funkce_s_prázdným_příkazem()
funkce_s_výpustkou()
# >>>



#Výpis 3.7: Definice funkce demonstrující použití anotací
############################################################################
def anotace(celé: int, reálné: float = 3.14) -> None:
    """Funkce demonstrující použití anotací."""
    proměnná: str = f'{celé * reálné = } = {celé} * {reálné}'
    print(proměnná)

anotace.__annotations__
# {'celé': <class 'int'>, 'reálné': <class 'float'>, 'return': None}
anotace(3, 'Chyba! ')
# celé * reálné = 'Chyba! Chyba! Chyba! ' = 3 * Chyba!
# >>>



############################################################################
##### KONEC #####
