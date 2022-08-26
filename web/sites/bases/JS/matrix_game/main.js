var GRASS_SRC = 'https://art.pixilart.com/02aa0790086f91a.png'


function randomNumber(min, max) { 
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
} 

Array.prototype.random_choice = function(){
    return this[randomNumber(0, this.length - 1)]
}


class Creature {
    constructor (i, j, hp, sprite_src){
        this.i = i
        this.j = j
        this.hp = hp
        this.max_hp = hp
        this.is_alive = true
        this.sprite_src = sprite_src
        this.is_alive = true
    }

    get_damage(){

    }

    move(dir, world){
        if (this instanceof Hero)
            debugger
        switch (dir) {
            case 'w':
                if (this.i != 0) this.i -= 1
                break;
            
            case 'a':
                if (this.j != 0) this.j -= 1
                break;
            
            case 's':
                if (this.i != world.n-1) this.i += 1
                break;

            case 'd':
                if (this.j != world.m-1) this.j += 1
                break;
        
            default:
                break;
        }
    }

    die (){
        this.is_alive = false
    }
}


class Animal extends Creature {
    my_turn(world){
        throw {name : "NotImplementedError", message : "too lazy to implement"}; 
    }
}


class Hero extends Creature {
    constructor (name, i, j, hp=10, main_weapon=null, points=0){
        super(i, j, hp, 'https://tokegameart.net/wp-content/uploads/2018/03/01-Cool-Boy-2D-Game-Character-Sprite.png')
        this.name = name
        this.main_weapon = main_weapon
        this.points = points
        this.inventory = []
    }

    update(key, world){
        this.move(key, world)
        for (let animal of world.alive_animals){
            if (animal instanceof Chicken){
                if (this.i == animal.i & this.j == animal.j){
                    animal.die()
                    this.points += 1
                }
            }
        }
        world.drawer.draw_html()
    }
}


class Chicken extends Animal {
    constructor (i, j, name='new'){
        super(i, j, 3, 'https://media1.giphy.com/media/l3vR9IEU6nYAmZyoM/giphy.gif')
        this.name = name
    }

    my_turn(world){
        this.move(['w', 'a', 's', 'd'].random_choice(), world)
    }
}


class Setupper{
    constructor (world){
        this.world = world
    }

    setup_listeners(){
        document.addEventListener('keyup', (event)=>{
            this.world.keyup(event.key)
        })
    }

    setup_interval(){
        setInterval(()=>{this.world.update()}, 500)
    }

    setup(){
        var r = document.querySelector(':root');
        r.style.setProperty('--w', `${100 / this.world.m}%`)
        r.style.setProperty('--h', `${100 / this.world.n}%`)

        this.setup_listeners()
        this.setup_interval()
    }
}


class Drawer {
    constructor (world){
        this.world = world
    }

    create_matrix(){
        var matrix = []
        for (let i = 0; i < this.world.n; i++){
            var row = []
            for (let j = 0; j < this.world.m; j++){
                row.push(GRASS_SRC)
            }
            matrix.push(row)
        }
        return matrix
    }

    fill_matrix(matrix){
        for (let obj of this.world.all_objects()){
            matrix[obj.i][obj.j] = obj.sprite_src
        }
    }

    create_html(matrix){
        var html = ''
        for (let row of matrix){
            html += `<div class='row'>`
            for (let src of row){
                html += `<div class='cell'><img src='${src}' class='sprite'></div>`
            }
            html += `</div>`
        }
        return html
    }

    draw_html (){
        var matrix = this.create_matrix()
        this.fill_matrix(matrix)
        document.getElementById('map').innerHTML = this.create_html(matrix)
        document.getElementById('points').innerText = this.world.hero.points
    }
}


class World {
    constructor(n, m){
        this.n = n
        this.m = m

        this.hero = new Hero('Bob', 3, 4)
        this.animals = [
            new Chicken(1, 6, 'Ryaba'),
            new Chicken(6, 8)
        ]

        this.round = 0
        this.drawer = new Drawer(this)
        this.setupper = new Setupper(this)
    }

    get alive_animals(){
        return this.animals.filter((creature)=>{ return creature.is_alive })
    }

    all_objects(){
        return [this.hero, ...this.alive_animals]
    }

    run(){
        this.setupper.setup()

        this.drawer.draw_html()
    }

    keyup(key){
        if (['w', 'a', 's', 'd'].includes(key)){
            this.hero.update(key, this)
        }
    }

    update(){
        for (let animal of this.alive_animals){
            animal.my_turn(world)
        }
        this.animals = this.alive_animals

        this.spawn()

        
        this.drawer.draw_html()
        this.round += 1
    }

    spawn(){
        if (this.round % 10 == 0){
            this.animals.push(new Chicken(randomNumber(0, this.n-1), randomNumber(0, this.m-1)))
        }
    }
}


var world = new World(14, 16)
world.update()
world.run()
