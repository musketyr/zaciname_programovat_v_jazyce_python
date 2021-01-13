#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v1a/m07a_relative_import.py
"""
Pomocný importující modul pro demonstraci funkce relativního importu.
"""

print(f'===== Modul {__name__} ===== START')

from .          import game
from ..         import m07b_imported
from ..game_v1b import m07c_imported

print(f'===== Modul {__name__} ===== STOP')
