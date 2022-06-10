CREATE TABLE Ingredient (
    id INT PRIMARY KEY,
    name VARCHAR(30),
    price FLOAT
);


CREATE TABLE Pizza (
    id INT PRIMARY KEY,
    name VARCHAR(20),
    is_custom BOOLEAN
);


CREATE TABLE Cart (
    id INT PRIMARY KEY
);


CREATE TABLE User_ (
    id INT PRIMARY KEY,
    username VARCHAR(20),
    phone VARCHAR(20),
    email VARCHAR(30),
    cur_cart_id INT NULL REFERENCES Cart(id)
);


CREATE TABLE IngredientInPizza (
    ingredient_id INT REFERENCES Ingredient(id),
    pizza_id INT REFERENCES Pizza(id),
    grams INT,
    PRIMARY KEY (ingredient_id, pizza_id)
);


CREATE TABLE PizzaCart (
    id INT PRIMARY KEY,
    cart_id INT REFERENCES Cart(id),
    pizza_id INT REFERENCES Pizza(id)
);


CREATE TABLE Orders (
    id INT PRIMARY KEY,
    datetime TIMESTAMP CURRENT_TIMESTAMP,
    price FLOAT,
    address VARCHAR(50),
    cart_id INT REFERENCES Cart(id),
    user_id INT REFERENCES User_(id)
);
