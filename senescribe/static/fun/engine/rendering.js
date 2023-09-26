/*
    RENDERING
 */
import {mainCanvasElem, mainCtx} from "./init.js"
import {world} from "./physics.js";

let cell_size = 20;

export function render(){
    render_background();
    render_square(...world.player.position);
    for(const m of world.missiles){
        render_circle(...m.position);
    }
}
function render_background(){
    mainCtx.fillStyle="black";
    mainCtx.fillRect(0,0,mainCanvasElem.width,mainCanvasElem.height);
}
function render_square(x, y, length=cell_size, border=2, color="white"){
    mainCtx.fillStyle=color;
    mainCtx.fillRect(x * cell_size, y * cell_size, length-border, length-border);
}
function render_circle(x, y, radius=cell_size/3, color="yellow"){
    mainCtx.fillStyle=color;
    mainCtx.beginPath();
    mainCtx.ellipse(x * cell_size + radius, y * cell_size + radius,
        radius, radius, 0, 0, 2 * Math.PI);
    mainCtx.fill();
}
