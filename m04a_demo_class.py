#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m04a_demo_class.py
"""
Definice třídy DemoClass uložená separátně v modulu m04a_DemoClass
"""



class DemoClass:
    """Demonstrační třída definující svůj datový a funkční atribut,
    tj. datovou proměnnou a metodu a vedle toho i důležité instanční metody
    """
    print('Spouští se definice třídy DemoClass')

    c_atribut = 'Třídní datový atribut'
    instancí  = 0     # Počet doposud vytvořených instancí

    @staticmethod
    def c_mtd(id=None):
        """Metoda třídy - statická metoda."""
        print(f'Spuštěna třídní metoda DemoClass.c_mtd({id=})')

    def i_mtd(self, id=None):
        """Instanční metoda."""
        print(f'Spuštěna metoda i_mtd({id=}) instance {self}')

    def __init__(self):
        """Initor (přesněji inicializátor) instancí třídy DemoClass."""
        DemoClass.instancí = DemoClass.instancí + 1
        self.ID = DemoClass.instancí
        print(f'Instance vytvořena: {self}')

    def __repr__(self):
        """Vrátí textový podpis dané instance."""
        return f'DemoClass(ID={self.ID})'

    print('Konec definice třídy DemoClass')
