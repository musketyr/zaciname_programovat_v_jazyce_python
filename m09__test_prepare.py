#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m09__test_prepare.py
"""
Příkazy a záznamy odpovědí zadávané ve výpisech kapitoly:
9  Připravujeme test
"""



#Výpis 9.1: Definice třídy _Step v modulu scenarios
############################################################################

# Definice je v souboru ./game/game_v1b/scenarios.py



#Výpis 9.2: Definice počátku n tice reprezentující „šťastný scénář“ vybrané hry
############################################################################

# Definice je v souboru ./game/game_v1b/scenarios.py



#Výpis 9.3: Definice metody simulate_simple()
############################################################################

# Definice je v souboru ./game/game_v1a/scenarios.py



#Výpis 9.4: Import modulu scenarios v balíčku game_v1a a spuštění metody simulate_simple()
############################################################################
# =============================== RESTART: Shell ==============================
from game.game_v1a.scenarios import simulate_simple
# ##### game - Společný rodičovský balíček balíčků jednotlivých verzí her
# ##### game.game_v1a - Balíček s verzí hry na konci 7., resp. 9. kapitoly
#       po prvotní analýze (7. kapitola) a
#       po návrhu šťastného scénáře a simulačních metod (9. kapitola)
# ===== Modul game.game_v1a.scenarios ===== START
# ===== Modul game.game_v1a.scenarios ===== STOP
simulate_simple()
# 0.
# ------------------------------
# Vítejte!
# Toto je příběh o Červené Karkulce, babičce a vlkovi.
# Svými příkazy řídíte Karkulku, aby donesla věci babičce.
# Nebudete-li si vědět rady, zadejte znak ?.
# ============================================================
# 1. Vezmi víno
# ------------------------------
# Karkulka dala do košíku objekt: Víno
# ============================================================
# 2. Vezmi bábovka
# ------------------------------
# Karkulka dala do košíku objekt: Bábovka
# ============================================================
# 3. Jdi LES
# ------------------------------
# Karkulka se přesunula do prostoru:
# Les s jahodami, malinami a pramenem vody
# ============================================================
# ...



#Výpis 9.5: Definice metody simulate_with_state()
############################################################################

# Definice je v souboru ./game/game_v1a/scenarios.py



#Výpis 9.6: Začátek simulace vypsané metodou simulate_with_state()
############################################################################
from game.game_v1a.scenarios import simulate_with_state as sws
sws()
# 0.
#
# ------------------------------
# Vítejte!
# Toto je příběh o Červené Karkulce, babičce a vlkovi.
# Svými příkazy řídíte Karkulku, aby donesla věci babičce.
# Nebudete-li si vědět rady, zadejte znak ?.
# ------------------------------
# Aktuální prostor: Domeček
# Sousedé prostoru: ('Les',)
# Předměty v prostoru: ('Bábovka', 'Víno', 'Stůl', 'Panenka')
# Předměty v batohu:   ()
# ============================================================
# 1.
# Vezmi víno
# ------------------------------
# Karkulka dala do košíku objekt: Víno
# ------------------------------
# Aktuální prostor: Domeček
# Sousedé prostoru: ('Les',)
# Předměty v prostoru: ('Bábovka', 'Stůl', 'Panenka')
# Předměty v batohu:   ('Víno',)
# ============================================================
# ...



############################################################################
##### KONEC #####
