debug = true;
key = null;
count = 0;
cell_size = 30;

window.onload = function() {
    init();
    render();
}
/*
    INIT
 */
function init(){
    init_elements();
    init_events();
    init_game();
}
function init_elements(){
    keyElem = document.getElementById("key");
    countElem = document.getElementById("count");
    mainCanvasElem = document.getElementById("mainCanvas");
    mainCtx = mainCanvasElem.getContext("2d");
}
function init_events(){
    document.addEventListener("keydown",keyPush);
}
function init_game(){
    player = {}
    player.px = 0;
    player.py = 0;
}
/*
    GAME LOOP
 */
function game_step(){
    render();
}
function game_start(){
    // boucle infinie : appelle la fonction game() toutes les 15/1000 de seconde
    started = true;
    interval_id = setInterval(game_step,1000/15);
}
function game_stop(display_gameover=true){
    started = false;
    // si la boucle infinie tourne, alors on l'arrete et on affiche l'ecran game over
    if(interval_id !== undefined){
        // on arrete la boucle
        clearInterval(interval_id);
        interval_id = undefined;
    }
}
function game_pause() {
    stop_game(false);
}
game_unpause = game_start();
/*
    RENDERING
 */
function render(){
    render_background();
    render_square(px, py);
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
    mainCtx.ellipse(x * cell_size + radius, y * cell_size + radius, radius);
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
/*
    GAME LOGIC
 */
function moveBy(x, y){
    player.px += x;
    player.py += y;
}
function moveTo(x, y){
    player.px = x;
    player.py = y;
}
/*
    KEY BINDINGS
 */
function keyPush(evt) {
    /*
        Here we map what to do on a key press.
        It is possible to play with the arrow keys or with ZQSD.
    */
    switch (evt.keyCode) {
        case 37: // left arrow
        case 81: // Q
        case 65: // A
            moveBy(-1, 0);
            break;
        case 38: // up arrow
        case 90: // Z
        case 87: // W
            moveBy(0, -1);
            break;
        case 39: // right arrow
        case 68: // D
            moveBy(1, 0);
            break;
        case 40: // down arrow
        case 83: // S
            moveBy(0, 1);
            break;
        case 27: // echap
            px=py=0;
            break;
        default: // debug mode, log key code for yet unmapped keys
            if (debug) {
                console.log(evt.key + " : " + evt.keyCode);
            }
    }
    if(debug){
        logKeysDown(evt);
    }
}

