#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game.game_v2a/game.py
"""
Modul reprezentuje hru.
"""
from dbg import DBG
if DBG>0: print(f'===== Modul {__name__} ===== START')
############################################################################

from . import world, actions

from .texts import GameMessages   as GM

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
    result = (f'{GM.state_cp} {cp}\n'
              f'{GM.state_pn} {list(cp.name_2_neighbor.values())}\n'
              f'{GM.state_pi} {cp.items}\n'
              f'{GM.state_bi} {world.BAG.items}\n')
    return result


def run():
    """Spustí hru ovládanou z příkazového řádku."""
    command = ''
    while True:     # Nekonečný cyklus hraní hry
        message = execute_command(command)
        print(message)
        if not actions.is_active:
            break    # Hra je ukončena => vyskakujeme z cyklu ---------->
            # Předchozí příkaz by mohl být i return, což by bylo lepší,
            # protože v danou chvíli hra beztak končí
        command = input(GM.enter_cmd + ' ')


def multirun():
    """Umožní opakované spuštění hry ovládané z příkazového řádku."""
    while True:
        run()
        while True:
            answer = input(GM.multi_more).strip()
            if (len(answer) > 0)   and   (answer[0] in '01ANan'):
                break       # Výskok z vnitřního cyklu    ---------->
            print(GM.multi_wrong)
        if answer[0] in '0Nn':
            break       # Výskok z vnějšího cyklu    ---------->
        print(f'\n{GM.multi_yes}\n')
    print(f'\n{GM.multi_no}\n')


def main():
    """Spustí aplikaci podle zadaných argumentů příkazového řádku."""
    args = sys.argv
    if DBG>0: print(f'main - argumenty: {args}')
    if '-h' in args:
        help()
        return
    global print_state
    print_state = ('-s' in args)
    if '-m' in args:
        multirun()
    else:
        run()


def help():
    """Zobrazí nápovědu k aplikaci."""
    print(GM.cmd_help)


############################################################################
if DBG>0: print(f'===== Modul {__name__} ===== STOP')
