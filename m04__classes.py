#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m04__classes.py
"""
Příkazy a záznamy odpovědí zadávané ve výpisech kapitoly:
4  Základy OOP
"""



#Výpis 4.1: Demonstrační definice třídy
############################################################################
# >>> \
class DemoClass:
    """Demonstrační třída definující svůj datový a funkční atribut,
    tj. datovou proměnnou a metodu a vedle toho i důležité instanční metody.
    """
    print('Spouští se definice třídy DemoClass')

    c_atribut = 'Třídní datový atribut'
    instancí  = 0     # Počet doposud vytvořených instancí

    @staticmethod
    def c_mtd(id=None):
        """Metoda třídy - statická metoda."""
        print(f'Spuštěna třídní metoda DemoClass.c_mtd({id=})')

    def __init__(self):
        """Initor (přesněji inicializátor) instancí třídy DemoClass."""
        DemoClass.instancí = DemoClass.instancí + 1
        self.ID = DemoClass.instancí
        print(f'Instance vytvořena: {self}')

    def __repr__(self):
        """Vrátí textový podpis dané instance."""
        return f'DemoClass(ID={self.ID})'

    def i_mtd(self, id=None):
        """Instanční metoda."""
        print(f'Spuštěna metoda i_mtd({id=}) instance {self}')

    print('Konec definice třídy DemoClass')

# Spouští se definice třídy DemoClass
# Konec definice třídy DemoClass
# >>>



#Výpis 4.2: Vytvoření instancí třídy DemoClass a práce s nimi
############################################################################
DemoClass.c_mtd(111)
# Spuštěna třídní metoda DemoClass.c_mtd(id=111)
DemoClass.instancí
# 0
i1 = DemoClass();   i2 = DemoClass()
# Instance vytvořena: DemoClass(ID=1)
# Instance vytvořena: DemoClass(ID=2)
DemoClass.instancí
# 2
i1.i_mtd('Kvalifikováno instancí')
# Spuštěna metoda i_mtd(id='Kvalifikováno instancí') instance DemoClass(ID=1)
DemoClass.i_mtd(i2, 'Kvalifikováno třídou')
# Spuštěna metoda i_mtd(id='Kvalifikováno třídou') instance DemoClass(ID=2)
# >>>



#Výpis 4.3: Použití initoru s parametry
############################################################################
# >>> \
class Kvádr:
    """Instance reprezentují kvádry se zadanými rozměry.
    """
    def __init__(self, délka: float, šířka: float, výška: float):
        """Vytvoří a inicializuje požadovaný kvádr."""
        self.délka = délka
        self.šířka = šířka
        self.výška = výška

    def __repr__(self) -> str:
        """Vrátí textový podpis dané instance."""
        return f'Kvádr(délka={self.délka}, šířka={self.šířka}, ' \
               f'výška={self.výška})'

k1=Kvádr(1, 2, 3);   k2=Kvádr(10, 20, 30);   print(f'{k1 = }\n{k2 = }')
# k1 = Kvádr(délka=1, šířka=2, výška=3)
# k2 = Kvádr(délka=10, šířka=20, výška=30)
# >>>



#Výpis 4.4: Definice prázdné třídy
############################################################################
class PrázdnáOkomentovaná:
    """Dokumentační komentář s účelem třídy"""

PrázdnáOkomentovaná
# <class '__main__.PrázdnáOkomentovaná'>
# >>>



#Výpis 4.5: Definice a použití funkce pvt()
############################################################################
# >>> \
def pvt(expression: str) -> None:
    """Vytiskne zadaný výraz, jeho hodnotu a typ výsledku."""
    value = eval(expression)
    print(f'{expression} = {value} # type = {type(value)}')

celé = 1;   reálné = 1.5;   string = "String";   objekt = DemoClass()
# Instance vytvořena: DemoClass(ID=3)
pvt('celé');   pvt('reálné');   pvt('string');   pvt('objekt')
# celé = 1 # type = <class 'int'>
# reálné = 1.5 # type = <class 'float'>
# string = String # type = <class 'str'>
# objekt = DemoClass(ID=3) # type = <class '__main__.DemoClass'>
# >>>



############################################################################
##### KONEC #####
