#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/utils.py
"""
Modul s užitečnými funkcemi.
"""

# print('===== START načítání modulu', __name__, '=====')


def pvt(expression: str) -> None:
    """Vytiskne zadaný výraz, jeho hodnotu a typ výsledku.
    Mnemonika: print variable and type.
    """
    value = eval(expression)
    print(f'{expression} = {value} # type = {type(value)}')


def prSK(sk, obj, msg='') -> str:
    """Vytiskne oznámení o startu, resp, konci provádění volající metody.
       sk  = příznak tisku startu (True) či ukončení (False) těla metody
       obj = pojmenovaný objekt definující funkci, jež tuto metodu volá
       msg = Případná zpráva za vlastním oznámením
       Vrací doporučený text odsazení pro následující tisky
    """
    if not sk: prSK.level -= 1  # Trasovaná metoda končí, zmenšuji odsazení
    print(f'{prSK.level * prSK.sp}{obj.__name__} - ' +
          f'{"START" if sk else "KONEC"}' +
          f'{"" if msg == "" else f" - {msg}"}')
    if sk: prSK.level += 1  # Zvětšuji odsazení pro nižší hladinu
    return prSK.level * prSK.sp
prSK.level = 0      # Hladina vnoření pro nastavení odsazení
prSK.sp = '   '     # Text odsazení pro znázornění hladiny volání



# print('===== KONEC načítání modulu', __name__, '=====')
