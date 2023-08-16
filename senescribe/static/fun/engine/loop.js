/*
    GAME LOOP
 */
import {render} from "./rendering.js"
import {step_physics} from "./physics.js";

let started, interval_id;

export function game_step(){
    step_physics();
    render();
}

export function game_start(){
    // boucle infinie : appelle la fonction game() toutes les 15/1000 de seconde
    let started = true;
    interval_id = setInterval(game_step,1000/15);
}

export function game_stop(display_gameover=true){
    // si la boucle infinie tourne, alors on l'arrete et on affiche l'ecran game over
    started = false;
    if(interval_id !== undefined){
        // on arrete la boucle
        clearInterval(interval_id);
        interval_id = undefined;
    }
}

export function game_pause() {
    stop_game(false);
}

export let game_unpause = game_start();
