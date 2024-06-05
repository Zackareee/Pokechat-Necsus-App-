import requests
import json
import random

pkmn_request = requests.get("https://pokeapi.co/api/v2/generation/1/")
pkmn_json = json.loads(pkmn_request.text)
# pkmn_move_list = pkmn_json['moves']
pkmn_move_list = json.load(open('pkmn/static/moves.json'))
pkmn_abilities_list = pkmn_json['abilities']
pkmn_name_list = pkmn_json['name']
pkmn_names_list = pkmn_json['names']
pkmn_species_list = pkmn_json['pokemon_species']
pkmn_types_list = pkmn_json['types']
pkmn_pokedex = json.load(open('pkmn/static/pokedex.json'))

type_map = json.load(open('pkmn/static/types.json'))
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

