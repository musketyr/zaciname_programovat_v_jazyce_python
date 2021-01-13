#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v1h/game.py
"""
Modul reprezentuje hru.
"""
print(f'===== Modul {__name__} ===== START')
############################################################################

from . import world, actions


############################################################################

print_state = False

def execute_command(command: str) -> str:
    """Zpracuje zadaný příkaz a vrátí string se zprávou pro uživatele."""
    message = actions.execute_command(command) \
            + '\n' + 30*'-' \
            + (('\n' + current_state()) if print_state else '')
    return message


def current_state() -> str:
    """Vrátí string s popisem aktuálního stavu, tj. s názvem
    aktuálního prostoru, jeho sousedů a h-objektů a obsahu batohu.
    """
    cp = world.current_place
    result = (f'Aktuální prostor: {cp}\n'
              f'Sousedé prostoru: {list(cp.name_2_neighbor.values())}\n'
              f'Předměty v prostoru: {cp.items}\n'
              f'Předměty v batohu:   {world.BAG.items}\n')
    return result


############################################################################
print(f'===== Modul {__name__} ===== STOP')
