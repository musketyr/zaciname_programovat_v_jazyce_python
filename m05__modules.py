#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m05__modules.py
"""
Příkazy a záznamy odpovědí zadávané ve výpisech kapitoly:
5  Moduly a práce s nimi
"""



#Výpis 5.1: Importování modulů
############################################################################
#!# turtle.Turtle()   # Před importem modulu jsou jeho atributy nepoužitelné
# Traceback (most recent call last):
#   File "<pyshell#1>", line 1, in <module>
#     turtle.Turtle()   # Před importem modulu jsou jeho atributy nepoužitelné
# NameError: name 'turtle' is not defined
import turtle
t = turtle.Turtle()      # Otevře se okno, v jehož středu se objeví želva
t.forward(50); t.left(90); t.forward(50)   # Nakreslí čáru doprava a vzhůru
# >>>



#Výpis 5.2: Uložení odkazu na modul pod jiným názvem
############################################################################
import turtle as želva    # Vytvoří proměnnou želva, do níž uloží odkaz na modul
ž = želva.Turtle()        # Ve středu okna se objeví nová želva
ž.forward(-50); ž.left(90); ž.forward(50)    # Nakreslí čáru doleva a vzhůru
korytnačka = želva        # Korytnačka = želva slovensky
k = korytnačka.Turtle()   # Ve středu okna se objeví třetí želva
k.left(90); k.forward(50) # Nakreslí čáru vzhůru
# >>>



#Výpis 5.3: Import zadaných objektů ze zadaného modulu
############################################################################
from turtle import Turtle as Želva  # Proměnná Želva odkazuje na třídu turtle.Turtle
žž = Želva()                        # Vytvoří se čtvrtá želva
žž.right(90); žž.forward(50)        # Nakreslí čáru dolů
# >>>



#Výpis 5.4: Modul m05a_module_demo sloužící k demonstraci chování Pythonu
#           při zavádění modu-lu
############################################################################
#
# Zdrojový kód modulu m05a_module_demo
#



#Výpis 5.5: Použití modulu
############################################################################
import m05a_module_demo as m05a
# ===== START načítání modulu m05a_module_demo =====
# Při zavádění modulu se hodnoty výrazových příkazů nezobrazují
# Chcete-li objekt zobrazit, musíte jej explicitně vytisknout
#  text='Datový atribut modulu m05a_module_demo'
# ===== KONEC načítání modulu m05a_module_demo =====
m05a
# <module 'm05a_module_demo' from 'Q:\\65_PGM\\65_PYT\\m05a_module_demo.py'>
m05a.text
# 'Datový atribut modulu m05a_module_demo'
m05a.MCls
# <class 'm05a_module_demo.MCls'>
m05a.MCls.s_mtd()
    #
    # Spuštěna metoda s_mtd()
    #     definované ve třídě MCls
    #        definované v modulu m05a_module_demo
from m05a_module_demo import *
MCls.s_mtd()
#
#     Spuštěna metoda s_mtd()
#         definované ve třídě MCls
#            definované v modulu m05a_module_demo
# >>>



#Výpis 5.6: Načtení opravené verze modulu m05a_module_demo
############################################################################
from importlib import reload
reload(m05a)
# ===== START načítání modulu m05a_module_demo =====
# ===== KONEC načítání modulu m05a_module_demo =====
# <module 'm05a_module_demo' from 'Q:\\65_PGM\\65_PYT\\m05a_module_demo.py'>
MCls.s_mtd()
    #
    # Spuštěna metoda s_mtd()
    #     definované ve třídě MCls
    #        definované v modulu m05a_module_demo
m05a.MCls.s_mtd()
# Spuštěna metoda s_mtd()
#     definované ve třídě MCls
#        definované v modulu m05a_module_demo
from m05a_module_demo import *
MCls.s_mtd()
    # Spuštěna metoda s_mtd()
    #     definované ve třídě MCls
    #        definované v modulu m05a_module_demo
# >>>



############################################################################
##### KONEC #####
