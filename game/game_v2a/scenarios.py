#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game.game_v2a/scenarios.py
"""
Scénáře, které nám umožní otestovat funkcionalitu hry.
"""
from dbg import DBG
if DBG>0: print(f'===== Modul {__name__} ===== START')
############################################################################

from . import world, actions, game

from .texts import PlaceName         as PN
from .texts import PlaceDescription  as PD
from .texts import ItemName          as IN
from .texts import ActionName        as AN
from .texts import ActionMessages    as AM
from .texts import GameMessages      as GM
from .texts import ScenariosMessages as SM


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
                f'{GM.state_cp} {self.place}\n'
                f'{GM.state_pn} {self.neighbors}\n'
                f'{GM.state_pi} {self.items}\n'
                f'{GM.state_bi} {self.bag}\n'
                f'{_double_line}')


############################################################################
class Scenario(world.ANamed):
    """Instance reprezentují jednotlivé scénáře hry.
    Každý scénář má svůj název, stručný popis toho, co se jím testuje,
    a n-tici kroků, jejichž příkazy se postupně zadávají hře.
    """
    def __init__(self, name: str, description: str, steps: tuple[_Step]):
        super().__init__(name)
        self.description = description
        self.steps = steps

    def __repr__(self):
        return f'{self.name} scenario\n{self.description}\n'

    def simulate_simple(self):
        """Vytiskne jednoduchou simulaci běhu hry podle šťastného scénáře,
        přičemž v každém kroku zobrazí pouze příkaz a odpověď hry.
        """
        for step in self.steps:
            print(f'{step.index}. {step.command}\n{_single_line}\n'
                  f'{step.message}\n{_double_line}')

    def simulate_with_state(self):
        """Vytiskne simulaci běhu hry podle šťastného scénáře,
        přičemž v každém kroku vytiskne za příkazem a odpovědí
        informace o požadovaném stavu hry po provedeném kroku.
        """
        for step in self.steps:
            print(step)
        print("KONEC HRY")

    def test(self):
        """Prověří, zda hra pracuje podle zadaného scénáře;
        Zadané příkazy a odpovědi průběžně tiskne.
        """
        print(f'\n{SM.test_by} {self}\n{_double_line}')
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

        for step in self.steps:
            print(f'{step.index}.\n{_single_line}\n'
                  f'{step.command}\n{_single_line}')
            try:
                answer = game.execute_command(step.command)
                print(f'{answer}\n{_double_line}\n')
            except Exception as Ex:
                print(f'{SM.test_exc}\n', Ex)
                print(f'{SM.test_exp} {step}')
                raise Exception(Ex)

            if step.message != answer[:len(step.message)]:
                _error(step, SM.err_answer, answer)
            if not actions.is_active:
                continue
            current_place = world.current_place
            if  step.place != current_place.name:
                _error(step, SM.err_place, answer)
            if compare_containers(step.neighbors,
                                  current_place.name_2_neighbor.keys()):
                _error(step, SM.err_neigh, answer)
            if compare_containers(step.items, current_place.item_names):
                _error(step, SM.err_items, answer)
            if compare_containers(step.bag, world.BAG.item_names):
                _error(step, SM.err_bag, answer)

        if actions.is_active:
            _error(step, SM.err_after, SM.err_a_msg)
        print(f'{SM.err_done} {self}'
              f'\n{_double_line}\n{_double_line}\n')


############################################################################

def _error(step: _Step, reason: str, answer: str):
    """Ohlásí zprávu o chybě a ukončí aplikaci."""
    msg = f'V {step.index}. kroku neodpovídá: {reason}\n' \
          f'{SM.err_expected} \n{step}\n' \
          f'{SM.err_obtained} \n{answer}\n{_single_line}\n' \
          f'{game.current_state()}'
    print( msg )
    input(SM.err_enter)
    exit(1)


############################################################################

_START_STEP = _Step('', """\
Vítejte!
Toto je příběh o Červené Karkulce, babičce a vlkovi.
Svými příkazy řídíte Karkulku, aby donesla věci babičce.
Nebudete-li si vědět rady, zadejte znak ?.""",
                    PN.house,
                    (PN.wood,),
                    (IN.cake, IN.wine, IN.table, IN.doll,),
                    (),
                    )


_HAPPY = Scenario('HAPPY',
    'Základní úspěšný scénář demonstrující průběh hry, v němž hráč\n'
    'nezadává chybné příkazy a směřuje chytře k zadanému cíli.',
    steps = (
        _START_STEP
        ,
        _Step(f'{AN.take} {IN.wine.lower()}',
              f'{AM.take_done} {IN.wine}',
              PN.house,
              (PN.wood, ),
              (IN.cake, IN.table, IN.doll, ),
              (IN.wine,),
              ),
        _Step(f'{AN.take} {IN.cake.lower()}',
              f'{AM.take_done} {IN.cake}',
              PN.house,
              (PN.wood, ),
              (IN.table, IN.doll, ),
              (IN.cake, IN.wine,),
              ),
        _Step(f'{AN.goto} {PN.wood.upper()}',
              f'{AM.goto_done}\n{PD.wood}',
              PN.wood,
              (PN.house, PN.forest, ),
              (IN.raspberry, IN.strawberry, IN.well, ),
              (IN.cake, IN.wine,),
              ),
        _Step(f'{AN.goto} {PN.forest.lower()}',
              f'{AM.goto_done}\n{PD.forest}',
              PN.forest,
              (PN.wood, PN.cave, PN.cottage, ),
              (IN.wolf,  ),
              (IN.cake, IN.wine,),
              ),
        _Step(f'{AN.goto} {PN.cottage.lower()}',
              f'{AM.goto_done}\n{PD.cottage}',
              PN.cottage,
              (PN.forest, ),
              (IN.bed, IN.table, IN.granny, ),
              (IN.cake, IN.wine,),
              ),
        _Step(f'{AN.put} {IN.cake.lower()}',
              f'{AM.put_done} {IN.cake}',
              PN.cottage,
              (PN.forest, ),
              (IN.bed, IN.table, IN.granny, IN.cake, ),
              (IN.wine,),
              ),
        _Step(f'{AN.put} {IN.wine.upper()}',
              f'{AM.put_done} {IN.wine}',
              PN.cottage,
              (PN.forest, ),
              (IN.bed, IN.table, IN.granny, IN.cake, IN.wine,),
              (),
              ),
        _Step(AN.end,
              AM.end_done,
              PN.cottage,
              (PN.forest, ),
              (IN.bed, IN.table, IN.granny, IN.cake, IN.wine,),
              (),
              ),
    ),
)


