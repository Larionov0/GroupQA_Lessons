import sqlite3
import plotly.graph_objs as go


connection = sqlite3.connect('test_db.db')
cursor = connection.cursor()


def get_users_table():
    cursor.execute('SELECT * FROM User')
    table = cursor.fetchall()
    print(table)


def get_users_table_harder():
    params = ['id', 'name', 'age']
    cursor.execute(f'SELECT {",".join(params)} FROM User')
    table = cursor.fetchall()
    print(table)


def get_groups_and_users():
    cursor.execute('SELECT User.id, User.name, age, Group_.id, Group_.name as group_name '
                   'FROM User JOIN Group_ '
                   'ON User.group_id = Group_.id')
    for row in cursor.fetchall():
        print(row)


def build_diagram():
    """
    Пользователь вводи группы, которые необходимо проаналировать.
    Мы делаем выборку из бд всех студентов, которые относятся к этим групам.
    И строим диаграму с именами студентов и возрастами.
    :return:
    """
    groups = input('Введіть групи для аналізу через пробіл: ')
    groups = groups.split(' ')

    where = ' OR '.join([f"Group_.name='{group}'" for group in groups])

    query = f"SELECT User.name, User.age, Group_.name " \
            f"FROM User JOIN Group_ " \
            f"ON User.group_id = Group_.id " \
            f"WHERE {where}"
    print(query)
    cursor.execute(query)
    x = []
    y = []

    for row in cursor.fetchall():
        x.append(f"{row[0]} ({row[2]})")
        y.append(row[1])

    go.Figure(data=[go.Bar(x=x, y=y)]).write_html('diag.html', auto_open=True)


build_diagram()
