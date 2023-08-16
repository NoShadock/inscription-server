/*
    INIT
 */
import {game_start} from "./loop.js";
import {render} from "./rendering.js";
import {keyPush} from "./keymap.js";
import {init_physics} from "./physics.js";

export let keyElem, countElem, mainCanvasElem, mainCtx;

window.onload = function() {
    init();
    render();
    game_start();
}

export function init(){
    init_elements();
    init_events();
    init_physics();
}
function init_elements(){
    keyElem = document.getElementById("key");
    countElem = document.getElementById("count");
    mainCanvasElem = document.getElementById("mainCanvas");
    mainCtx = mainCanvasElem.getContext("2d");
}
function init_events(){
    document.addEventListener("keydown", keyPush);
}
