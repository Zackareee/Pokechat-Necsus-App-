from types import MethodType
from flask import Flask, request
import random
from flask_cors import CORS

from team.manage import make_a_pokemon_team

from pkmn.values import health_color
from pkmn.interface import get_pkmn_images, get_pkmn_levels, get_pkmn_names, get_pkmn_health, get_current_pkmn, get_pkmn_by_turn_order
from pkmn.attack.manage import handle_attack
# from pkmn.attack.tests.abrajynx import game

from templates.setup import setup
from templates.pkmn_fight import render_fight
from templates.pkmn_party import render_party
from templates.text.pkmn_fight_text import render_fight_text
# from templates.default_game import game

#   functions
# TODO make critical % chance
# TODO make attack ambigious for whos attacking, figure out attack order on its own
# TODO integrate the storage api so game isnt stored locally - allow for parallel games

# import pkmn.attack.tests.tests

app = Flask(__name__)
CORS(app)
game = {
    'game_text': [],
    'user': '',
    'vw_const': 50,
    "player": {
        "pokemon": make_a_pokemon_team(count=2, turn_order=True)
    },
    "opponent": {
        "pokemon": make_a_pokemon_team(count=1, turn_order=True)
    }
}

vw_const = game['vw_const']

#get and set functions

# game state screens
#todo - make modular, instead of putting html all in one place.


def handle_menu(form_data, method_type):
  print(form_data)
  player_pkmn, opponent_pkmn = get_current_pkmn(game)
  if "main_menu" in form_data:

    if "fight" in form_data["main_menu"]:
      return render_fight(vw_const, game)

    elif "pkmn" in form_data["main_menu"]:
      return render_party(vw_const, game)

  elif "fight_menu" in form_data:
    if form_data["fight_menu"].isnumeric():
      current_state = int(form_data["fight_menu"])
      print(current_state)
      if len(game['game_text']) > current_state + 1:
        return render_fight_text(vw_const, game,
                                 game['game_text'][current_state + 1],
                                 current_state + 1)
      else:
        return setup(vw_const, game, True)
    else:
      game['game_text'] = []
      game['game_text'] += handle_attack(game, form_data["fight_menu"])
      game['game_text'] += handle_attack(game,
                                         random.choice(
                                             opponent_pkmn.moves).name,
                                         attacking_opponent=False)
      print(game['game_text'])
      return render_fight_text(vw_const, game, game['game_text'][0], 0)

  elif "party_swap" in form_data:
    turn_order = form_data["party_swap"]
    player_pkmn, opponent_pkmn = get_current_pkmn(game)
    target_pkmn = get_pkmn_by_turn_order(game, turn_order)
    player_pkmn.turn_order, target_pkmn.turn_order = target_pkmn.turn_order, player_pkmn.turn_order
    return setup(vw_const, game, True)


@app.route('/game', methods=["GET", "POST"])
def play():
  global game
  return game


@app.route('/', methods=["GET", "POST"])
def index():
  global game
  global vw_const
  pkmn_names = get_pkmn_names(game)
  response_json = request.json

  if "form_data" not in response_json:
    return setup(vw_const, game, True)
  else:
    return handle_menu(response_json['form_data'], request.method)


# if 'form_data' in response_json:
#   if 'main_menu' in response_json['form_data']:
#     if response_json['form_data']['main_menu'] == 'fight':
#       return fight(vw_const, game)
#     elif response_json['form_data']['main_menu'] == 'pkmn':
#       return party(vw_const, game)
#   elif 'party_swap' in response_json['form_data']:
#     game['player']['pokemon'][
#         pkmn_names[0].lower()]['turn_order'], game['player']['pokemon'][
#             response_json['form_data']
#             ['party_swap']]['turn_order'] = game['player']['pokemon'][
#                 response_json['form_data']
#                 ['party_swap']]['turn_order'], game['player']['pokemon'][
#                     pkmn_names[0].lower()]['turn_order']
#   elif 'fight_menu' in response_json['form_data']:
#     attack(True, game, response_json['form_data']['fight_menu'])
#     player_pkmn, opponent_pkmn = get_current_pkmn(game)
#     player_pkmn_name, opponent_pkmn_name = get_pkmn_names(game)
#     opponent_move = random.choice(
#         list(dict(opponent_pkmn)[opponent_pkmn_name]['moves'].keys()))
#     print(str(opponent_move) + "this move")
#     attack(False, game, opponent_move)

#   # player_pkmn_team[response_json['form_data']['party_swap']]['turn_order'] = 0
#   return setup(vw_const, game, True)
# else:

#   if response_json['text'].startswith("size"):
#     print(int(response_json['text'].split()[1]))
#     vw_const = int(response_json['text'].split()[1])

#   game = {
#       'user': '',
#       'vw_const': 50,
#       "player": {
#           "pokemon": make_a_pokemon_team(count=1, turn_order=True)
#       },
#       "opponent": {
#           "pokemon": make_a_pokemon_team(count=1, turn_order=True)
#       }
#   }
#   #True
# return setup(vw_const, game, True)

app.run(host='0.0.0.0', port=5000, debug=True)