_Step.last_index = -1
_MISTAKE = Scenario('MISTAKE',
    'Základní chybový scénář demonstrující průběh hry, v němž hráč\n'
    'nejprve zkusí zadat neprázdný příkaz, pak korektně hru spustí\n,'
    'postupně zadá všechny chybné verze příkazů, požádá o nápovědu\n'
    'a nakonec hru předčasně ukončí.',
    steps = (
        _Step(SM.mistake_wrong_start_cmd,
              AM.start_wrong,
              SM.mistake_wrong_start_place,
              (SM.mistake_wrong_start_neigh,),
              (SM.mistake_wrong_start_items,),
              (SM.mistake_wrong_start_bag,),
              ),
        _START_STEP
        ,
        _Step('',
              AM.start_empty,
              PN.house,
              (PN.wood,),
              (IN.cake, IN.wine, IN.table, IN.doll,),
              (),
              ),
        _Step(AN.take,
              AM.take_no,
              PN.house,
              (PN.wood,),
              (IN.cake, IN.wine, IN.table, IN.doll,),
              (),
              ),
        _Step(f'{AN.take} {SM.mistake_wrong_item_take}',
              f'{AM.take_wrong} {SM.mistake_wrong_item_take}',
              PN.house,
              (PN.wood,),
              (IN.cake, IN.wine, IN.table, IN.doll,),
              (),
              ),
        _Step(f'{AN.take} {IN.table.lower()}',
              f'{AM.take_heavy} {IN.table}',
              PN.house,
              (PN.wood,),
              (IN.cake, IN.wine, IN.table, IN.doll,),
              (),
              ),
        _Step(f'{AN.take} {IN.wine.lower()}',
              f'{AM.take_done} {IN.wine}',
              PN.house,
              (PN.wood, ),
              (IN.cake, IN.table, IN.doll, ),
              (IN.wine,),
              ),
        _Step(f'{AN.take} {IN.cake.lower()}',
              f'{AM.take_done} {IN.cake}',
              PN.house,
              (PN.wood, ),
              (IN.table, IN.doll, ),
              (IN.cake, IN.wine,),
              ),
        _Step(f'{AN.take.lower()} {IN.doll.lower()}',
              f'{AM.take_full} {IN.doll}',
              PN.house,
              (PN.wood, ),
              (IN.table, IN.doll, ),
              (IN.cake, IN.wine,),
              ),
        _Step(AN.put.upper(),
              AM.put_no,
              PN.house,
              (PN.wood, ),
              (IN.table, IN.doll, ),
              (IN.cake, IN.wine,),
              ),
        _Step(f'{AN.put.lower()} {IN.doll.lower()}',
              AM.put_wrong,
              PN.house,
              (PN.wood, ),
              (IN.table, IN.doll, ),
              (IN.cake, IN.wine,),
              ),
        _Step(f'  {AN.goto}  ',
              AM.goto_no,
              PN.house,
              (PN.wood, ),
              (IN.table, IN.doll, ),
              (IN.cake, IN.wine,),
              ),
        _Step(f'  {AN.goto}  {SM.mistake_wrong_destination}',
              AM.goto_wrong,
              PN.house,
              (PN.wood, ),
              (IN.table, IN.doll, ),
              (IN.cake, IN.wine,),
              ),
        _Step(AN.help,
              f'{AM.help_done}\n',
              PN.house,
              (PN.wood, ),
              (IN.table, IN.doll, ),
              (IN.cake, IN.wine,),
              ),
        _Step(AN.end.upper(),
              AM.end_done,
              PN.house,
              (PN.wood, ),
              (IN.table, IN.doll, ),
              (IN.cake, IN.wine,),
              ),
    ))


# Slovník s definovanými scénáři klíčovanými svým názvem
_NAME_2_SCENARIO = {_HAPPY.name: _HAPPY,
                    _MISTAKE.name: _MISTAKE,
                   }


############################################################################

def get() -> tuple[Scenario]:
    """Vrátí kolekci názvů definovaných scénářů"""
    return tuple(_NAME_2_SCENARIO.values())

def show():
    """Vytiskne indexy, názvy a stručné popisy doposud definovaných scénářů.
    """
    ss = get()
    for i in range(len(ss)):
        print(f'{i}. {ss[i]}')

def test_named(*names: tuple[str]):
    """Postupně spustí testy podle scénářů se zadanými názvy."""
    for name in names:
        _NAME_2_SCENARIO[name].test()

def test_indexed(*indexes: tuple[int]):
    """Postupně spustí testy podle scénářů se zadanými indexy."""
    ss = get()
    for index in indexes:
        ss[index].test()


############################################################################
if DBG>0:
    print('\nDefinované scénáře:\n');  show()
    print(f'===== Modul {__name__} ===== STOP')
