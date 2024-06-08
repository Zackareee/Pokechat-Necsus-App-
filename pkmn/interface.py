from pkmn.manage import Stats, Pkmn, Move


def get_pkmn_images(game, version='generation-i', game_v='red-blue'):
  player_pkmn, opponent_pkmn = get_current_pkmn(game)

  return [
      player_pkmn.sprites[version][game_v]['back_transparent'],
      opponent_pkmn.sprites[version][game_v]['front_transparent']
  ]


def get_pkmn_levels(game):
  player_pkmn, opponent_pkmn = get_current_pkmn(game)
  return [player_pkmn.level, opponent_pkmn.level]


def get_pkmn_names(game):
  player_pkmn, opponent_pkmn = get_current_pkmn(game)
  return [player_pkmn.name, opponent_pkmn.name]


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


def get_pkmn_by_turn_order(game, order, player=True):
  target_pkmn = ""
  if player == True:
    for i in game['player']['pokemon']:
      if i.turn_order == int(order):
        target_pkmn = i
        return target_pkmn
  else:
    for i in game['opponent']['pokemon']:
      if i.name == order:
        target_pkmn = i
        return target_pkmn
  return target_pkmn
