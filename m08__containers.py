#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m08__containers.py
"""
Příkazy a záznamy odpovědí zadávané ve výpisech kapitoly:
8  Kontejnery a práce s nimi
"""



#Výpis 8.0: Inicializace seance
############################################################################
# >>> \
def pvt(expression: str) -> None:
    """Vytiskne zadaný výraz, jeho hodnotu a typ výsledku."""
    value = eval(expression)
    print(f'{expression} = {value} # type = {type(value)}')



#Výpis 8.1: Vytváření seznamů
############################################################################
prvočísla_L = [3, 5, 7, 11];   pvt('prvočísla_L')
# prvočísla_L = [3, 5, 7, 11] # type = <class 'list'>
pořadí_L = ['Nultý', 'První', 'Druhý', 'Třetí'];   pvt('pořadí_L')
# pořadí_L = ['Nultý', 'První', 'Druhý', 'Třetí'] # type = <class 'list'>
písmena_L = list('Python');   pvt('písmena_L')
# písmena_L = ['P', 'y', 't', 'h', 'o', 'n'] # type = <class 'list'>
mocniny_L = [n*n for n in prvočísla_L];   pvt('mocniny_L')
# mocniny_L = [9, 25, 49, 121] # type = <class 'list'>
prázdný_L = [];   pvt('prázdný_L')
# prázdný_L = [] # type = <class 'list'>
# >>>



#Výpis 8.2: Vytváření n-tic
############################################################################
prvočísla_T = 3, 5, 7, 11;   pvt('prvočísla_T')
# prvočísla_T = (3, 5, 7, 11) # type = <class 'tuple'>
písmena_T = tuple('Python');   pvt('písmena_T')
# písmena_T = ('P', 'y', 't', 'h', 'o', 'n') # type = <class 'tuple'>
mocniny_T = (n*n for n in prvočísla_L);   pvt('mocniny_T')
# mocniny_T = <generator object <genexpr> at 0x0000024D5B887900> # type = <class 'generator'>
mocniny_T = tuple(n*n for n in prvočísla_L);   pvt('mocniny_T')
# mocniny_T = (9, 25, 49, 121) # type = <class 'tuple'>
prázdná_T = ();   pvt('prázdná_T')
# prázdná_T = () # type = <class 'tuple'>
číslo = (135);   ntice = (135,);   pvt('číslo');   pvt('ntice')
# číslo = 135 # type = <class 'int'>
# ntice = (135,) # type = <class 'tuple'>
# >>>



#Výpis 8.3: Vytváření množin
############################################################################
prvočísla_S = {3, 5, 7, 11};   pvt('prvočísla_S')
# prvočísla_S = {11, 3, 5, 7} # type = <class 'set'>
pořadí_S = {'Nultý', 'První', 'Druhý', 'Třetí'};   pvt('pořadí_S')
# pořadí_S = {'Třetí', 'První', 'Druhý', 'Nultý'} # type = <class 'set'>
písmena_S = set('Python');   pvt('písmena_S')
# písmena_S = {'y', 'n', 'P', 'o', 't', 'h'} # type = <class 'set'>
mocniny_S = {n * n for n in prvočísla_S};   pvt('mocniny_S')
# mocniny_S = {121, 49, 9, 25} # type = <class 'set'>
prázdná_S = {};   pvt('prázdná_S')
# prázdná_S = {} # type = <class 'dict'>
prázdná_S = set();   pvt('prázdná_S')
# prázdná_S = set() # type = <class 'set'>
písmena_F = frozenset('Python');   pvt('písmena_F')
# písmena_F = frozenset({'y', 'n', 'P', 'o', 't', 'h'}) # type = <class 'frozenset'>
mocniny_F = frozenset(n * n for n in prvočísla_S);   pvt('mocniny_F')
# mocniny_F = frozenset({121, 49, 9, 25}) # type = <class 'frozenset'>
# >>>



