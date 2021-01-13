#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v2x/module_template.py
"""
Dokumentační komentář modulu.
"""
from dbg import DBG
if DBG>0: print(f'===== Modul {__name__} ===== START')
############################################################################


############################################################################
class PlaceName:
    """Názvy prostorů hry"""
    house   = 'Domeček'
    wood    = 'Les'
    forest  = 'Temný_les'
    cottage = 'Chaloupka'
    cave    = 'Jeskyně'

class PlaceDescription:
    """Stručné popisy prostorů hry"""
    house   = 'Domeček, kde bydlí Karkulka'
    wood    = 'Les s jahodami, malinami a pramenem vody'
    forest  = 'Temný_les s jeskyní a číhajícím vlkem'
    cottage = 'Chaloupka, kde bydlí babička'
    cave    = 'Jeskyně, kde v zimě přespává medvěd'

class ItemName:
    """Názvy h-objektů použitých ve hře."""
    cake        = 'Bábovka'
    wine        = 'Víno'
    table       = 'Stůl'
    doll        = 'Panenka'
    wolf        = 'Vlk'
    raspberry   = 'Maliny'
    strawberry  = 'Jahody'
    well        = 'Studánka'
    bed         = 'Postel'
    granny      = 'Babička'

class ItemWeight:
    """Názvy h-objektů doplněné o informační prefixy."""
    light = '_'  # Prefix označující běžný h-objekt
    heavy = '#'  # Prefix označující nezvednutelný h-objekt
    cake        = light + ItemName.cake
    wine        = light + ItemName.wine
    table       = heavy + ItemName.table
    doll        = light + ItemName.doll
    wolf        = heavy + ItemName.wolf
    raspberry   = light + ItemName.raspberry
    strawberry  = light + ItemName.strawberry
    well        = heavy + ItemName.well
    bed         = heavy + ItemName.bed
    granny      = heavy + ItemName.granny

class ActionName:
    """Názvy jednotlivých akcí."""
    end  = 'Konec'
    goto = 'Jdi'
    help = '?'
    put  = 'Polož'
    take = 'Vezmi'

class ActionDescription:
    """Stručné popisy akcí pro nápovědu."""
    end  = 'Ukončení hry'
    goto = 'Přesune Karkulku do zadaného sousedního prostoru.'
    help = 'Zobrazí seznam dostupných akcí spolu s jejich stručnými popisy.'
    put  = 'Přesune zadaný předmět z košíku do aktuálního prostoru.'
    take = 'Přesune zadaný předmět z aktuálního prostoru do košíku.'

class ActionMessages:
    """Zprávy vydávané při zpracování příkazů."""
    start_done = ('Vítejte!\n' 
        'Toto je příběh o Červené Karkulce, babičce a vlkovi.\n'
        'Svými příkazy řídíte Karkulku, aby donesla věci babičce.\n'
        'Nebudete-li si vědět rady, zadejte znak ?.')
    start_empty = 'Prázdný příkaz lze použít pouze pro start hry'
    start_wrong = ('Prvním příkazem není startovací příkaz.\n'
        'Hru, která neběží, lze spustit pouze startovacím příkazem.')

    command_wrong = 'Tento příkaz neznám:'

    end_done = 'Ukončili jste hru.\nDěkujeme, že jste si zahráli.'

    enter_cmd = 'Zadejte příkaz:'

    goto_no    = ('Nevím, kam mám jít.\n'
                  'Je třeba zadat název cílového prostoru.')
    goto_wrong = 'Do zadaného prostoru se odsud nedá přejít:'
    goto_done  = 'Karkulka se přesunula do prostoru:'

    help_done = 'Hra umožňuje zadat následující příkazy:'

    put_no    = ('Nevím, co mám položit.\n'
                 'Je třeba zadat název pokládaného předmětu.')
    put_wrong = 'Zadaný předmět v košíku není:'
    put_done  = 'Karkulka vyndala z košíku objekt:'

    take_no    = ('Nevím, co mám zvednout.\n'
                  'Je třeba zadat název zvedaného předmětu.')
    take_wrong = 'Zadaný předmět v prostoru není:'
    take_heavy = 'Zadaný předmět nelze zvednout:'
    take_full  = 'Zadaný předmět se již do košíku nevejde:'
    take_done  = 'Karkulka dala do košíku objekt:'

class GameMessages:
    """Zprávy funkcí modulu game."""
    state_cp = 'Aktuální prostor:'
    state_pn = 'Sousedé prostoru:'
    state_pi = 'Předměty v prostoru:'
    state_bi = 'Předměty v batohu:  '

    enter_cmd = 'Zadejte příkaz:'

    multi_more  = 'Chcete si zahrát ještě jednou (A/N):'
    multi_wrong = ('Odpověď musí začínat některým ze znaků "01ANan"\n'
                   'Zkuste odpovědět znovu.')
    multi_yes   = 'Dobře, zahrajeme si ještě jednou.'
    multi_no    = 'Ještě jednou děkuji za hru.\nNa shledanou.'

    cmd_help = (
        'Aplikace představuje jednoduchou konverzační hru.\n'
        'Při spuštění můžete zadat následující argumenty:\n'
        '-h  Spustí tuto nápovědu\n'
        '-m  Umožní zahrát si hru po skončení znovu\n'
        '-s  Součástí odpovědi hry na zadání příkazu bude informace\n'
        '    o aktuálním stavu světa hry')

class ScenariosMessages:
    """Zprávy při simulacích a testech podle scénářů."""
    test_by = 'Spuštěn test podle scénáře'
    test_exc = 'Při vykonávání příkazu byla vyhozena výjimka:'
    test_exp = 'Očekávaný stav po kroku č.'

    err_answer = 'odpověď hry'
    err_place  = 'aktuální prostor'
    err_neigh  = 'aktuální sousedé'
    err_items  = 'objekty v prostoru'
    err_bag    = 'objekty v batohu'
    err_after  = 'stav hry po testu'
    err_a_msg  = 'Po ukončeném testu má být hra neaktivní'
    err_done   = 'Hra úspěšně otestována podle scénáře'
    err_expected = 'Očekáváno:'
    err_obtained = 'Obdrženo:'
    err_enter    = 'Stisk klávesy Enter aplikaci ukončí'

    mistake_wrong_start_cmd   = 'START'
    mistake_wrong_start_place = 'Prostor'
    mistake_wrong_start_neigh = 'Sousedé'
    mistake_wrong_start_items = 'H-objekty'
    mistake_wrong_start_bag   = 'Batoh'
    mistake_wrong_destination = 'do_háje'

    mistake_wrong_item_take = 'pivo'
    mistake_heavy_item_take = 'stůl'


############################################################################
if DBG>0: print(f'===== Modul {__name__} ===== STOP')
