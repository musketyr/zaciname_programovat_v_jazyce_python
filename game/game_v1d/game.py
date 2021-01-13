#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v1d/game.py
"""
Modul reprezentuje hru.
"""
print(f'===== Modul {__name__} ===== START')
############################################################################

from . import actions


############################################################################

def execute_command(command: str) -> str:
    """Zpracuje zadaný příkaz a vrátí string se zprávou pro uživatele."""
    message = actions.execute_command(command)
    return message


############################################################################
print(f'===== Modul {__name__} ===== STOP')
