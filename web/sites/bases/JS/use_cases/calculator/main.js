var cur_number1 = ''
var sign = ''
var cur_number2 = ''

var output = document.getElementById('screen')

for (let number=0; number<10; number++){
    document.getElementById(`${number}`).onclick = function(){
        if (sign == ''){
            cur_number1 += `${number}`
        } else {
            cur_number2 += `${number}`
        }

        output.innerText = cur_number1 + sign + cur_number2
    }
}


for (let operation of ['+', '-', '*', '/']) {
    document.getElementById(operation).onclick = function(){
        if (cur_number1 == ''){

        } else if (cur_number2 == ''){
            sign = operation
        } else {
            equal()
            sign = operation
        }
        output.innerText = cur_number1 + sign + cur_number2
    }
}


function equal(){
    cur_number1 = eval(cur_number1 + sign + cur_number2)
    cur_number2 = ''
    sign = ''
    output.innerText = cur_number1 + sign + cur_number2
}


document.getElementById('=').onclick = function(){
    equal()
}
