#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v1i/game.py
"""
Modul reprezentuje hru.
"""
from dbg import DBG
if DBG>0: print(f'===== Modul {__name__} ===== START')
############################################################################

from . import world, actions
import sys


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


def run() -> None:
    """Spustí hru ovládanou z příkazového řádku."""
    command = ''
    while True:     # Nekonečný cyklus hraní hry
        message = execute_command(command)
        print(message)
        if not actions.is_active:
            break    # Hra je ukončena => vyskakujeme z cyklu ---------->
            # Předchozí příkaz by mohl být i return, což by bylo lepší,
            # protože v danou chvíli hra beztak končí
        command = input('Zadejte příkaz: ')


def multirun() -> None:
    """Umožní opakované spuštění hry ovládané z příkazového řádku."""
    while True:
        run()
        while True:
            answer = input('Chcete si zahrát ještě jednou (A/N): ').strip()
            if (len(answer) > 0)   and   (answer[0] in '01ANan'):
                break       # Výskok z vnitřního cyklu    ---------->
            print('Odpověď musí začínat některým ze znaků "01ANan"\n'
                  'Zkuste odpovědět znovu.')
        if answer[0] in '0Nn':
            break       # Výskok z vnějšího cyklu    ---------->
        print('\nDobře, zahrajeme si ještě jednou.\n')
    print('\nJeště jednou děkuji za hru.\nNa shledanou.')


def main() -> None:
    """Spustí aplikaci podle zadaných argumentů příkazového řádku."""
    args = sys.argv
    if DBG>=0: print(f'main – argumenty příkazového řádku: {args}')
    if '-h' in args:
        help()
        return
    global print_state
    print_state = ('-s' in args)
    if '-m' in args:
        multirun()
    else:
        run()


def help() -> None:
    """Zobrazí nápovědu k aplikaci."""
    print('Aplikace představuje jednoduchou konverzační hru.\n'
          'Při spuštění můžete zadat následující argumenty:\n'
          '-h  Spustí tuto nápovědu\n'
          '-m  Umožní zahrát si hru po skončení znovu\n'
          '-s  Součástí odpovědi hry na zadání příkazu bude informace\n'
          '    o aktuálním stavu světa hry')


############################################################################
if DBG>0: print(f'===== Modul {__name__} ===== STOP')
