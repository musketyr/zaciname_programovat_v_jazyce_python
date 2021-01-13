#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v2b/gui_0.py
"""
Sada funkcí umožňujících použít GUI v aplikaci
navržené původně pro příkazový řádek.
"""
from dbg import DBG
if DBG>0: print(f'===== Modul {__name__} ===== START')
############################################################################

import tkinter
from   tkinter import messagebox   as mb, \
                      simpledialog as sd


############################################################################

def get_command(answer: str) -> str:
    """Zobrazí uživateli zadanou odpověď hry,
    vyzve jej k zadání dalšího příkazu a vrátí zadaný příkaz.
    """
    if DBG>0: print(f'get_command: {answer = :s}')
    command = sd.askstring('Zadání příkazu', answer)
    if command == None: command = ''
    if DBG>0: print(f'get_command: {command = }')
    return command


def show_message(message: str) -> None:
    """Zobrazí uživateli zadanou zprávu."""
    if DBG>0: print(f'show_message: {message = :s}')
    mb.showinfo('Poděkování', message)
    if DBG>0: print(f'show_message: END')


def ask_question(message: str) -> bool:
    """Položí uživateli zadanou otázku a čeká na odpověď ANO/NE."""
    if DBG>0: print(f'ask_question: {message = :s}')
    answer = mb.askyesno('Dotaz', message)
    if DBG>0: print(f'ask_question: {answer = :s}')
    return answer


############################################################################

parent = tkinter.Tk()           # Vytvoří rodičovské okno,
parent.withdraw()               # a zhasne je


############################################################################
if DBG>0: print(f'===== Modul {__name__} ===== STOP')
