var GRASS_SRC = 'https://art.pixilart.com/02aa0790086f91a.png'


class Creature {
    constructor (i, j, hp, sprite_src){
        this.i = i
        this.j = j
        this.hp = hp
        this.max_hp = hp
        this.is_alive = true
        this.sprite_src = sprite_src
    }

    get_damage(){

    }

    move(dir, world){
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
}


class Hero extends Creature {
    constructor (name, i, j, hp=10, main_weapon=null, coins=0){
        super(i, j, hp, 'https://tokegameart.net/wp-content/uploads/2018/03/01-Cool-Boy-2D-Game-Character-Sprite.png')
        this.name = name
        this.main_weapon = main_weapon
        this.coins = coins
        this.inventory = []
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

    setup(){
        var r = document.querySelector(':root');
        r.style.setProperty('--w', `${100 / this.world.m}%`)
        r.style.setProperty('--h', `${100 / this.world.n}%`)

        this.setup_listeners()
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
    }
}


class World {
    constructor(n, m){
        this.n = n
        this.m = m

        this.hero = new Hero('Bob', 3, 4)
        this.animals = []

        this.round = 0
        this.drawer = new Drawer(this)
        this.setupper = new Setupper(this)
    }

    all_objects(){
        return [this.hero, ...this.animals]
    }

    run(){
        this.setupper.setup()

        this.drawer.draw_html()
    }

    keyup(key){
        if (['w', 'a', 's', 'd'].includes(key)){
            this.hero.move(key, this)

            // others move
            this.drawer.draw_html()
        }
    }
}



var world = new World(14, 16)
world.run()
