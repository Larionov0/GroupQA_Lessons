import pickle


data = {
    'a': [1, 2, 3],
    'b': [3, 4, 5],
    'c': {
        'k': 'lol',
        'as': 'kokog'
    }
}


with open('data.dat', 'wb') as file:
    bytes_ = pickle.dumps(data)
    file.write(bytes_)
    # pickle.dump(data, file)


with open('data.dat', 'rb') as file:
    bytes_ = file.read()
    data2 = pickle.loads(bytes_)


print(data)
print(data2)
