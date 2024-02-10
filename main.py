from flask import Flask, request, Response
import requests
import json
import random
from flask_cors import CORS

#   variable setup - import refactored json and request from the api
#

pkmn_request = requests.get("https://pokeapi.co/api/v2/generation/1/")
pkmn_json = json.loads(pkmn_request.text)
# pkmn_move_list = pkmn_json['moves']
pkmn_move_list = json.load(open('moves.json'))
pkmn_abilities_list = pkmn_json['abilities']
pkmn_name_list = pkmn_json['name']
pkmn_names_list = pkmn_json['names']
pkmn_species_list = pkmn_json['pokemon_species']
pkmn_types_list = pkmn_json['types']
pkmn_pokedex = json.load(open('pokedex.json'))

type_map = json.load(open('types.json'))
effective_map = {
    "double_damage_from": 2,
    "double_damage_to": 2,
    "half_damage_from": 0.5,
    "half_damage_to": 0.5,
    "no_damage_from": 0,
    "no_damage_to": 0
}
effective_def = {
    "double_damage_from": "super effective",
    "double_damage_to": "super effective",
    "half_damage_from": "not very effective",
    "half_damage_to": "not very effective",
    "no_damage_from": "inaffective",
    "no_damage_to": "inaffective"
}

#TODO make health_color change color of health bar
health_color = {
    "green": 0.5625,
    "yellow": 0.207,
    "red": 0,
}

#
#   functions
#


def make_a_pokemon_team(count=1, turn_order=False):
  pkmn_pokedex = json.load(open('pokedex.json'))
  pkmn_team = random.choices(list(pkmn_pokedex.keys()), k=count)
  pkmn_team = dict((i, pkmn_pokedex[i]) for i in pkmn_team)
  for index, i in enumerate(pkmn_team):
    pkmn_team[i]['moves'] = random.choices(pkmn_team[i]['moves'],
                                           k=random.randint(1, 4))
    # pkmn_team[i]['moves'] = dict((random.choices(pkmn_team[i]['moves'],k=4),))
    pkmn_team[i]['moves'] = dict(
        (j, pkmn_move_list[j]) for j in pkmn_team[i]['moves'])
    pkmn_request = json.loads(
        requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}").text)
    sprites_request = pkmn_request['sprites']['versions']['generation-i'][
        'red-blue']
    abilities_request = pkmn_request['abilities']
    stats_request = pkmn_request['stats']
    # set-up maximum stats of pokemon
    pkmn_team[i]['max_stats'] = dict(
        (i['stat']['name'], i['base_stat']) for i in stats_request)
    pkmn_team[i]['active_stats'] = dict(
        # set-up current stats of pokemon
        (i['stat']['name'], i['base_stat']) for i in stats_request)
    pkmn_team[i]['abilities'] = dict(
        (i['ability']['name'], i['ability']['url'])
        # set-up pokemon abilities
        for i in abilities_request)
    pkmn_team[i]['level'] = random.randint(50, 70)
    pkmn_team[i]['types'] = [
        i['type']['name'] for i in json.loads(
            requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}").text)
        ['types']
    ]
    pkmn_team[i]['sprites'] = sprites_request

    if turn_order == True:
      pkmn_team[i]['turn_order'] = index
  return pkmn_team


# TODO make critical % chance
# TODO make attack ambigious for whos attacking, figure out attack order on its own


