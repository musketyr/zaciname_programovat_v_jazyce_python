#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m11__test_define.py
"""
Příkazy a záznamy odpovědí zadávané ve výpisech kapitoly:
11  Definice testu hry
"""



#Výpis 11.1: Demonstrace použití přiřazovacího výrazu
############################################################################
lst_a = list('Python');   print(f'{lst_a = }')
# lst_a = ['P', 'y', 't', 'h', 'o', 'n']
lst_a.sort();   print(f'{lst_a = }')
# lst_a = ['P', 'h', 'n', 'o', 't', 'y']
(lst_b := list('Python')).sort();   print(f'{lst_b = }')
# lst_b = ['P', 'h', 'n', 'o', 't', 'y']
# >>>



#Výpis 11.2: Definice modulu game v balíčku game_v1b
############################################################################

# Definice je v souboru ./game/game_v1b/game.py



#Výpis 11.3: Prozatímní definice modulu world v balíčku game_v1b
############################################################################

# Definice je v souboru ./game/game_v1b/world.py



#Výpis 11.4: Definice funkce test_scenario() v modulu scenario v balíčku game_v1b
############################################################################

# Definice je v souboru ./game/game_v1b/scenarios.py



#Výpis 11.5: Definice metody _error() v modulu scenario v balíčku game_v1b
############################################################################

# Definice je v souboru ./game/game_v1b/scenarios.py



#Výpis 11.6: Import modulu scenarios v balíčku game_v1b
############################################################################
# =============================== RESTART: Shell ==============================
import game.game_v1b.scenarios
# ##### game - Společný rodičovský balíček balíčků jednotlivých verzí her
# ##### game.game_v1b - Balíček s verzí hry po definici testu hry na konci 11. kapitoly
# ===== Modul game.game_v1b.scenarios ===== START
# ===== Modul game.game_v1b.game ===== START
# ===== Modul game.game_v1b.game ===== STOP
# ===== Modul game.game_v1b.world ===== START
# ===== Modul game.game_v1b.world ===== STOP
# ===== Modul game.game_v1b.scenarios ===== STOP
# Spuštěna metoda game.game_v1b.game.game_v1b.scenarios.test_scenario
# 0.
# ------------------------------
#
# ------------------------------
# Prozatímní text
# ============================================================
#
# V 0. kroku neodpovídá: odpověď hry
#    Očekáváno: Vítejte!
# Toto je příběh o Červené Karkulce, babičce a vlkovi.
# Svými příkazy řídíte Karkulku, aby donesla věci babičce.
# Nebudete-li si vědět rady, zadejte znak ?.
#    Obdrženo:  Prozatímní text
# Stisk klávesy Enter aplikaci ukončí
# >>>



############################################################################
##### KONEC #####
