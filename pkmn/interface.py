import requests
import json
import random
from pkmn.values import pkmn_request, pkmn_json, pkmn_move_list, pkmn_abilities_list, pkmn_name_list, pkmn_names_list, pkmn_species_list, pkmn_types_list, pkmn_pokedex, type_map, effective_map, effective_def, health_color




def get_pkmn_images(game):
  filtered_player, filtered_opponent = get_current_pkmn(game)
  player_pic = list(filtered_player)[0][1]['sprites']['back_transparent']
  opponent_pic = list(filtered_opponent)[0][1]['sprites']['front_transparent']
  return [player_pic, opponent_pic]


def get_pkmn_levels(game):
  filtered_player, filtered_opponent = get_current_pkmn(game)
  player_lvl = list(filtered_player)[0][1]['level']
  opponent_lvl = list(filtered_opponent)[0][1]['level']
  return [player_lvl, opponent_lvl]


def get_pkmn_names(game):
  filtered_player = filter(lambda x: x[1]['turn_order'] == 0,
                           game['player']['pokemon'].items())
  filtered_opponent = filter(lambda x: x[1]['turn_order'] == 0,
                             game['opponent']['pokemon'].items())
  return_list = [list(filtered_player)[0][0], list(filtered_opponent)[0][0]]
  return return_list


def get_pkmn_health(game):
  current_pkmn = get_current_pkmn(game)
  player_pkmn_hp = [
      current_pkmn[0][0][1]['active_stats']['hp'],
      current_pkmn[0][0][1]['max_stats']['hp']
  ]
  opponent_pkmn_hp = [
      current_pkmn[1][0][1]['active_stats']['hp'],
      current_pkmn[1][0][1]['max_stats']['hp']
  ]
  return [player_pkmn_hp, opponent_pkmn_hp]


def get_current_pkmn(game):
  filtered_player = filter(lambda x: x[1]['turn_order'] == 0,
                           game['player']['pokemon'].items())
  filtered_opponent = filter(lambda x: x[1]['turn_order'] == 0,
                             game['opponent']['pokemon'].items())
  return [list(filtered_player), list(filtered_opponent)]