def attack(attacking_opponent, game, move_name, *args):
  # player_pkmn, opponent_pkmn = get_current_pkmn()
  player_pkmn_name, opponent_pkmn_name = get_pkmn_names()
  player_pkmn = game['player']['pokemon'][player_pkmn_name]
  opponent_pkmn = game['opponent']['pokemon'][opponent_pkmn_name]

  if not attacking_opponent:
    player_pkmn_name, opponent_pkmn_name = opponent_pkmn_name, player_pkmn_name
    player_pkmn, opponent_pkmn = opponent_pkmn, player_pkmn

  critical = True
  move = dict(player_pkmn)['moves'][move_name.lower()]  #['moves'][move_name]

  stab = 1.5 if move['type'] in player_pkmn['types'] else 1
  power = move['power'] if move['power'] != None else 1

  if move['damage_class'] == 'physical':
    attack = player_pkmn['active_stats']['attack']
    defence = player_pkmn['active_stats']['defense']
  elif move['damage_class'] == 'special':
    attack = player_pkmn['active_stats']['special-attack']
    defence = player_pkmn['active_stats']['special-defense']
  else:
    attack = 1
    defence = 1

  if attack > 255 or defence > 255:
    attack = attack / 4
    defence = defence / 4

  opponent_types = opponent_pkmn['types']
  attack_type = type_map[move['type']]

  effective_bonus_1 = 1
  effective_bonus_2 = 1

  effective_bonus_def_1 = "effective"
  effective_bonus_def_2 = "effective"
  for index2, j in enumerate(attack_type):
    if opponent_types[0] in attack_type[j] and "to" in j:
      effective_bonus_1 = effective_map[j]
      effective_bonus_def_1 = effective_def[j]

    if len(opponent_types
           ) > 1 and opponent_types[1] in attack_type[j] and "to" in j:
      effective_bonus_2 = effective_map[j]
      effective_bonus_def_1 = effective_def[j]

  print(effective_bonus_1, effective_bonus_2)

  critical = 1 if critical else 2

  damage_inner_one = ((2 * int(player_pkmn['level']) * critical) / 5) + 2
  damage_inner_top = damage_inner_one * power * (attack / defence)
  damage_inner_two = (damage_inner_top / 50) + 2
  damage_outer = damage_inner_two * stab * effective_bonus_1 * effective_bonus_2
  if damage_outer == 1:
    randomval = 1
  else:
    randomval = random.randint(217, 255) / 255
  damage_total = round(damage_outer * randomval, 2)
  print("damage total", damage_total)
  print(
      f"{player_pkmn_name} used {move_name} on {opponent_pkmn_name}. It was {effective_bonus_def_1}. It dealt {damage_total} damage"
  )
  if attacking_opponent:
    game['opponent']['pokemon'][opponent_pkmn_name]['active_stats'][
        'hp'] -= damage_total
    if game['opponent']['pokemon'][opponent_pkmn_name]['active_stats'][
        'hp'] < 0:
      game['opponent']['pokemon'][opponent_pkmn_name]['active_stats']['hp'] = 0
  else:
    game['player']['pokemon'][opponent_pkmn_name]['active_stats'][
        'hp'] -= damage_total
    if game['player']['pokemon'][opponent_pkmn_name]['active_stats']['hp'] < 0:
      game['player']['pokemon'][opponent_pkmn_name]['active_stats']['hp'] = 0
  return (damage_total)


#define the game
#todo integrate the storage api so game isnt stored locally - allow for parallel games
game = {
    'user': '',
    'vw_const': 50,
    "player": {
        "pokemon": make_a_pokemon_team(count=3, turn_order=True)
    },
    "opponent": {
        "pokemon": make_a_pokemon_team(count=1, turn_order=True)
    }
}
game['player']['inventory'] = {}

app = Flask(__name__)
CORS(app)

vw_const = 30

#get and set functions


def get_pkmn_images():
  filtered_player, filtered_opponent = get_current_pkmn()
  player_pic = list(filtered_player)[0][1]['sprites']['back_transparent']
  opponent_pic = list(filtered_opponent)[0][1]['sprites']['front_transparent']
  return [player_pic, opponent_pic]


def get_pkmn_levels():
  filtered_player, filtered_opponent = get_current_pkmn()
  player_lvl = list(filtered_player)[0][1]['level']
  opponent_lvl = list(filtered_opponent)[0][1]['level']
  return [player_lvl, opponent_lvl]


def get_pkmn_names():
  filtered_player = filter(lambda x: x[1]['turn_order'] == 0,
                           game['player']['pokemon'].items())
  filtered_opponent = filter(lambda x: x[1]['turn_order'] == 0,
                             game['opponent']['pokemon'].items())
  return_list = [list(filtered_player)[0][0], list(filtered_opponent)[0][0]]
  return return_list


def get_pkmn_health():
  current_pkmn = get_current_pkmn()
  player_pkmn_hp = [
      current_pkmn[0][0][1]['active_stats']['hp'],
      current_pkmn[0][0][1]['max_stats']['hp']
  ]
  opponent_pkmn_hp = [
      current_pkmn[1][0][1]['active_stats']['hp'],
      current_pkmn[1][0][1]['max_stats']['hp']
  ]
  return [player_pkmn_hp, opponent_pkmn_hp]