#Výpis 8.4: Vytváření slovníků
############################################################################
pořadí_D = {'Druhý':2, 'První':1, 'Nultý':0};   pvt('pořadí_D')
# pořadí_D = {'Druhý': 2, 'První': 1, 'Nultý': 0} # type = <class 'dict'>
dvojice_L = [(n, n*n) for n in prvočísla_S];   pvt('dvojice_L')
# dvojice_L = [(11, 121), (3, 9), (5, 25), (7, 49)] # type = <class 'list'>
dvojice_D = dict(dvojice_L);   pvt('dvojice_D')
# dvojice_D = {11: 121, 3: 9, 5: 25, 7: 49} # type = <class 'dict'>
mocniny_D = {n:n*n for n in prvočísla_T};   pvt('mocniny_D')
# mocniny_D = {3: 9, 5: 25, 7: 49, 11: 121} # type = <class 'dict'>
prázdný_D = {};   pvt('prázdný_D')
# prázdný_D = {} # type = <class 'dict'>
# >>>



#Výpis 8.5: Získání prvku z kontejneru pomocí indexu
############################################################################
f'{pořadí_L[3]=}, {mocniny_T[2]=}, {pořadí_D["První"]=}'
# 'pořadí_L[3]=\'Třetí\', mocniny_T[2]=49, pořadí_D["První"]=1'
def kontejner(název: str):
    """Vrátí odkaz na kontejner se zadaným názvem."""
    return eval(název)

názvy = ('prvočísla_L', 'písmena_T', 'mocniny_L')
print(f'{kontejner("názvy[1]")[0] = }')
# kontejner("názvy[1]")[0] = 'p'
# >>>



#Výpis 8.6: Procházení kontejnerem pomocí příkazu for
############################################################################
# >>> \
def prvky_pod_sebou(kontejner):
    """Vypíše číslovaně prvky kontejneru, každý na samostatný řádek."""
    index = 0
    for prvek in kontejner:
        print(f'{index}. {prvek}')
        index = index + 1

prvky_pod_sebou(pořadí_L)
# 0. Nultý
# 1. První
# 2. Druhý
# 3. Třetí
prvky_pod_sebou(pořadí_D)
# 0. Druhý
# 1. První
# 2. Nultý
prvky_pod_sebou(prvočísla_S)
# 0. 11
# 1. 3
# 2. 5
# 3. 7
prvky_pod_sebou(prázdný_L)
# >>>



#Výpis 8.7: Použití hvězdičkového parametru
############################################################################
def hp(*par: int) -> None:
    print(f'Obdržené argumenty: {par=}')

hp(3, 2, 1, 0)
# Obdržené argumenty: par=(3, 2, 1, 0)
# >>>



#Výpis 8.8: Použití hvězdičkového argumentu
############################################################################
def ha(a, b, c, *zbytek) -> None:
    print(f'Obdržené argumenty: {a=}, {b=}, {c=}, {zbytek=}')

ha(*range(6))
# Obdržené argumenty: a=0, b=1, c=2, zbytek=(3, 4, 5)
# >>>



#Výpis 8.9: Použití dvouhvězdičkového parametru
############################################################################
def dhp(**args) -> None:
    print(f'Zadané argumenty: {args=}')

dhp(a=1, b=2, c=3)
# Zadané argumenty: args={'a': 1, 'b': 2, 'c': 3}
# >>>



#Výpis 8.10: Použití dvouhvězdičkového argumentu
############################################################################
def dha(x: int, y: int, z: int) -> None:
    print(f'Souřadnice: {x=}, {y=}, {z=}')

pozice = {'z': 30, 'x': 100, 'y': 2}
dha(**pozice)
# Souřadnice: x=100, y=2, z=30
# >>>



#Výpis 8.11: Specifika slovníků
############################################################################
název_2_číslo = pořadí_D;   název_2_číslo
# {'Druhý': 2, 'První': 1, 'Nultý': 0}
číslo_2_mocnina = dvojice_D;   číslo_2_mocnina
# {11: 121, 3: 9, 5: 25, 7: 49}
název_číslo = {dvojice for dvojice in název_2_číslo.items()};   název_číslo
# {('Nultý', 0), ('Druhý', 2), ('První', 1)}
názvy = tuple(název for název in název_2_číslo.keys());   názvy
# ('Druhý', 'První', 'Nultý')
mocniny = [mocnina for mocnina in číslo_2_mocnina.values()];   mocniny
# [121, 9, 25, 49]
# >>>



############################################################################
##### KONEC #####
