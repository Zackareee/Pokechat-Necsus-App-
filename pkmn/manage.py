class Stats:

  def __init__(self, attack, defense, hp, special_attack, special_defense,
               speed):
    self.attack = attack
    self.defense = defense
    self.hp = hp
    self.special_attack = special_attack
    self.special_defense = special_defense
    self.speed = speed

  def __str__(self):
    return (f"""
    attack: {self.attack}
    defense:{self.defense}
    hp:{self.hp}
    special_attack:{self.special_attack}
    special_defense:{self.special_defense}
    speed:{self.speed}""")


class Move:

  def __init__(self, name, damage_class, power, pp, type, url):
    self.name = name
    self.damage_class = damage_class
    self.power = power
    self.pp = pp
    self.type = type
    self.url = url

  def __str__(self):
    return (f"{self.name}")


class Pkmn:

  def __init__(self, name, level, sprites, turn_order, types, active_stats,
               max_stats, moves):
    self.name = name
    self.level = level
    self.sprites = sprites
    self.turn_order = turn_order
    self.types = types
    self.active_stats = active_stats
    self.max_stats = max_stats
    self.moves = moves

  def __str__(self):
    return (f"""name: {self.name}
    level:{self.level}
    sprites:{self.sprites}
    turn_order:{self.turn_order}
    types:{self.types}
    active_stats:{self.active_stats}
    max_stats:{self.max_stats}
    moves:{self.moves}""")


#"alakazam": {
#   "abilities": {
#       "inner-focus": "https://pokeapi.co/api/v2/ability/39/",
#       "magic-guard": "https://pokeapi.co/api/v2/ability/98/",
#       "synchronize": "https://pokeapi.co/api/v2/ability/28/"
#   },
#   "active_stats": {
#       "attack": 50,
#       "defense": 45,
#       "hp": 52.58,
#       "special-attack": 135,
#       "special-defense": 95,
#       "speed": 120
#   },
#   "level": 62,
#   "max_stats": {
#       "attack": 50,
#       "defense": 45,
#       "hp": 55,
#       "special-attack": 135,
#       "special-defense": 95,
#       "speed": 120
#   },
#   "moves": {
#       "flash": {
#           "damage_class": "status",
#           "power": None,
#           "pp": 20,
#           "type": "normal",
#           "url": "https://pokeapi.co/api/v2/move/148/"
#       },
#       "take-down": {
#           "damage_class": "physical",
#           "power": 90,
#           "pp": 20,
#           "type": "normal",
#           "url": "https://pokeapi.co/api/v2/move/36/"
#       }
#   },
#   "sprites": {
#       "back_default":
#       "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/65.png",
#       "back_gray":
#       "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/65.png",
#       "back_transparent":
#       "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/back/65.png",
#       "front_default":
#       "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/65.png",
#       "front_gray":
#       "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/gray/65.png",
#       "front_transparent":
#       "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/65.png"
#   },
#   "turn_order": 0,
#   "types": ["psychic"]
# }