def get_current_pkmn():
  filtered_player = filter(lambda x: x[1]['turn_order'] == 0,
                           game['player']['pokemon'].items())
  filtered_opponent = filter(lambda x: x[1]['turn_order'] == 0,
                             game['opponent']['pokemon'].items())
  return [list(filtered_player), list(filtered_opponent)]


# game state screens
#todo - make modular, instead of putting html all in one place.
def setup(bool=False):
  global vw_const
  pkmn_images = get_pkmn_images()
  pkmn_names = get_pkmn_names()
  pkmn_levels = get_pkmn_levels()
  pkmn_health = get_pkmn_health()

  return {
      "author": "PokemoN CoolS System",
      "text": f'''
        <div style="position:relative; display:inline-block;">
        {'<div id="targetElement" onload="(reloadJs || console.log)()">' if bool else ""}
           <img {'onload="(reloadJs || console.log)()"' if bool else ""} class="pkmn_back" src="/static/images/pkmn_back.png"></img>
           <img class="pkmn_user" src="{pkmn_images[0]}"></img>
           <img class="pkmn_enemy" src="{pkmn_images[1]}"></img>
           <p class="opponent_pkmn_name" style="">{pkmn_names[1]}</p>
           <p class="player_pkmn_name" style="">{pkmn_names[0]}</p>
           <p class="opponent_pkmn_level" style="">{pkmn_levels[1]}</p>
           <p class="player_pkmn_level" style="">{pkmn_levels[0]}</p>
           <p class="player_pkmn_health" >{pkmn_health[0][0]}/{pkmn_health[0][1]}</p>
           <div class="pkmn_player_health_bar ">
             <svg class="pkmn_health_bar" viewBox="0 0 50 4" width="100%" height="100%">
                 <polygon points="1,0 49,0 49,1 50,1 50,3 49,3 49,4 1,4 1,3 0,3 0,1 1,1 " style="fill:black;" shape-rendering="crispEdges" />
                 <polygon points="1,1 49,1 49,3 1,3 " style="fill:white;" shape-rendering="crispEdges" />
                 <polygon points="1,1 {str(1+(48*int(pkmn_health[0][0])/int(pkmn_health[0][1])))},1 {str(1+(48*int(pkmn_health[0][0])/int(pkmn_health[0][1])))},3 1,3 " style="fill:limegreen;" shape-rendering="crispEdges" />
             </svg>
           </div>
           <div class="pkmn_opponent_health_bar ">
             <svg class="pkmn_health_bar" viewBox="0 0 50 4" width="100%" height="100%">
                 <polygon points="1,0 49,0 49,1 50,1 50,3 49,3 49,4 1,4 1,3 0,3 0,1 1,1 " style="fill:black;" shape-rendering="crispEdges" />
                 <polygon points="1,1 49,1 49,3 1,3 " style="fill:white;" shape-rendering="crispEdges" />
                 <polygon points="1,1 {str(1+(48*int(pkmn_health[1][0])/int(pkmn_health[1][1])))},1 {str(1+(48*int(pkmn_health[1][0])/int(pkmn_health[1][1])))},3 1,3 " style="fill:limegreen;" shape-rendering="crispEdges" />
             </svg>
           </div>

           
           <table style="position: absolute; z-index: 999; top: 0%;">
              <tbody style="display:block; overflow-y:visible; height:{vw_const*0.9}vw">
                 <tr>
                    <td style="width:{0.4*vw_const}vw"></td>
                    <td style="width:{0.6*vw_const}vw"></td>
                 </tr>
                 <tr>
                    <td style="width:{0.4*vw_const}vw"></td>
                    <td style="width:{0.6*vw_const}vw"></td>
                    </td>
                 </tr>
                 <tr>
                    <td style="width:calc(var(--vw-const)/2.3)"></td>
                    <td style="width:calc(var(--vw-const)/1.6);">
                       <form style="padding-top: calc(var(--vw-const)/40);">
                          <div class = "grid-container">
                             <div class="main-menu-grid-item" style="">
                                <button value="fight" name="main_menu" class = "pkmn_btn small_btn">FIGHT</button>
                             </div>
                             <div class="main-menu-grid-item">
                                <button value="pkmn" name="main_menu" class = "pkmn_btn small_btn">$%</button>
                             </div>
                             <div class="main-menu-grid-item">
                                <button value="item" name="main_menu" class = "pkmn_btn small_btn">ITEM</button>
                             </div>
                             <div class="main-menu-grid-item">
                                <button value="run" name="main_menu" class = "pkmn_btn small_btn">RUN</button>
                             </div>
                          </div>
                       </form>
                    </td>
                 </tr>
              </tbody>
           </table>
        </div>
                                ''',
      "css": "static/style/style.css",
      'js': "static/javascript/tooltip.js"
  }


