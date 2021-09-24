

while True:
    pas = input('Enter your password:   ')

    if pas == '111':
        with open('secret.txt', 'rt', encoding='utf-8') as file:
            text = file.read()
        print(text)
        break
    else:
        print('Try again')


