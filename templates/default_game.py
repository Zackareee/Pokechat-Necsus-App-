from team.manage import make_a_pokemon_team

game = {
    'user': '',
    'vw_const': 30,
    "player": {
        "pokemon": make_a_pokemon_team(count=3, turn_order=True)
    },
    "opponent": {
        "pokemon": make_a_pokemon_team(count=1, turn_order=True)
    }
}
game['player']['inventory'] = {}