def fights():
  pkmn_names = get_pkmn_names()
  print(pkmn_names)
  print(list(game['player']['pokemon'][pkmn_names[0]]['moves'].keys()))
  moves_list = list(game['player']['pokemon'][pkmn_names[0]]['moves'].keys())
  html_moves = ""
  pkmn_health = get_pkmn_health()
  pkmn_images = get_pkmn_images()
  pkmn_levels = get_pkmn_levels()
  print(pkmn_levels)
  # print(pkmn_names)
  # pkmn_names = get_pkmn_names()
  for i in moves_list:
    html_moves += f"""<div class="tooltip">
      <span class="tooltiptext"><img class="tooltip_img" src="/static/images/tooltip.png"></img></span>
      <button value="{i.capitalize()}" name="fight_menu" class = "tooltip pkmn_fight_btn small_btn"> {i.capitalize() }</button>
    </div>"""
  return {
      "author": "PokemoN CoolS System",
      "text": f'''
      <div style="position:relative; display:inline-block;">
       <img onload="(reloadJs || console.log)()" class="pkmn_back" src="../static/images/pkmn_back.png"></img>
       <img class="pkmn_user" src="{pkmn_images[0]}"></img>
       <img class="pkmn_enemy" src="{pkmn_images[1]}"></img>
       <p class="opponent_pkmn_name" style="">{pkmn_names[1]}</p>
       <p class="player_pkmn_name" style="">{pkmn_names[0]}</p>
       <p class="opponent_pkmn_level" style="">{pkmn_levels[1]}</p>
       <p class="player_pkmn_level" style="">{pkmn_levels[0]}</p>
       <p class="player_pkmn_health" style="">{pkmn_health[0][0]}/{pkmn_health[0][1]}</p>
        <div class="pkmn_player_health_bar ">
          <svg class="pkmn_health_bar" viewBox="0 0 50 4" width="100%" height="100%">
              <polygon points="1,0 49,0 49,1 50,1 50,3 49,3 49,4 1,4 1,3 0,3 0,1 1,1 " style="fill:black;" shape-rendering="crispEdges" />
              <polygon points="1,1 49,1 49,3 1,3 " style="fill:white;" shape-rendering="crispEdges" />
              <polygon points="1,1 {str(1+(48*int(pkmn_health[0][0])/int(pkmn_health[0][1])))},1 {str(1+(48*int(pkmn_health[0][0])/int(pkmn_health[0][1])))},3 1,3 " style="fill:limegreen;" shape-rendering="crispEdges" />
          </svg>
        </div>
        <div class="pkmn_opponent_health_bar ">
          <svg class="pkmn_health_bar" viewBox="0 0 50 4" width="100%" height="100%">
              <polygon points="1,0 49,0 49,1 50,1 50,3 49,3 49,4 1,4 1,3 0,3 0,1 1,1 " style="fill:black;" shape-rendering="crispEdges" />
              <polygon points="1,1 49,1 49,3 1,3 " style="fill:white;" shape-rendering="crispEdges" />
              <polygon points="1,1 {str(1+(48*int(pkmn_health[1][0])/int(pkmn_health[1][1])))},1 {str(1+(48*int(pkmn_health[1][0])/int(pkmn_health[1][1])))},3 1,3 " style="fill:limegreen;" shape-rendering="crispEdges" />
          </svg>
        </div>

       
       <table style="position: absolute; z-index: 999; top: 0%;">
          <tbody style="display:block; overflow-y:visible; height:{0.9*vw_const}vw">
             <tr>
             </tr>
             <tr>
             </tr>
             <tr>
                <td style="width:calc(var(--vw-const)/2.3)"></td>
                <td style="max-width:calc(var(--vw-const)/1.6); width:{0.6*vw_const}vw;">
                   <form style="padding:calc(var(--vw-const)/25); width:calc((var(--vw-const)/1.6) - 0.75em); >
                      <div class="fight-grid-container">
                         {html_moves}
                      </div>
                   </form>
                </td>
             </tr>
          </tbody>
       </table>
    </div>
    ''',
      "css": "static/style/style.css"
  }


