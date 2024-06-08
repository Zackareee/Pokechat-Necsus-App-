import requests
import json
import random as rand
from pkmn.values import pkmn_move_list, pkmn_pokedex
from pkmn.manage import Stats, Move, Pkmn


def move_from_name(move_name):
    move_details = pkmn_move_list[move_name]
    move = Move(name=move_name,
                damage_class=move_details["damage_class"],
                pp=move_details["pp"],
                power=move_details["power"],
                type=move_details["type"],
                url=move_details["url"])
    return move


def moves_from_json(json_data):
    moves = []
    for i in json_data:
        moves.append(move_from_name(i))
    return moves


def stats_from_json(json_data):
    stats = dict((i['stat']['name'], i['base_stat']) for i in json_data)
    return Stats(attack=stats['attack'],
                 defense=stats['defense'],
                 hp=stats['hp'],
                 special_attack=stats['special-attack'],
                 special_defense=stats['special-defense'],
                 speed=stats['speed'])


def make_a_pokemon(name, index, random=True):
    pkmn_request = json.loads(
        requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").text)
    sprites_request = pkmn_request['sprites']['versions']
    # ['generation-i']['red-blue']
    stats_request = pkmn_request['stats']

    types = [
        i['type']['name'] for i in json.loads(
            requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").text)
        ['types']
    ]
    moves = moves_from_json(
        rand.choices(pkmn_pokedex[name]['moves'], k=rand.randint(1, 4)))
    max_stats = stats_from_json(stats_request)
    active_stats = stats_from_json(stats_request)

    return Pkmn(name=name,
                level=rand.randint(5, 7),
                sprites=sprites_request,
                turn_order=index,
                types=types,
                active_stats=active_stats,
                max_stats=max_stats,
                moves=moves)


def make_a_pokemon_team(count=1, turn_order=False):
    pkmn_team = rand.choices(list(pkmn_pokedex.keys()), k=count)
    # pkmn_team = ["mew"]
    pkmn_team = dict((i, pkmn_pokedex[i]) for i in pkmn_team)
    team = []
    for index, i in enumerate(pkmn_team):
        print(index, i)
        team.append(make_a_pokemon(index=index, name=i))
    return team
