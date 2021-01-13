#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v1d/world.py
"""
Modul world reprezentuje svět a obsahuje definice tříd prostorů,
předmětů (h-objektů) a batohu.
"""
print(f'===== Modul {__name__} ===== START')
############################################################################

from abc import ABCMeta


############################################################################
class ANamed(metaclass=ABCMeta):
    """Společný rodič všech tříd s pojmenovanými instancemi,
    v případě našich textových her je to rodič h-objektů, prostorů a akcí.
    """

    def __init__(self, name):
        """Zapamatuje si jméno dané instance."""
        self.name = name

    def __repr__(self) -> str:
        """Pojmenovaný objekt se bude podepisovat svým názvem."""
        return self.name


############################################################################
class Item(ANamed):
    """Instance reprezentují h-objekty v prostorech hry a v batohu."""

    def __init__(self, name: str):
        """Vytvoří h-objekt se zadaným názvem."""
        super().__init__(name)


############################################################################
class Place(ANamed):
    """Instance reprezentují prostory hry."""

    def __init__(self, name: str, description: str,
                 initial_neighbor_names: tuple[str],
                 initial_item_names:     tuple[str]):
        """Vytvoří prostor se zadaným názvem a stručným popisem napojený
        zpočátku na zadané sousedy a obsahující zadané h-objekty."""
        super().__init__(name)
        self.description            = description
        self.initial_neighbor_names = initial_neighbor_names
        self.initial_item_names     = initial_item_names
        self.name_2_neighbor        = dict.fromkeys(initial_neighbor_names)
        self.item_names             = list(initial_item_names)


############################################################################
class Bag:
    """Instance třídy reprezentuje batoh."""

    CAPACITY = 0    # Maximální kapacita batohu

    def __init__(self):
        """Vytvoří batoh."""
        self.item_names = []


############################################################################

def initialize():
    """Inicializuje batoh a prostory."""


############################################################################

# Slovník, jehož klíče jsou názvy prostorů a hodnotami jsou prostory.
# Obsahuje všechny prostory hry včetně těch přímo nedosažitelných
# (v této hře takové zatím nejsou, ale mohl by to být třeba košík).
_NAME_2_PLACE = {p.name.lower() : p for p in (
    Place('Domeček',
          'Domeček, kde bydlí Karkulka',
          ('Les',),
          ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),
         ),
    Place('Les',
          'Les s jahodami, malinami a pramenem vody',
          ('Domeček', 'Temný_les',),
          ('Maliny', 'Jahody', 'Studánka', ),
         ),
    Place('Temný_les',
          'Temný_les s jeskyní a číhajícím vlkem',
          ('Les', 'Jeskyně', 'Chaloupka', ),
          ('Vlk', ),
          ),
    Place('Chaloupka',
          'Chaloupka, kde bydlí babička',
          ('Temný_les', ),
          ('Postel', 'Stůl', 'Babička', ),
         ),
    Place('Jeskyně',
          'Jeskyně, kde v zimě přespává medvěd',
          ('Temný_les', ),
          (),
         ),
)}

# Aktuální prostor = prostor, v němž se hráč právě nachází
current_place = _NAME_2_PLACE['domeček']

# Jediná instance batohu
BAG = Bag()


############################################################################
print(f'===== Modul {__name__} ===== STOP')
