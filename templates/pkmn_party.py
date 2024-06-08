from pkmn.interface import get_pkmn_images, get_pkmn_levels, get_pkmn_names


def render_party(vw_const, game):
  pkmn_images = get_pkmn_images(game)
  pkmn_names = get_pkmn_names(game)
  pkmn_levels = get_pkmn_levels(game)
  print(pkmn_levels)
  print(pkmn_names)
  # pkmn_names = get_pkmn_names()
  pokemon = []
  for i in game['player']['pokemon']:
    pokemon.append([i.name, i.turn_order])

  test_pokemon = []
  for index, i in enumerate(game['player']['pokemon']):
    print(index, i.turn_order)
  html_party = ""
  for i in pokemon:
    html_party += f"""
    <div class="idk_lets_go">
      <button class="pkmn_btn" style="z-index:10; position:relative" value="{i[1]}" name="party_swap">{i[0].upper()}</button>
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
