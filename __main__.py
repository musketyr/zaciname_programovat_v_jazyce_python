# -*- coding: utf-8 -*-

import sys
sys.argv.append('-d')
print(f'{sys.argv = }')

import game.game_v2b.game as game
game.main()
