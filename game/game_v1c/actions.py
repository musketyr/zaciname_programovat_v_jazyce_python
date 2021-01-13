#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v1c/actions.py
"""
Modul action má na starosti zpracování příkazů.
"""
print(f'===== Modul {__name__} ===== START')
############################################################################


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
        return ('Prvním příkazem není startovací příkaz.\n' +
                'Hru, která neběží, lze spustit pouze startovacím příkazem.')


def _execute_empty_command() -> str:
    """Zpracuje prázdný příkaz, tj. příkaz zadaný jako prázdný řetězec.
    Tento příkaz odstartuje hru, ale v běžící hře se nesmí použít.
    """
    global is_active
    if is_active:
        return 'Prázdný příkaz lze použít pouze pro start hry'
    else:
        is_active = True
        _initialize()
        return ('Vítejte!\n' 
                'Toto je příběh o Červené Karkulce, babičce a vlkovi.\n'
                'Svými příkazy řídíte Karkulku, aby donesla věci babičce.\n'
                'Nebudete-li si vědět rady, zadejte znak ?.')


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
        return 'Tento příkaz neznám: ' + action_name
    return action.execute(words)


def _initialize():
    """Inicializuje všechny součásti hry před jejím spuštěním."""
    # world.initialize()



############################################################################

# Příznak toho, zda hra právě běží (True), anebo jen čeká na další spuštění
is_active: bool = False     # Na počátku hra čeká, až ji někdo spustí

# Slovník, jehož klíče jsou názvy akcí převedené na malá písmena
# a hodnotami jsou příslušné akce
_NAME_2_ACTION = {}



############################################################################
print(f'===== Modul {__name__} ===== STOP')
