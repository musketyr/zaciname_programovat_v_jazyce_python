#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v1e/scenarios.py
"""
Scénáře, které nám umožní otestovat funkcionalitu hry.
"""
print(f'===== Modul {__name__} ===== START')
############################################################################

from . import world, game


############################################################################

_single_line = 30*'-'
_double_line = 60*'='


############################################################################
class _Step:
    """Krok scénáře definuje zadávaný příkaz a stav hry po jeho zpracování.
    Pomocí sekvence kroků tvořících scénář lze otestovat funkcionalitu hry.
    """
    # Atribut třídy pamatující si index naposledy vytvářeného kroku
    last_index:int = -1

    def __init__(self,
            command: str,   # Zadaný příkaz
            message: str,   # Zpráva hry vypsaná v reakci na příkaz
            # Stav hry po provedení příkazu
            place:     str,         # Aktuální prostor
            neighbors: tuple[str],  # Sousedé aktuálního prostoru
            items:     tuple[str],  # H-objekty v aktuálním prostoru
            bag:       tuple[str],  # H-objekty v batohu
        ):
        """Vytvoří krok scénáře, přičemž použije index o jedničku větší,
        než byl index předchozího vytvářeného kroku.
        """
        self.command    = command
        self.message    = message
        self.place      = place
        self.neighbors  = neighbors
        self.items      = items
        self.bag        = bag
        _Step.last_index= _Step.last_index + 1
        self.index      = _Step.last_index

    def __str__(self):
        """Vrátí uživatelský podpis instance."""
        return (f'{self.index}.\n'
                f'{self.command}\n{_single_line}\n'
                f'{self.message}\n{_single_line}\n'
                f'Aktuální prostor: {self.place}\n'
                f'Sousedé prostoru: {self.neighbors}\n'
                f'Předměty v prostoru: {self.items}\n'
                f'Předměty v batohu:   {self.bag}\n'
                f'{_double_line}')


############################################################################

def simulate_simple():
    """Vytiskne jednoduchou simulaci běhu hry podle šťastného scénáře,
    přičemž v každém kroku zobrazí pouze příkaz a odpověď hry.
    """
    for step in _HAPPY_SCENARIO:
        print(f'{step.index}. {step.command}\n{_single_line}\n'
              f'{step.message}\n{_double_line}')


def simulate_with_state():
    """Vytiskne simulaci běhu hry podle šťastného scénáře,
    přičemž v každém kroku vytiskne za příkazem a odpovědí
    informace o požadovaném stavu hry po provedeném kroku.
    """
    for step in _HAPPY_SCENARIO:
        print(step)
    print("KONEC HRY")


def test_scenario():
    """Prověří, zda hra pracuje podle zadaného scénáře;
    Zadané příkazy a odpovědi průběžně tiskne.
    """
    print(f'Spuštěna metoda {__package__}.{__name__}.test_scenario')
    from_scenario = None
    from_game     = None

    def compare_containers(cont1, cont2) -> bool:
        """Porovná obsah dvou kontejnerů a jako vedlejší efekt uloží do
        proměnných from_scenario a from_game seznamy s názvy v zadaných
        kontejnerech převedenými na malá písmena a seřazenými dle abecedy.
        """
        nonlocal from_scenario, from_game
        (from_scenario := [item.lower() for item in cont1]).sort()
        (from_game     := [item.lower() for item in cont2]).sort()
        return from_scenario != from_game

    for step in _HAPPY_SCENARIO:
        print(f'{step.index}.\n{_single_line}\n'
              f'{step.command}\n{_single_line}')
        try:
            answer = game.execute_command(step.command)
            print(f'{answer}\n{_double_line}\n')
        except Exception as Ex:
            print('Při vykonávání příkazu byla vyhozena výjimka:\n', Ex)
            print('Očekávaný stav po kroku č.', step)
            raise Exception(Ex)

        if step.message != answer:
            _error(step, step.message, answer, 'odpověď hry')
        current_place = world.current_place
        if  step.place != current_place.name:
            _error(step, step.place, current_place, 'aktuální prostor')
        if compare_containers(step.neighbors,
                              current_place.name_2_neighbor.keys()):
            _error(step, from_scenario, from_game, 'aktuální sousedé')
        if compare_containers(step.items, current_place.item_names):
            _error(step, from_scenario, from_game, 'objekty v prostoru')
        if compare_containers(step.bag, world.BAG.item_names):
            _error(step, from_scenario, from_game, 'objekty v batohu')

    print('Hra úspěšně otestována podle šťastného scénáře')


