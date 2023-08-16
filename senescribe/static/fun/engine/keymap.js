import {countElem, keyElem} from "./init.js";
import {world, Vertex} from "./physics.js";

let debug = true;
let key = null;
let count = 0;

/*
    KEY BINDINGS
 */
export function keyPush(evt) {
    /*
        Here we map what to do on a key press.
        It is possible to play with the arrow keys or with ZQSD.
    */
    let move = new Vertex(0, 0);
    switch (evt.keyCode) {
        case 37: // left arrow
        case 81: // Q
        case 65: // A
            move = move.plus(new Vertex(-1, 0));
            break;
        case 38: // up arrow
        case 90: // Z
        case 87: // W
            move = move.plus(new Vertex(0, -1));
            break;
        case 39: // right arrow
        case 68: // D
            move = move.plus(new Vertex(1, 0));
            break;
        case 40: // down arrow
        case 83: // S
            move = move.plus(new Vertex(0, 1));
            break;
        case 32: // space
            world.player.start_fire();
            break;
        case 27: // esc
            world.player.init();
            break;
        default: // debug mode, log key code for yet unmapped keys
            if (debug) {
                console.log(evt.key + " : " + evt.keyCode);
            }
    }
    world.player.set_move(move);
    if(debug){
        logKeysDown(evt);
    }
}

/*
    DEBUGGING
 */
function logKeysDown(ev) {
    if(key !== ev.key) {
        key = ev.key;
        count = 0;
    }
    count++;
    keyElem.textContent = key;
    countElem.textContent = count;
}