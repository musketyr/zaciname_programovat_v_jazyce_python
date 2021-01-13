#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game.game_v2b/world.py
"""
Modul world reprezentuje svět a obsahuje definice tříd prostorů,
předmětů (h-objektů) a batohu.
"""
from dbg import DBG
if DBG>0: print(f'===== Modul {__name__} ===== START')
############################################################################

from abc import ABCMeta

from .texts import PlaceName         as PN
from .texts import PlaceDescription  as PD
from .texts import ItemWeight        as IW


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

    HEAVY: int = 999    # Váha nepřenositelného h-objektu

    def __init__(self, name: str):
        """Vytvoří h-objekt se zadaným názvem. Podle prvního znaku
        pozná přenositelnost objektu a nastaví jeho váhu.
        Zbylé znaky argumentu si zapamatuje jako jeho název.
        """
        prefix    = name[0]   # Předpona indikující další vlastnosti
        real_name = name[1:]  # Název h-objektu používaný v příkazech
        super().__init__(real_name)
        self.weight = 1 if prefix == IW.light else Item.HEAVY


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
        self.item_names         = list (initial_item_names)

    def initialize(self):
        """Připraví počáteční obsah kontejneru na počátku hry tak,
        že vytvoří a zapamatuje si objekty zadaných počátečních názvů.
        """
        # Následující dva atributy se vytvářejí až při první inicializaci
        self.items      = [Item(name) for name in self.initial_item_names]
        # Názvy se ukládají bez prefixů a převedené na malá písmena
        self.item_names = [item.name.lower() for item in self.items]

    def add_item(self, item: Item):
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

    def initialize(self):
        """Inicializuje prostor na počátku hry.
        """
        AItemContainer.initialize(self)    # Inicializuje h-objekty
        # Inicializuje sousedy, atribut se vytváří až při první inicializaci
        self.name_2_neighbor = {name.lower() : _NAME_2_PLACE[name.lower()]
                                for name in self.initial_neighbor_names}


############################################################################
class Bag(AItemContainer):
    """Instance třídy reprezentuje batoh."""

    CAPACITY = 2    # Maximální kapacita batohu

    def __init__(self):
        """Vytvoří batoh."""
        super().__init__(())

    def try_add(self, item: Item) -> bool:
        """Pokusí se vložit do batohu zadaný objekt a vrátí informaci
        o tom, zda se tam ještě vešel.
        """
        if len(self.items) + item.weight  > Bag.CAPACITY:
            return False
        self.add_item(item)
        return True


############################################################################

def initialize():
    """Inicializuje batoh a prostory."""
    global current_place
    current_place = _NAME_2_PLACE['domeček']
    for p in _NAME_2_PLACE.values():
        p.initialize()
    BAG.initialize()


############################################################################

# Slovník, jehož klíče jsou názvy prostorů a hodnotami jsou prostory
# Obsahuje všechny prostory hry včetně těch přímo nedosažitelných
# (v této hře takové zatím nejsou, ale mohl by to být třeba košík)
_NAME_2_PLACE = {p.name.lower() : p for p in (
    Place(PN.house,
          PD.house,
          (PN.wood,),
          (IW.cake, IW.vine, IW.table, IW.doll, ),
         ),
    Place(PN.wood,
          PD.wood,
          (PN.house, PN.forest,),
          (IW.raspberry, IW.strawberry, IW.well, ),
         ),
    Place(PN.forest,
          PD.forest,
          (PN.wood, PN.cave, PN.cottage, ),
          (IW.wolf, ),
          ),
    Place(PN.cottage,
          PD.cottage,
          (PN.forest, ),
          (IW.bed, IW.table, IW.granny, ),
         ),
    Place(PN.cave,
          PD.cave,
          (PN.forest, ),
          (),
         ),
)}

# Aktuální prostor = prostor, v němž se hráč právě nachází
current_place = None

# Jediná instance batohu
BAG = Bag()


############################################################################
if DBG>0: print(f'===== Modul {__name__} ===== STOP')