def party():
  pkmn_images = get_pkmn_images()
  pkmn_names = get_pkmn_names()
  pkmn_levels = get_pkmn_levels()
  print(pkmn_levels)
  print(pkmn_names)
  # pkmn_names = get_pkmn_names()
  html_party = ""
  for i in list(game['player']['pokemon'].keys()):
    html_party += f"""
    <div class="idk_lets_go">
      <button class="pkmn_btn" style="z-index:10; position:relative" value="{i}" name="party_swap">{i.upper()}</button>
    </div>
    """
  return {
      "author": "PokemoN CoolS System",
      "text": f'''
       <div style="position:relative; display:inline-block;">
         <img onload="(reloadJs || console.log)()" class="pkmn_back" src="../static/images/pkmn_empty.png"></img>
         <div style="position:absolute; top:0px;">
            <form style="padding:{0.06*vw_const}vw; padding-top:0px;">
               {html_party}
            </form>
         </div>
      </div>
      ''',
      "css": "static/style/style.css"
  }


#return json of game state for debugging
@app.route('/game', methods=["GET", "POST"])
def pla():
  global game
  return game


@app.route('/', methods=["GET", "POST"])
def index():
  global game
  global vw_const
  pkmn_names = get_pkmn_names()
  response_json = request.json
  print(response_json)
  if 'form_data' in response_json:
    if 'main_menu' in response_json['form_data']:
      if response_json['form_data']['main_menu'] == 'fight':
        return fights()
      elif response_json['form_data']['main_menu'] == 'pkmn':
        return party()
    elif 'party_swap' in response_json['form_data']:
      game['player']['pokemon'][
          pkmn_names[0].lower()]['turn_order'], game['player']['pokemon'][
              response_json['form_data']
              ['party_swap']]['turn_order'] = game['player']['pokemon'][
                  response_json['form_data']
                  ['party_swap']]['turn_order'], game['player']['pokemon'][
                      pkmn_names[0].lower()]['turn_order']
    elif 'fight_menu' in response_json['form_data']:
      attack(True, game, response_json['form_data']['fight_menu'])
      player_pkmn, opponent_pkmn = get_current_pkmn()
      player_pkmn_name, opponent_pkmn_name = get_pkmn_names()
      opponent_move = random.choice(
          list(dict(opponent_pkmn)[opponent_pkmn_name]['moves'].keys()))
      print(str(opponent_move) + "this move")
      attack(False, game, opponent_move)

    # player_pkmn_team[response_json['form_data']['party_swap']]['turn_order'] = 0
    return setup(True)
  else:

    if response_json['text'].startswith("size"):
      print(int(response_json['text'].split()[1]))
      vw_const = int(response_json['text'].split()[1])

    #
    # debugging for rewriting css
    #
    # with open("./static/style/style.css") as f:
    #   lines = f.readlines()
    # print(vw_const)
    # lines[
    #     0] = f":root {{--vw-const: {vw_const}vw; --px-const: {vw_const}px;}}\n"
    # with open("./static/style/style.css", "w") as f:
    #   f.writelines(lines)

    # game['opponent'] = {
    #     "pokemon": make_a_pokemon_team(count=1, turn_order=True)
    # }
    # game['player'] = {"pokemon": make_a_pokemon_team(count=3, turn_order=True)}

    game = {
        'user': '',
        'vw_const': 50,
        "player": {
            "pokemon": make_a_pokemon_team(count=3, turn_order=True)
        },
        "opponent": {
            "pokemon": make_a_pokemon_team(count=1, turn_order=True)
        }
    }
    #True
    return setup(True)


app.run(host='0.0.0.0', port=5000, debug=True)
