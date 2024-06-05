import requests
import json
import random
from pkmn.values import pkmn_move_list, pkmn_pokedex


def make_a_pokemon_team(count=1, turn_order=False):
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
