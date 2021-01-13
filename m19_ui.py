#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m00__chapter_template.py
"""
Příkazy a záznamy odpovědí zadávané ve výpisech kapitoly:
19  Spustitelná aplikace.
"""



#Výpis 19.1: Ukázky definic funkcí používajících cyklus while
############################################################################
# >>> \
def countDown(n) -> None:
    """Vytiskne zadaný počet čísel – a po nich slovo BUM."""
    while n>0:
        print(n, end='-')
        n -= 1
    print('BUM')

countDown(5)
# 5-4-3-2-1-BUM
# >>> \
def factW(n):
    """Faktoriál počítaný pomocí cyklu while."""
    f = 1      # Hodnota vracená v případě, když n <= 1
    while n > 1:
        f *= n
        n -= 1
    return f

factW(5)
# 120
# >>>



#Výpis 19.2: Nekonečný cyklus
############################################################################
# >>> \
def infinite() -> None:
    """Spustí prázdný nekonečný cyklus, který bude nutné přerušit zvenku."""
    while True: pass
    print('Hotovo')

infinite ()
# Traceback (most recent call last):
#   File "<pyshell#11>", line 1, in <module>
#     infinite()
#   File "<pyshell#10>", line 4, in infinite
#     while True: pass
# KeyboardInterrupt
# >>>



#Výpis 19.3: Chování logických operátorů
############################################################################
a = 5 > 3         #Výsledek porovnání (logická hodnota) ukládám do proměnné
a
# True
not a
# False
'' and 'cokoliv'  #Levý operand je False => jeho hodnota je výsledkem
# ''
1 and ''          #Levý operand je True => výsledkem je hodnota pravého
# ''
'' or 'cokoliv'   #Levý operand je False => výsledkem je hodnota pravého
# 'cokoliv'
1 or ''           #Levý operand je True => jeho hodnota je výsledkem
# 1
#V následujícím příkladu jsou hodnoty prvních tří operandů False =>
not a or 0 or "" or "poslední" # => výsledkem je hodnota posledního
# 'poslední'
# >>>



#Výpis 19.4: Definice metody run() v modulu game v balíčku game_v1i
############################################################################



#Výpis 19.5: Definice metody multirun() v modulu game v balíčku game_v1i
############################################################################



#Výpis 19.6: Definice modulu m19a_script
############################################################################



#Výpis 19.7: Reakce na spuštění modulu m19a_script v interaktivním režimu
############################################################################



#Výpis 19.8: Reakce na spuštění modulu m19a_script v příkazovém okně Windows
############################################################################



#Výpis 19.9: Vytvoření samostatné aplikace pomocí modu winapp a její spuštění
############################################################################



#Výpis 19.10: Definice modulu __main__ v souboru Game.pyz
############################################################################



#Výpis 19.11: Definice funkcí main() a main() v modulu game v balíčku game_v1i
############################################################################



############################################################################
##### KONEC #####
