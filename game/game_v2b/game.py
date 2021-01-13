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
class Console:
    """Definuje základní funkce pro standardní vstup a výstup."""

    @staticmethod
    def get_command(answer: str) -> str:
        """Zobrazí uživateli zadanou odpověď hry,
        vyzve jej k zadání dalšího příkazu a vrátí zadaný příkaz.
        """
        return input(f'answer\n----------\n{GM.enter_cmd} ')

    @staticmethod
    def show_message(message: str) -> None:
        """Zobrazí uživateli zadanou zprávu."""
        print(message)

    @staticmethod
    def ask_question(question: str) -> bool:
        """Položí uživateli zadanou otázku a čeká na odpověď ANO/NE."""
        while True:
            answer = input(question).strip()
            if (len(answer) > 0)   and   (answer[0] in '01ANan'):
                break       # ---------->
            print(GM.multi_wrong)
        return answer[0] in '1Aa'


############################################################################

"""Indikátor tisku stavových informací jako součásti výstupu."""
print_state = False

"""Objekt zprostředkovávající vstup a výstup."""
io = Console


############################################################################

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


def run() -> None:
    """Spustí hru ovládanou z příkazového řádku."""
    command = ''
    while True:     # Nekonečný cyklus hraní hry
        answer = execute_command(command)
        if not actions.is_active:
            io.show_message(answer)
            return    # Hra je ukončena => vyskakujeme z cyklu ==========>
        command = io.get_command(answer)


def multirun() -> None:
    """Umožní opakované spuštění hry ovládané z příkazového řádku."""
    while True:
        run()
        answer = io.ask_question(GM.multi_more)
        if not answer:      # Už nechce pokračovat
            print(f'\n{GM.multi_no}\n')
            return          # ==========>
        print(f'\n{GM.multi_yes}\n')


def main() -> None:
    """Spustí aplikaci podle zadaných argumentů příkazového řádku."""
    args = sys.argv
    if DBG>0: print(f'main - argumenty: {args}')
    if '-h' in args:
        help()
        return
    if '-d' in args:
        global io
        from . import gui_0
        io = gui_0

    global print_state
    print_state = ('-s' in args)

    if '-m' in args:
        multirun()
    else:
        run()


def mainw() -> None:
    """Spustí aplikaci v okenním režimu."""
    import sys
    sys.argv = '-d'
    print('Spouštím aplikaci v okenním režimu')
    main()


def help():
    """Zobrazí nápovědu k aplikaci."""
    print(GM.cmd_help)


############################################################################
if DBG>0: print(f'===== Modul {__name__} ===== STOP')
