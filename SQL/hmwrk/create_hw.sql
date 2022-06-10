CREATE TABLE Shoes(
    id INT PRIMARY KEY,
    size_35 INTEGER,
    size_36 INTEGER,
    size_37 INTEGER,
    size_38 INTEGER,
    size_39 INTEGER,
    size_40 INTEGER,
    size_41 INTEGER

);

CREATE TABLE Price_shoes(
    id INT REFERENCES Shoes(id),
    active BOOLEAN,
    main_photo VARCHAR(50),
    photo_link VARCHAR(50),
    description VARCHAR(250),
    measurements VARCHAR(100),
    sale INTEGER
    wholesale INTEGER,
    retail INTEGER,
);

CREATE TABLE Client(
    id INT PRIMARY KEY,
    name VARCHAR(30),
    contact VARCHAR(30),
    information VARCHAR(30),
    balance INTEGER
);

CREATE TABLE Status_order(
    id INT PRIMARY KEY,
    status VARCHAR(20)
);

CREATE TABLE Cart(
    id INT PRIMARY KEY
);

CREATE TABLE CartClient(
    id INT REFERENCES Cart(id),
    client_id INT REFERENCES Client(id)
);

CREATE CartShoes(
    cart_id INT REFERENCES Cart(id),
    shoes_id INT REFERENCES Shoes(id)
    size_ INT
);

CREATE TABLE Order_(
    id INT PRIMARY KEY
);

CREATE TABLE Order_CartStatus(
    order_id INT REFERENCES Order_(id),
    cart_id INT REFERENCES Cart(id),
    status_order_id INT REFERENCES Status_order(id)
);

CREATE TABLE In_work(
    id INT PRIMARY KEY,
    order_id REFERENCES Order_(id),
    datetime TIMESTAMP CURRENT_TIMESTAMP
);

