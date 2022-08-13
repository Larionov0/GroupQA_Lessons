function getRandomIntInclusive(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1) + min); //The maximum is inclusive and the minimum is inclusive
}


function magic_change(){
    var p = document.getElementById('main_p')

    p.innerText = 'Changed text'
}


function magic_change2(){
    var p = document.getElementById('main_p')

    p.innerText = p.innerText + '!'
}

function magic_change3(){
    var p = document.getElementsByTagName('p')[0]
    red += 0.1
    bord_radius += 1
    p.style['background-color'] = `rgba(255, 0, 0, ${red})`
    p.style['border-radius'] = `${bord_radius}px`
    document.body.style['background-color'] = `rgba(${getRandomIntInclusive(0, 255)}, ${getRandomIntInclusive(0, 255)}, ${getRandomIntInclusive(0, 255)}, 0.4)`
}


var red = 0
var bord_radius = 0

document.getElementById('btn').onclick = magic_change3
