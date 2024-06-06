from flask import Flask, request
import random
from flask_cors import CORS

from team.manage import make_a_pokemon_team

from pkmn.values import health_color
from pkmn.interface import get_pkmn_images, get_pkmn_levels, get_pkmn_names, get_pkmn_health, get_current_pkmn
from pkmn.attack.manage import handle_attack
# from pkmn.attack.tests.abrajynx import game

from templates.setup import setup
from templates.pkmn_party import party
from templates.pkmn_fight import render_fight
# from templates.default_game import game

#   functions
# TODO make critical % chance
# TODO make attack ambigious for whos attacking, figure out attack order on its own
# TODO integrate the storage api so game isnt stored locally - allow for parallel games

# import pkmn.attack.tests.tests

app = Flask(__name__)
CORS(app)
game = {
    'user': '',
    'vw_const': 50,
    "player": {
        "pokemon": make_a_pokemon_team(count=1, turn_order=True)
    },
    "opponent": {
        "pokemon": make_a_pokemon_team(count=1, turn_order=True)
    }
}

vw_const = game['vw_const']

#get and set functions

# game state screens
#todo - make modular, instead of putting html all in one place.


def handle_menu(form_data):
  if "main_menu" in form_data:
    if "fight" in form_data["main_menu"]:
      return render_fight(vw_const, game)
  elif "fight_menu" in form_data:
    handle_attack(game, form_data["fight_menu"])
    return setup(vw_const, game, True)
  # elif "party_swap" in form_data:
  #   pass


#return json of game state for debugging
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
  print(response_json)

  if "form_data" not in response_json:
    return setup(vw_const, game, True)
  else:
    return handle_menu(response_json['form_data'])


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