def _error(step: _Step, scenario: object, game: object, reason: str):
    """Ohlásí zprávu o chybě a ukončí aplikaci."""
    msg = f'V {step.index}. kroku neodpovídá: {reason}\n' \
          f'   Očekáváno: {scenario}\n' \
          f'   Obdrženo:  {game}'
    print( msg )
    input('Stisk klávesy Enter aplikaci ukončí')
    exit(1)


############################################################################

# Základní úspěšný scénář demonstrující průběh hry,
# v něm hráč nezadává žádné chybné příkazy
# a směřuje co nejkratší cestou k zadanému cíli.
_HAPPY_SCENARIO = (
    _Step('',
          'Vítejte!\n'
          'Toto je příběh o Červené Karkulce, babičce a vlkovi.\n'
          'Svými příkazy řídíte Karkulku, aby donesla věci babičce.\n'
          'Nebudete-li si vědět rady, zadejte znak ?.',
          'Domeček',
          ('Les',),
          ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),
          (),
          ),
    _Step('Vezmi víno',
          'Karkulka dala do košíku objekt: Víno',
          'Domeček',
          ('Les', ),
          ('Bábovka', 'Stůl', 'Panenka', ),
          ('Víno', ),
          ),
    _Step('Vezmi bábovka',
          'Karkulka dala do košíku objekt: Bábovka',
          'Domeček',
          ('Les', ),
          ('Stůl', 'Panenka', ),
          ('Bábovka', 'Víno', ),
          ),
    _Step('Jdi LES',
          'Karkulka se přesunula do prostoru:\n'
          'Les s jahodami, malinami a pramenem vody',
          'Les',
          ('Domeček', 'Temný_les', ),
          ('Maliny', 'Jahody', 'Studánka', ),
          ('Bábovka', 'Víno', ),
          ),
    _Step('Jdi temný_les',
          'Karkulka se přesunula do prostoru:\n'
          'Temný_les s jeskyní a číhajícím vlkem',
          'Temný_les',
          ('Les', 'Jeskyně', 'Chaloupka', ),
          ('Vlk',  ),
          ('Bábovka', 'Víno', ),
          ),
    _Step('Jdi chaloupka',
          'Karkulka se přesunula do prostoru:\n'
          'Chaloupka, kde bydlí babička',
          'Chaloupka',
          ('Temný_les',),
          ('Postel', 'Stůl', 'Babička', ),
          ('Bábovka', 'Víno', ),
          ),
    _Step('Polož bábovka',
          'Karkulka vyndala z košíku objekt: Bábovka',
          'Chaloupka',
          ('Temný_les',),
          ('Postel', 'Stůl', 'Babička', 'Bábovka', ),
          ('Víno', ),
          ),
    _Step('Polož VÍNO',
          'Karkulka vyndala z košíku objekt: Víno',
          'Chaloupka',
          ('Temný_les', ),
          ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
          (),
          ),
    _Step('Konec',
          'Ukončili jste hru.\nDěkujeme, že jste si zahráli.',
          'Chaloupka',
          ('Temný_les', ),
          ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno', ),
          (),
          ),
)


############################################################################
print(f'===== Modul {__name__} ===== STOP')
test_scenario()
