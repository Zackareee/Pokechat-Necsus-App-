import random
from pkmn.values import type_map, effective_map, effective_def
from pkmn.interface import get_pkmn_names


def handle_attack(game, move_name, attacking_opponent=True, *args):
  # player_pkmn, opponent_pkmn = get_current_pkmn()
  # player_pkmn_name, opponent_pkmn_name = get_pkmn_names(game)
  # player_pkmn = game['player']['pokemon'][player_pkmn_name]
  # opponent_pkmn = game['opponent']['pokemon'][opponent_pkmn_name]

  # if not attacking_opponent:
  #   player_pkmn_name, opponent_pkmn_name = opponent_pkmn_name, player_pkmn_name
  #   player_pkmn, opponent_pkmn = opponent_pkmn, player_pkmn

  # critical = True
  # move = dict(player_pkmn)['moves'][move_name.lower()]  #['moves'][move_name]

  # stab = 1.5 if move['type'] in player_pkmn['types'] else 1
  # power = move['power'] if move['power'] != None else 1

  # if move['damage_class'] == 'physical':
  #   attack = player_pkmn['active_stats']['attack']
  #   defence = player_pkmn['active_stats']['defense']
  # elif move['damage_class'] == 'special':
  #   attack = player_pkmn['active_stats']['special-attack']
  #   defence = player_pkmn['active_stats']['special-defense']
  # else:
  #   attack = 1
  #   defence = 1

  # print(attack)
  # if attack == 0:
  #   print("shouldnt do damage")

  # if attack > 255 or defence > 255:
  #   attack = attack / 4
  #   defence = defence / 4

  # opponent_types = opponent_pkmn['types']
  # attack_type = type_map[move['type']]

  # effective_bonus_1 = 1
  # effective_bonus_2 = 1

  # effective_bonus_def_1 = "effective"
  # effective_bonus_def_2 = "effective"
  # for index2, j in enumerate(attack_type):
  #   if opponent_types[0] in attack_type[j] and "to" in j:
  #     effective_bonus_1 = effective_map[j]
  #     effective_bonus_def_1 = effective_def[j]

  #   if len(opponent_types
  #          ) > 1 and opponent_types[1] in attack_type[j] and "to" in j:
  #     effective_bonus_2 = effective_map[j]
  #     effective_bonus_def_1 = effective_def[j]

  # print(effective_bonus_1, effective_bonus_2)

  # critical = 1 if critical else 2

  # damage_inner_one = ((2 * int(player_pkmn['level']) * critical) / 5) + 2
  # damage_inner_top = damage_inner_one * power * (attack / defence)
  # damage_inner_two = (damage_inner_top / 50) + 2
  # damage_outer = damage_inner_two * stab * effective_bonus_1 * effective_bonus_2
  # if damage_outer == 1:
  #   randomval = 1
  # else:
  #   randomval = random.randint(217, 255) / 255
  # damage_total = round(damage_outer * randomval, 2)
  # print("damage total", damage_total)
  # print(
  #     f"{player_pkmn_name} used {move_name} on {opponent_pkmn_name}. It was {effective_bonus_def_1}. It dealt {damage_total} damage"
  # )
  # if attacking_opponent:
  #   game['opponent']['pokemon'][opponent_pkmn_name]['active_stats'][
  #       'hp'] -= damage_total
  #   if game['opponent']['pokemon'][opponent_pkmn_name]['active_stats'][
  #       'hp'] < 0:
  #     game['opponent']['pokemon'][opponent_pkmn_name]['active_stats']['hp'] = 0
  # else:
  #   game['player']['pokemon'][opponent_pkmn_name]['active_stats'][
  #       'hp'] -= damage_total
  #   if game['player']['pokemon'][opponent_pkmn_name]['active_stats']['hp'] < 0:
  #     game['player']['pokemon'][opponent_pkmn_name]['active_stats']['hp'] = 0
  # return (damage_total)
  return None
