#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m17_remaining.py
"""
Příkazy a záznamy odpovědí zadávané ve výpisech kapitoly:
17  Co nám ještě chybí
"""



#Výpis 17.1: Začátek definice třídy Scenario v modulu scenarios v balíčku game_v1g
############################################################################



#Výpis 17.2: Začátek definice chybového scénáře v modulu scenarios v balíčku game_v1g
############################################################################



#Výpis 17.3: Definice dalších funkcí v modulu scenarios v balíčku game_v1g
############################################################################



#Výpis 17.4: Import modulu scenarios v balíčku game_v1g a zadání trojitého testu
############################################################################
from game.game_v1g import scenarios



#Výpis 17.5: Použití příkazu break
############################################################################
# >>> \
def demo_break():
    """Najde krok, v němž má aktuální prostor více jak dva sousedy."""
    for step in scenarios._HAPPY.steps:
        if len(step.neighbors) > 2:
            break
    print(f'{step.index}. {step.command}\n{step.neighbors}')

demo_break()
# 4. Jdi temný_les
# ('Les', 'Jeskyně', 'Chaloupka')
# >>>



#Výpis 17.6: Použití příkazu continue
############################################################################
# >>> \
def demo_continue():
    """Vypíše indexy a příkazy kroků bez argumentů."""
    for step in scenarios._MISTAKE.steps:
        if (len(step.command.split()) != 1):
            continue
        print(f'{step.index}. {step.command}')

demo_continue()
# 0. START
# 2. Vezmi
# 8. POLOŽ
# 10.   Jdi
# 12. ?
# 13. KONEC
# >>>



#Výpis 17.7: Konec zprávy o průběhu testu po opravě reakce na příkaz ukončení v balíčku game_v1g
############################################################################



#Výpis 17.7: Popisek
############################################################################



############################################################################
##### KONEC #####
