#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v1e/world.py
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

    def __init__(self, name, **kwds):
        """Zapamatuje si jméno dané instance."""
        super().__init__(**kwds)
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
class AItemContainer(metaclass=ABCMeta):
    """Společný rodič tříd, jejichž instance mohou obsahovat h-objekty."""

    def __init__(self, initial_item_names: tuple[str], **kwds):
        """Rodič si zapamatuje název vytvářeného kontejneru a uloží názvy
        výchozí sady obsažených objektů v kontejneru pro inicializaci.
        """
        super().__init__(**kwds)
        # Počáteční názvy se ukládají včetně prefixů, aby se při
        # inicializaci daly použít jako argumenty initoru
        self.initial_item_names = tuple(initial_item_names)

    def initialize(self) -> None:
        """Připraví počáteční obsah kontejneru na počátku hry tak,
        že vytvoří a zapamatuje si objekty zadaných počátečních názvů.
        """
        # Následující dva atributy se vytvářejí až při první inicializaci
        self.items      = [Item(name) for name in self.initial_item_names]
        # Názvy se ukládají bez prefixů a převedené na malá písmena
        self.item_names = [item.name.lower() for item in self.items]

    def add_item(self, item: Item) -> None:
        """Přidá zadanou položku do seznamu a její název převedený
        na malá písmena uloží do seznamu názvů.
        """
        # Obě se uloží na konec seznamu, takže budou mít shodný index
        self.item_names.append(item.name.lower())
        self.items     .append(item)

    def remove_item(self, item_name: str) -> Item:
        """Vyjme položku se zadaným názvem ze seznamu položek a vrátí ji
        jako svoji funkční hodnotu. Není-li položka v seznamu, vrátí None.
        Při rozpoznávání názvů nesmí záležet na velikosti písmen.
        """
        try:
            # Zapamatované názvy jsou malými písmeny => musím převést zadaný
            index = self.item_names.index(item_name.lower())
        except ValueError:
            return None
        # Název i odpovídající objekt mají v seznamech shodné indexy
        self.item_names.pop(index)
        result = self.items.pop(index)
        return result


############################################################################
class Place(ANamed, AItemContainer):
    """Instance reprezentují prostory hry."""

    def __init__(self, name: str, description: str,
                 initial_neighbor_names: tuple[str],
                 initial_item_names:     tuple[str]):
        """Vytvoří prostor se zadaným názvem a stručným popisem napojený
        zpočátku na zadané sousedy a obsahující zadané h-objekty."""
        super().__init__(name=name, initial_item_names=initial_item_names)
        self.description            = description
        self.initial_neighbor_names = initial_neighbor_names
        self.name_2_neighbor        = dict.fromkeys(initial_neighbor_names)


############################################################################
class Bag(AItemContainer):
    """Instance třídy reprezentuje batoh."""

    CAPACITY = 2    # Maximální kapacita batohu

    def __init__(self):
        """Vytvoří batoh."""
        super().__init__(())


############################################################################

def initialize() -> None:
    """Inicializuje batoh a prostory."""
    for p in _NAME_2_PLACE.values():
        p.initialize()
    BAG.initialize()


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
