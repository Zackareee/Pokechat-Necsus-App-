from pkmn.interface import get_pkmn_images, get_pkmn_levels, get_pkmn_names, get_pkmn_health


def setup(vw_const, game, bool=False):
   pkmn_images = get_pkmn_images(game)
   pkmn_names = get_pkmn_names(game)
   pkmn_levels = get_pkmn_levels(game)
   pkmn_health = get_pkmn_health(game)

   return {
       "author": "PokemoN CoolS System",
       "text": f'''
        <div style="position:relative; display:inline-block;">
        {'<div id="targetElement" onload="(reloadJs || console.log)()">' if bool else ""}
           <img {'onload="(reloadJs || console.log)()"' if bool else ""} class="pkmn_back" src="/static/images/pkmn_back.png"></img>
           <img class="pkmn_user" src="{pkmn_images[0]}"></img>
           <img class="pkmn_enemy" src="{pkmn_images[1]}"></img>
           <p class="opponent_pkmn_name" style="">{pkmn_names[1].upper()}</p>
           <p class="player_pkmn_name" style="">{pkmn_names[0].upper()}</p>
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
