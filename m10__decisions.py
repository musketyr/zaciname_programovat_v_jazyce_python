#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/chapters/m10__decisions.py
"""
Příkazy a záznamy odpovědí zadávané ve výpisech kapitoly:
10  Rozhodování.
"""



#Výpis 10.1: Převod libovolné hodnoty na logickou
############################################################################
bool(0), bool(None), bool(''), bool([]), bool({})
# (False, False, False, False, False)
bool(1), bool('A'), bool((1,)), bool([2,3]), bool({1, "Raz"})
# (True, True, True, True, True)
# >>>



#Výpis 10.2: Porovnání hodnot versus porovnání objektů
############################################################################
a = 'Dobrý ';   b = 'den!';   ab = a + b
print(f'''\
Objekty:   {ab = },   {a+b = }
Rovnost:   {ab == (a+b) = }
Totožnost: {ab is (a+b) = }'''
    )
# Objekty:   ab = 'Dobrý den!',   a+b = 'Dobrý den!'
# Rovnost:   ab == (a+b) = True
# Totožnost: ab is (a+b) = False
# >>>



#Výpis 10.3: Podmíněný výraz a jeho použití
############################################################################
def ifExpr(value):
    """Nahradí znaménko jeho slovním vyjádřením."""
    return ('plus ' if value > 0 else 'minus ')  +  str(abs(value))

f'{ifExpr(+5) = },     {ifExpr(-5) = }'
# "ifExpr(+5) = 'plus 5',     ifExpr(-5) = 'minus 5'"
# >>>



#Výpis 10.4: Použití jednoduchého podmíněného příkazu
############################################################################
# >>> \
def ifThen(číslo):
    """Doplní číslo slovním vyjádřením znaménka."""
    znam = 'plus'       # Předpokládám, že číslo je kladné
    if číslo < 0:       # Oprava pro záporné číslo
        znam  = 'minus'
        číslo = -číslo
    print (znam, číslo);

ifThen(5); ifThen(-7)
# plus 5
# minus 7
# >>>



#Výpis 10.5: Použití úplného podmíněného příkazu
############################################################################
# >>> \
def ifElse(číslo):
    """Doplní číslo slovním vyjádřením znaménka."""
    if (číslo > 0):     # Verze pro kladná čísla
        text = "plus " + str(číslo)
    else:               # Verze pro záporná čísla
        text = "minus " + str(-číslo)
    print(text)

ifElse(5);   ifElse(-7)
# plus 5
# minus 7
# >>>



#Výpis 10.6: Použití rozšířeného podmíněného příkazu
############################################################################
# >>> \
def dotaz(sezóna):
    """Vytiskne, co dělá jabloň v zadané sezóně."""
    if   sezóna == 'zima':
        aktivita = 'spí'
    elif sezóna == 'jaro':
        aktivita = 'kvete'
    elif sezóna == 'léto':
        aktivita = 'zraje'
    elif sezóna == 'podzim':
        aktivita = 'plodí'
    else:
         return "Špatně zadaná sezóna: " + str(sezóna)
    return 'Je-li ' + str(sezóna) + ', jabloň ' + str(aktivita)

print(f'{dotaz("jaro")}\n{dotaz("podzim")}\n{dotaz("nevím")}')
# Je-li jaro, jabloň kvete
# Je-li podzim, jabloň plodí
# Špatně zadaná sezóna: nevím
# >>>



#Výpis 10.7: Nástin syntaxe příkazů pro zachycení a ošetření výjimky
############################################################################
# try:
#     Příkazy, které mohou vyhodit výjimku
# except Očekávaná výjimka as Název proměnné :
#     Příkazy ošetřující danou výjimku
# except:
#     Příkazy ošetřující zbylé výjimky
# finally:
#     Příkazy, které se provedou vždy



#Výpis 10.8: Zachycení a ošetření výjimky
############################################################################
# >>> \
def dělení(a, b):
    """Zjistí, zda je možné zadané objekty dělit, a pokud ano,
    vrátí výsledek. Pokus o dělení nulou oznámí a vrátí None.
    Nelze-li zadané objekty dělit, vyhodí výjimku.
    """
    try:
        c = a / b
    except ZeroDivisionError as zde:
        print(f'Nepovolená operace: dělení nulou\n'
              f'Vyhozena výjimka {zde}')
        return None
    except:
        zpráva = f'Nelze dělit objekt «{a}» objektem «{b}»'
        raise Exception(zpráva)
    finally:
        print('--- Toto se provede vždy ---')
    return c

f'{dělení(5, 4) = }'
# --- Toto se provede vždy ---
# 'dělení(5, 4) = 1.25'
f'{dělení(5, 0) = }'
# Nepovolená operace: dělení nulou
# Vyhozena výjimka division by zero
# --- Toto se provede vždy ---
# 'dělení(5, 0) = None'
f'{dělení(a, b) = }'
# --- Toto se provede vždy ---
# Traceback (most recent call last):
#   File "<pyshell#22>", line 8, in dělení
#     c = a / b
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "<pyshell#26>", line 1, in <module>
#     f'{dělení(a, b) = }'
#   File "<pyshell#22>", line 15, in dělení
#     raise Exception(zpráva)
# Exception: Nelze dělit objekt «Dobrý » objektem «den!»
# >>>



############################################################################
##### KONEC #####
