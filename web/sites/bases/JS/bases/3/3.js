function find_max_price_product(store_list){
    var max_prod = ''
    var max_price = 0

    for (let prod of store_list){
        if (prod.price > max_price) {
            max_price = prod.price
            max_prod = prod.name
        }
    }

    return [max_prod, max_price]
}



store = [
    {
        name: 'молоко',
        price: 100
    },
    {
        name: 'хліб',
        price: 30
    },
    {
        name: 'сосиски',
        price: 130
    },
    {
        name: 'яйця',
        price: 50
    },
]


var [prod, price] = find_max_price_product(store)

console.log(prod, price)
