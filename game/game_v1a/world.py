#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v1a/world.py
"""
Modul world reprezentuje svět a obsahuje definice tříd prostorů,
předmětů (h-objektů) a batohu.
"""
print(f'===== Modul {__name__} ===== START')
############################################################################


############################################################################
class Item():
    """Instance reprezentují h-objekty v prostorech hry a v batohu."""

    def __init__(self, name: str):
        """Vytvoří h-objekt se zadaným názvem."""
        self.name = name


############################################################################
class Place:
    """Instance reprezentují prostory hry."""

    def __init__(self, name: str):
        """Vytvoří prostor se zadaným názvem."""
        self.name = name


############################################################################
class Bag:
    """Instance třídy reprezentuje batoh."""

    CAPACITY = 0    # Maximální kapacita batohu


############################################################################

# Aktuální prostor = prostor, v němž se hráč právě nachází
current_place = None

# Jediná instance batohu
BAG = Bag()


############################################################################
print(f'===== Modul {__name__} ===== STOP')
