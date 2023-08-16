let BASE_MISSILE_SPEED = 1;
let BASE_PLAYER_SPEED = 0.2;
let WORLD_END_X = 20;
let WORLD_END_Y = 20;


export class Vertex {
    /*
        2D vector
     */
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    copy(){
        return new Vertex(this.x, this.y);
    }
    [Symbol.iterator]() {
        return [this.x, this.y][Symbol.iterator]();
    }
    set(x, y){
        this.x = x;
        this.y = y;
    }
    length(){
        return Math.sqrt(this.x**2 + this.y**2);
    }
    times(a){
        return new Vertex(a * this.x, a * this.y);
    }
    rotate(theta){
        return new Vertex(Math.cos(theta) * this.x - Math.sin(theta) * this.y,
            Math.sin(theta) * this.x + Math.cos(theta) * this.y
        );
    }
    plus(vertex) {
        return new Vertex(this.x + vertex.x, this.y + vertex.y);
    }
    standardized(){
        // return the unit vertex with the same orientation
        let l = this.length();
        return new Vertex(this.x/l, this.y/l);
    }
    /*
        Algebra
     */
    dot(vertex){
        return this.x * vertex.x + this.y * vertex.y;
    }
    transform(vertex){
        /*
            where vertex is understood as a complex: x+iy coding for geometric transform
         */
        return new Vertex(this.x * vertex.x - this.y * vertex.y,
            this.x * vertex.y + this.y * vertex.x);
    }
}

class Box {
    constructor(topleft, bottomright) {
        this.topleft = topleft;
        this.bottomright = bottomright;
    }
    is_in(vertex){
        return vertex.x >= this.topleft.x && vertex.x <= this.bottomright.x &&
            vertex.y >= this.topleft.y && vertex.y <= this.bottomright.y;
    }
}

class MovingObject {
    /*
        Object with position, orientation, velocity
     */
    constructor(px=0, py=0, vx=0, vy=0, ox=0, oy=0) {
        this.position = new Vertex(px, py);
        this.orientation = new Vertex(ox, oy);
        this.velocity = new Vertex(vx, vy);
    }
    speed(){
        return this.velocity.length();
    }
    moveBy(translateVertex){
        this.position = this.position.plus(translateVertex);
        this.orientation = translateVertex.standardized();
        return this;
    }
    moveTo(vertex){
        return moveBy(vertex.plus(this.position.times(-1)));
    }
    cruise(){
        // increment position by a step with current speed
        this.position = this.position.plus(this.velocity);
        return this;
    }
    is_out_of_world(){
        return this.position
    }
}
class Missile extends MovingObject {
    constructor(parent) {
        super(...parent.position, ...parent.missile_speed(), ...parent.orientation);
        this.parent = parent;
    }
}

class Player extends MovingObject {
    missileSpeed = BASE_MISSILE_SPEED;
    playerSpeed = BASE_PLAYER_SPEED;
    firing = false;
    moving = null;
    start_fire(){
        this.firing = true;
        return this;
    }
    stop_fire(){
        this.firing = false;
        return this;
    }
    start_move(x, y){
        this.moving = new Vertex(x, y).standardized();
        return this;
    }
    stop_move(){
        this.moving = null;
        this.velocity = new Vertex(0, 0);
        return this;
    }
    set_move(vertex){
        if(vertex.length() === 0){
            this.stop_move();
        }
        else{
            this.start_move(...vertex);
        }
        return this;
    }
    move(){
        if(this.moving !== null){
            this.moveBy(this.moving.times(this.playerSpeed)).stop_move();
        }
        return this;
    }
    fire(){
        if(this.firing){
            let bullet = new Missile(this);
            world.missiles.push(bullet);
            this.stop_fire();
        }
        return this;
    }
    init(){
        this.position.set(0, 0);
        this.orientation.set(1, 0);
        this.velocity.set(0, 0);
        return this;
    }
    missile_speed(){
        return this.orientation.times(this.missileSpeed).plus(this.velocity);
    }
}

export let world = {};

export function init_physics(){
    world.player = (new Player()).init();
    world.missiles = [];
    world.frame = new Box(new Vertex(0, 0), new Vertex(WORLD_END_X, WORLD_END_Y));
}

function step_missiles(){
    for(const m of world.missiles){
        m.cruise();
    }
    world.missiles = world.missiles.filter(x => world.frame.is_in(x.position));
}

export function step_physics(){
    world.player.move().fire();
    step_missiles();
}
init_physics();
