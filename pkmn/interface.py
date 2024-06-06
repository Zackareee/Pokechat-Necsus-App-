from pkmn.manage import Stats, Pkmn, Move


def get_pkmn_images(game):
  player_pkmn, opponent_pkmn = get_current_pkmn(game)
  return [
      player_pkmn.sprites['back_transparent'],
      opponent_pkmn.sprites['front_transparent']
  ]


def get_pkmn_levels(game):
  player_pkmn, opponent_pkmn = get_current_pkmn(game)
  return [player_pkmn.level, opponent_pkmn.level]


def get_pkmn_names(game):
  player = ""
  for i in game['player']['pokemon']:
    player = i.name

  opponent = ""
  for i in game['opponent']['pokemon']:
    opponent = i.name

  return [player, opponent]


def get_pkmn_health(game):
  player_pkmn, opponent_pkmn = get_current_pkmn(game)

  player_pkmn_hp = [player_pkmn.active_stats.hp, player_pkmn.max_stats.hp]
  opponent_pkmn_hp = [
      opponent_pkmn.active_stats.hp, opponent_pkmn.max_stats.hp
  ]
  return [player_pkmn_hp, opponent_pkmn_hp]


def get_current_pkmn(game):
  player_pokemon = ""
  opponent_pokemon = ""
  for i in game['player']['pokemon']:
    if i.turn_order == 0:
      player_pokemon = i
  for i in game['opponent']['pokemon']:
    if i.turn_order == 0:
      opponent_pokemon = i

  return [player_pokemon, opponent_pokemon]
