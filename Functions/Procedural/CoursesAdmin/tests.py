import main
import datetime


def test_calculate_teacher_salary_for_lesson():
    """
    Проверить, Подсчет
    :return:
    """

    client1 = {
        'name': 'Bob',
        'surname': 'Bobenko',
        'balance': 1200
    }

    client2 = {
        'name': 'Vasya',
        'surname': 'Vasya',
        'balance': 5000
    }

    teacher = {
        'name': 'TestTeacher',
        'surname': 'Tester',
        'courses': [],
        'master_koef': 1,
        'salary': 1000
    }

    course = {
        'name': 'Test course',
        'description': 'best C course',
        'payment_koef': 300
    }

    group = {
        'number': 1245,
        'students': [client1, client2],
        'teacher': teacher,
        'course': course
    }

    lesson = {
        'date': datetime.date(2021, 7, 30),
        'time': datetime.time(hour=16),
        'duration': datetime.timedelta(hours=1),
        'present_students': [],
        'theme': '',
        'group': group
    }
    correct_result = course['payment_koef'] * 2 ** 0.5

    result = main.calculate_teacher_salary_for_lesson(lesson)
    if result != correct_result:
        print(f'Ошибка в тесте 1: {correct_result} != {result}')
        return

    print('Тест выполнен успешно')


test_calculate_teacher_salary_for_lesson()
