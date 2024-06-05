from pkmn.attack.manage import attack

game = {
    "opponent": {
        "pokemon": {
            "electrode": {
                "abilities": {
                    "aftermath": "https://pokeapi.co/api/v2/ability/106/",
                    "soundproof": "https://pokeapi.co/api/v2/ability/43/",
                    "static": "https://pokeapi.co/api/v2/ability/9/"
                },
                "active_stats": {
                    "attack": 50,
                    "defense": 70,
                    "hp": 60,
                    "special-attack": 80,
                    "special-defense": 80,
                    "speed": 150
                },
                "level": 56,
                "max_stats": {
                    "attack": 50,
                    "defense": 70,
                    "hp": 60,
                    "special-attack": 80,
                    "special-defense": 80,
                    "speed": 150
                },
                "moves": {
                    "agility": {
                        "damage_class": "status",
                        "power": 'null',
                        "pp": 30,
                        "type": "psychic",
                        "url": "https://pokeapi.co/api/v2/move/97/"
                    },
                    "swift": {
                        "damage_class": "special",
                        "power": 60,
                        "pp": 20,
                        "type": "normal",
                        "url": "https://pokeapi.co/api/v2/move/129/"
                    },
                    "thunderbolt": {
                        "damage_class": "special",
                        "power": 90,
                        "pp": 15,
                        "type": "electric",
                        "url": "https://pokeapi.co/api/v2/move/85/"
                    }
                },
                "sprites": {
                    "back_default":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/101.png",
                    "back_gray":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/101.png",
                    "back_transparent":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/back/101.png",
                    "front_default":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/101.png",
                    "front_gray":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/gray/101.png",
                    "front_transparent":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/101.png"
                },
                "turn_order": 0,
                "types": ["electric"],
                "url": "https://pokeapi.co/api/v2/pokemon-species/101/"
            }
        }
    },
    "player": {
        "inventory": {},
        "pokemon": {
            "koffing": {
                "abilities": {
                    "levitate": "https://pokeapi.co/api/v2/ability/26/",
                    "neutralizing-gas":
                    "https://pokeapi.co/api/v2/ability/256/",
                    "stench": "https://pokeapi.co/api/v2/ability/1/"
                },
                "active_stats": {
                    "attack": 65,
                    "defense": 95,
                    "hp": 40,
                    "special-attack": 60,
                    "special-defense": 45,
                    "speed": 35
                },
                "level": 53,
                "max_stats": {
                    "attack": 65,
                    "defense": 95,
                    "hp": 40,
                    "special-attack": 60,
                    "special-defense": 45,
                    "speed": 35
                },
                "moves": {
                    "bide": {
                        "damage_class": "physical",
                        "power": 'null',
                        "pp": 10,
                        "type": "normal",
                        "url": "https://pokeapi.co/api/v2/move/117/"
                    },
                    "mimic": {
                        "damage_class": "status",
                        "power": 'null',
                        "pp": 10,
                        "type": "normal",
                        "url": "https://pokeapi.co/api/v2/move/102/"
                    },
                    "screech": {
                        "damage_class": "status",
                        "power": 'null',
                        "pp": 40,
                        "type": "normal",
                        "url": "https://pokeapi.co/api/v2/move/103/"
                    },
                    "tackle": {
                        "damage_class": "physical",
                        "power": 40,
                        "pp": 35,
                        "type": "normal",
                        "url": "https://pokeapi.co/api/v2/move/33/"
                    }
                },
                "sprites": {
                    "back_default":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/109.png",
                    "back_gray":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/109.png",
                    "back_transparent":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/back/109.png",
                    "front_default":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/109.png",
                    "front_gray":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/gray/109.png",
                    "front_transparent":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/109.png"
                },
                "turn_order": 0,
                "types": ["poison"],
                "url": "https://pokeapi.co/api/v2/pokemon-species/109/"
            },
            "moltres": {
                "abilities": {
                    "flame-body": "https://pokeapi.co/api/v2/ability/49/",
                    "pressure": "https://pokeapi.co/api/v2/ability/46/"
                },
                "active_stats": {
                    "attack": 100,
                    "defense": 90,
                    "hp": 90,
                    "special-attack": 125,
                    "special-defense": 85,
                    "speed": 90
                },
                "level": 65,
                "max_stats": {
                    "attack": 100,
                    "defense": 90,
                    "hp": 90,
                    "special-attack": 125,
                    "special-defense": 85,
                    "speed": 90
                },
                "moves": {
                    "reflect": {
                        "damage_class": "status",
                        "power": 'null',
                        "pp": 20,
                        "type": "psychic",
                        "url": "https://pokeapi.co/api/v2/move/115/"
                    },
                    "solar-beam": {
                        "damage_class": "special",
                        "power": 120,
                        "pp": 10,
                        "type": "grass",
                        "url": "https://pokeapi.co/api/v2/move/76/"
                    },
                    "toxic": {
                        "damage_class": "status",
                        "power": 'null',
                        "pp": 10,
                        "type": "poison",
                        "url": "https://pokeapi.co/api/v2/move/92/"
                    }
                },
                "sprites": {
                    "back_default":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/146.png",
                    "back_gray":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/146.png",
                    "back_transparent":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/back/146.png",
                    "front_default":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/146.png",
                    "front_gray":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/gray/146.png",
                    "front_transparent":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/146.png"
                },
                "turn_order": 2,
                "types": ["fire", "flying"],
                "url": "https://pokeapi.co/api/v2/pokemon-species/146/"
            },
            "rhyhorn": {
                "abilities": {
                    "lightning-rod": "https://pokeapi.co/api/v2/ability/31/",
                    "reckless": "https://pokeapi.co/api/v2/ability/120/",
                    "rock-head": "https://pokeapi.co/api/v2/ability/69/"
                },
                "active_stats": {
                    "attack": 85,
                    "defense": 95,
                    "hp": 80,
                    "special-attack": 30,
                    "special-defense": 30,
                    "speed": 25
                },
                "level": 59,
                "max_stats": {
                    "attack": 85,
                    "defense": 95,
                    "hp": 80,
                    "special-attack": 30,
                    "special-defense": 30,
                    "speed": 25
                },
                "moves": {
                    "mimic": {
                        "damage_class": "status",
                        "power": 'null',
                        "pp": 10,
                        "type": "normal",
                        "url": "https://pokeapi.co/api/v2/move/102/"
                    },
                    "take-down": {
                        "damage_class": "physical",
                        "power": 90,
                        "pp": 20,
                        "type": "normal",
                        "url": "https://pokeapi.co/api/v2/move/36/"
                    }
                },
                "sprites": {
                    "back_default":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/111.png",
                    "back_gray":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/111.png",
                    "back_transparent":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/back/111.png",
                    "front_default":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/111.png",
                    "front_gray":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/gray/111.png",
                    "front_transparent":
                    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/111.png"
                },
                "turn_order": 1,
                "types": ["ground", "rock"],
                "url": "https://pokeapi.co/api/v2/pokemon-species/111/"
            }
        }
    },
    "user": "",
    "vw_const": 30
}

attack(True, game, "body-slam")
