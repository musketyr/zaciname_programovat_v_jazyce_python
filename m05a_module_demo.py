#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/m05a_module_demo.py
"""
Modul demonstrující základní pravidla pro tvorbu modulů,
jejich zavádění a následnou práci s nimi.
"""

print('===== START načítání modulu', __name__, '=====')

text = f'Datový atribut modulu {__name__}'
print("Při zavádění modulu se hodnoty výrazových příkazů nezobrazují")
text  # Výrazový příkaz => při zavádění modulu se nevytiskne
print('Chcete-li objekt zobrazit, musíte jej explicitně vytisknout\n',
      f"{text=}")

def m_fce(arg='Nezadán'):
    """Samostatně definovaná funkce = funkční atribut modulu."""
    print(f'Spuštěna funkce m_fce({arg=}) definovaná v modulu {__name__}')

class MCls:
    """Třída definovaná v modulu."""

    @staticmethod
    def s_mtd():
        """Statická metoda třídy MCls."""
        print(f"""
    Spuštěna metoda {MCls.s_mtd.__name__}()
        definované ve třídě {MCls.__name__}
           definované v modulu {__name__}""")

print('===== KONEC načítání modulu', __name__, '=====')
