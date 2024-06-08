import random
from pkmn.values import type_map, effective_map, effective_def, pkmn_move_list
from pkmn.interface import get_pkmn_names, get_current_pkmn, get_pkmn_health, get_pkmn_images, get_pkmn_levels
from team.manage import move_from_name


def handle_attack(game, move_name, attacking_opponent=True, *args):
  critical_chance = 1

  player_pkmn, opponent_pkmn = get_current_pkmn(game)
  player_pkmn_name, opponent_pkmn_name = get_pkmn_names(game)

  if not attacking_opponent:
    # easiest way to swap direction of attack is simply swap the variables
    player_pkmn_name, opponent_pkmn_name = opponent_pkmn_name, player_pkmn_name
    player_pkmn, opponent_pkmn = opponent_pkmn, player_pkmn

  move = move_from_name(move_name.lower())

  stab = 1.5 if move.type in player_pkmn.types else 1
  current_attack = player_pkmn.active_stats.attack if move.damage_class == "physical" else player_pkmn.active_stats.special_attack if move.damage_class == "special" else 1
  current_defense = player_pkmn.active_stats.defense if move.damage_class == "physical" else player_pkmn.active_stats.special_defense if move.damage_class == "special" else 1
  if current_attack > 255 or current_defense > 255:
    current_attack = current_attack / 4
    current_defense = current_defense / 4

  attack_type = type_map[move.type]

  # Pokemon always have at least one type, possibly two.
  # Check if theyre vulnerable to the move and allocate the damage scale found in effective_map[]
  effective_bonus_1 = 1
  effective_bonus_2 = 1
  effective_bonus_def_1 = "effective"
  effective_bonus_def_2 = "effective"
  for index, j in enumerate(attack_type):
    if opponent_pkmn.types[0] in move.type and "to" in j:
      effective_bonus_1 = effective_map[j]
      effective_bonus_def_1 = effective_def[j]

    if len(opponent_pkmn.types
           ) == 2 and opponent_pkmn.types[1] in move.type and "to" in j:
      effective_bonus_2 = effective_map[j]
      effective_bonus_def_2 = effective_def[j]

  print("1", effective_bonus_def_1, effective_bonus_def_2)
  print("2", effective_bonus_1, effective_bonus_2)
  #TODO make this more readable

  damage_innermost_fraction = (
      (2 * int(player_pkmn.level) * critical_chance) / 5) + 2
  damage_inner_fraction = ((damage_innermost_fraction * move.power *
                            (current_attack / current_defense)) / 50) + 2

  damage = damage_inner_fraction * stab * effective_bonus_1 * effective_bonus_2
  random_value = 1 if damage == 1 else random.randint(217, 255)
  damage = int((damage * random_value) / 255)

  if move.power == 1:
    damage = 0
  print(f"{player_pkmn.name} used move {move.name} did {damage} damage")

  opponent_pkmn.active_stats.hp -= damage
  if opponent_pkmn.active_stats.hp < 0:
    opponent_pkmn.active_stats.hp = 0
  return [
      f"{player_pkmn.name} used move {move.name}",
      f"It was {effective_bonus_def_1}"
  ]
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
