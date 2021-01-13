#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game.game_v2b/actions.py
"""
Modul action má na starosti zpracování příkazů.
"""
from dbg import DBG
if DBG>0: print(f'===== Modul {__name__} ===== START')
############################################################################

from abc import ABCMeta, abstractmethod
from .   import world

from .texts import ActionName        as AN
from .texts import ActionDescription as AD
from .texts import ActionMessages    as AM


############################################################################

def execute_command(command: str) -> str:
    """Zpracuje zadaný příkaz a vrátí text zprávy pro uživatele.
    """
    command = command.strip()   # Smaže úvodní a závěrečné bílé znaky
    if command == '':
        return _execute_empty_command()
    elif is_active:
        return _execute_standard_command(command)
    else:
        return AM.start_wrong


def _execute_empty_command() -> str:
    """Zpracuje prázdný příkaz, tj. příkaz zadaný jako prázdný řetězec.
    Tento příkaz odstartuje hru, ale v běžící hře se nesmí použít.
    """
    global is_active
    if is_active:
        return AM.start_empty
    else:
        is_active = True
        _initialize()
        return AM.start_done


def _execute_standard_command(command: str) -> str:
    """Připraví parametry pro standardní akci hry,
    tuto akci spustí a vrátí zprávu vrácenou metodou dané akce.
    Byla-li zadána neexistující akce, vrátí oznámení.
    """
    words = command.lower().split()
    action_name = words[0]
    try:
        action  = _NAME_2_ACTION[action_name]
    except KeyError:
        return AM.command_wrong + action_name
    return action.execute(words)


def _initialize():
    """Inicializuje všechny součásti hry před jejím spuštěním."""
    world.initialize()


############################################################################
class _AAction(world.ANamed, metaclass=ABCMeta):
    """Společná rodičovská třída všech akcí."""

    def __init__(self, name: str, description: str):
        """Zapamatuje si název vytvářené akce a její stručný popis."""
        super().__init__(name)
        self.description = description

    @abstractmethod
    def execute(self, arguments: list[str]) -> str:
        """Realizuje reakci hry na zadání daného příkazu.
        Počet argumentů je závislý na konkrétní akci.
        """


############################################################################
class _End(_AAction):
    """Ukončuje hru a převede ji do pasivního stavu.
    """
    def __init__(self):
        """Jen si u rodiče zapamatuje svůj název a popis."""
        super().__init__("Konec", "Ukončení hry")

    def execute(self, arguments: str) -> str:
        global is_active
        is_active = False
        return AM.end_done


############################################################################
class _GoTo(_AAction):
    """Přesune hráče do zadaného sousedního prostoru.
    """
    def __init__(self):
        super().__init__(AN.goto, AD.goto)

    def execute(self, arguments: list[str]) -> str:
        """Ověří, že zadaný prostor patří mezi sousedy aktuálního
        prostoru, hráče do něj přemístí a vrátí příslušnou zprávu.
        Není-li cílový prostor sousedem, vrátí příslušné oznámení.
        """
        if len(arguments) < 2:
            return AM.goto_no
        destination_name = arguments[1]
        try:
            destination = world.current_place \
                               .name_2_neighbor[destination_name.lower()]
        except KeyError:
            return f'{AM.goto_wrong} {destination_name}'
        world.current_place = destination
        return f'{AM.goto_done}\n{destination.description}'


############################################################################
class _Help(_AAction):
    """Zobrazí definované akce a jejich popisy.
    """
    def __init__(self):
        super().__init__(AN.help, AD.help)

    def execute(self, arguments: list[str]) -> str:
        """Zobrazí definované akce a jejich popisy."""
        result = AM.help_done + '\n\n'
        for a in _NAME_2_ACTION.values():
            result += f'{a.name}\n{a.description}\n\n'
        return result


############################################################################
class _Put(_AAction):
    """Přesune h-objekt z košíku do aktuálního prostoru.
    """
    def __init__(self):
        super().__init__(AN.put, AD.put)

    def execute(self, arguments: list[str]) -> str:
        """Ověří existenci zadaného h-objektu v košíku a je-li tam,
        vyjme jej z košíku a přesune do aktuálního prostoru.
        """
        if len(arguments) < 2:
            return (AM.put_no)
        item_name = arguments[1]
        item      = world.BAG.remove_item(item_name)
        if item:
            world.current_place.add_item(item)
            return f'{AM.put_done} {item.name}'
        else:
            return f'{AM.put_wrong} {item_name}'


############################################################################
class _Take(_AAction):
    """Přesune h-objekt z aktuálního prostoru do košíku.
    """
    def __init__(self):
        super().__init__(AN.take, AD.take)

    def execute(self, arguments: list[str]) -> str:
        """Ověří existenci zadaného h-objektu v aktuálním prostoru
        a je-li tam, přesune jej do košíku.
        """
        if len(arguments) < 2:
            return AM.take_no
        item_name = arguments[1]
        item      = world.current_place.remove_item(item_name)
        if not item:
            return f'{AM.take_wrong} {item_name}'
        if item.weight == world.Item.HEAVY:
            world.current_place.add_item(item)
            return f'{AM.take_heavy} {item.name}'
        if world.BAG.try_add(item):
            return f'{AM.take_done} {item.name}'
        else:
            world.current_place.add_item(item)
            return f'{AM.take_full} {item.name}'


############################################################################

# Příznak toho, zda hra právě běží (True), anebo jen čeká na další spuštění
is_active: bool = False     # Na počátku hra čeká, až ji někdo spustí

# Slovník, jehož klíče jsou názvy akcí převedené na malá písmena
# a hodnotami jsou příslušné akce
_NAME_2_ACTION = {AN.end .lower(): _End(),
                  AN.goto.lower(): _GoTo(),
                  AN.put .lower(): _Put(),
                  AN.take.lower(): _Take(),
                  AN.help.lower(): _Help(),
                  }



############################################################################
if DBG>0: print(f'===== Modul {__name__} ===== STOP')
