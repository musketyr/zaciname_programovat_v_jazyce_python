#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#Q:/65_PGM/65_PYT/game/game_v1g/scenarios.py
"""
Scénáře, které nám umožní otestovat funkcionalitu hry.
"""
print(f'===== Modul {__name__} ===== START')
############################################################################

from . import world, actions, game


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
        print(f'\nSpuštěn test podle scénáře {self}\n{_double_line}')
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
                print('Při vykonávání příkazu byla vyhozena výjimka:\n', Ex)
                print('Očekávaný stav po kroku č.', step)
                raise Exception(Ex)

            if step.message != answer:
                _error(step, 'odpověď hry', answer)
            if not actions.is_active:
                continue
            current_place = world.current_place
            if  step.place != current_place.name:
                _error(step, 'aktuální prostor', answer)
            if compare_containers(step.neighbors,
                                  current_place.name_2_neighbor.keys()):
                _error(step, 'aktuální sousedé', answer)
            if compare_containers(step.items, current_place.item_names):
                _error(step, 'objekty v prostoru', answer)
            if compare_containers(step.bag, world.BAG.item_names):
                _error(step, 'objekty v batohu', answer)

        if actions.is_active:
            _error(step, 'stav hry po testu',
                   'Po ukončeném testu má být hra neaktivní')
        print(f'Hra úspěšně otestována podle scénáře {self}'
              f'\n{_double_line}\n{_double_line}\n')


############################################################################

def _error(step: _Step, reason: str, answer: str):
    """Ohlásí zprávu o chybě a ukončí aplikaci."""
    msg = f'V {step.index}. kroku neodpovídá: {reason}\n' \
          f'Očekáváno:\n{step}' \
          f'Obdrženo:\n{answer}\n{_single_line}\n' \
          f'{game.current_state()}'
    print( msg )
    input('Stisk klávesy Enter aplikaci ukončí')
    exit(1)


############################################################################

_START_STEP = _Step('', """\
Vítejte!
Toto je příběh o Červené Karkulce, babičce a vlkovi.
Svými příkazy řídíte Karkulku, aby donesla věci babičce.
Nebudete-li si vědět rady, zadejte znak ?.""",
          'Domeček',
          ('Les',),
          ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),
          (),
    )


_HAPPY = Scenario('HAPPY',
    'Základní úspěšný scénář demonstrující průběh hry, v němž hráč\n'
    'nezadává chybné příkazy a směřuje chytře k zadanému cíli.',
    steps = (
        _START_STEP
        ,
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
    ),
)


_Step.last_index = -1
_MISTAKE = Scenario('MISTAKE',
    'Základní chybový scénář demonstrující průběh hry, v němž hráč\n'
    'nejprve zkusí zadat neprázdný příkaz, pak hru korektně spustí,\n'
    'postupně zadá všechny chybné verze příkazů, požádá o nápovědu,\n'
    'a nakonec hru předčasně ukončí.',
    steps = (
        _Step('START',
              'Prvním příkazem není startovací příkaz.\n' +
              'Hru, která neběží, lze spustit pouze startovacím příkazem.',
              'Prostor',
              ('Sousedé', ),
              ('H-objekty', ),
              ('Batoh', ),
              ),
        _START_STEP
        ,
        _Step('',
              'Prázdný příkaz lze použít pouze pro start hry',
              'Domeček',
              ('Les', ),
              ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),
              (),
              ),
        _Step('Vezmi',
              'Nevím, co mám zvednout.\n'
              'Je třeba zadat název zvedaného předmětu.',
              'Domeček',
              ('Les', ),
              ('Bábovka', 'Víno', 'Stůl', 'Panenka', ),
              (),
              ),
        _Step('Vezmi pivo',
              'Zadaný předmět v prostoru není: pivo',
              'Domeček',
              ('Les',),
              ('Bábovka', 'Víno','Stůl', 'Panenka',),
              (),
              ),
        _Step('Vezmi stůl',
              'Zadaný předmět nelze zvednout: Stůl',
              'Domeček',
              ('Les',),
              ('Bábovka', 'Víno', 'Stůl', 'Panenka',),
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
        _Step('vezmi panenka',
              'Zadaný předmět si již do košíku nevejde: Panenka',
              'Domeček',
              ('Les',),
              ('Stůl', 'Panenka',),
              ('Bábovka', 'Víno',),
              ),
        _Step('POLOŽ',
              'Nevím, co mám položit.\n'
              'Je třeba zadat název pokládaného předmětu.',
              'Domeček',
              ('Les',),
              ('Stůl', 'Panenka',),
              ('Bábovka', 'Víno',),
              ),
        _Step('polož panenka',
              'Zadaný předmět v košíku není: panenka',
              'Domeček',
              ('Les',),
              ('Stůl', 'Panenka',),
              ('Bábovka', 'Víno',),
              ),
        _Step('  Jdi  ',
              'Nevím, kam mám jít.\n'
              'Je třeba zadat název cílového prostoru.',
              'Domeček',
              ('Les',),
              ('Stůl', 'Panenka',),
              ('Bábovka', 'Víno',),
              ),
        _Step('  Jdi  do_háje',
              'Do zadaného prostoru se odsud nedá přejít: do_háje',
              'Domeček',
              ('Les',),
              ('Stůl', 'Panenka',),
              ('Bábovka', 'Víno',),
              ),
        _Step('?',
              'Hra umožňuje zadat následující příkazy:\n',
              'Domeček',
              ('Les',),
              ('Stůl', 'Panenka',),
              ('Bábovka', 'Víno',),
              ),
        _Step('KONEC',
              'Ukončili jste hru.\nDěkujeme, že jste si zahráli.',
              'Domeček',
              ('Les',),
              ('Stůl', 'Panenka',),
              ('Bábovka', 'Víno',),
              ),
    ))


# Slovník s definovanými scénáři klíčovanými svým názvem
_NAME_2_SCENARIO = {_HAPPY.name: _HAPPY,
                    _MISTAKE.name: _MISTAKE,
                   }


############################################################################

def get() -> tuple[Scenario]:
    """Vrátí kolekci názvů definovaných scénářů."""
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
print('\nDefinované scénáře:\n');  show()
print(f'===== Modul {__name__} ===== STOP')
