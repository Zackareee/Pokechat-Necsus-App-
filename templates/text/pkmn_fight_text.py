from pkmn.interface import get_pkmn_images, get_pkmn_levels, get_pkmn_names, get_pkmn_health, get_current_pkmn


def render_fight_text(vw_const, game, text, index):
   pkmn_names = get_pkmn_names(game)
   player_pkmn, opponent_pkmn = get_current_pkmn(game)
   player_moves = []
   for i in player_pkmn.moves:
      player_moves.append(i)
   pkmn_health = get_pkmn_health(game)
   pkmn_images = get_pkmn_images(game)
   pkmn_levels = get_pkmn_levels(game)
   print(pkmn_levels)
   # print(pkmn_names)
   # pkmn_names = get_pkmn_names()
   return {
       "author": "PokemoN CoolS System",
       "text": f'''
      <div style="position:relative; display:inline-block;">
       <img onload="(reloadJs || console.log)()" class="pkmn_back" src="../static/images/pkmn_tooltip_back.png"></img>
       <img class="pkmn_user" src="{pkmn_images[0]}"></img>
       <img class="pkmn_enemy" src="{pkmn_images[1]}"></img>
       <p class="opponent_pkmn_name" style="">{pkmn_names[1].upper()}</p>
       <p class="player_pkmn_name" style="">{pkmn_names[0].upper()}</p>
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
             <tr></tr>
             <tr></tr>
             <tr>
             <td>
                <form>
                   <div style="padding:calc(var(--vw-const)/25);" class="fight-grid-container">
                      <button value="{index}" style="line-break:anywhere" name="fight_menu" class = "pkmn_fight_btn small_btn">{text}</button>
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