# watch = StopWatch()
# watch.add_now('Старт')
# lst = [random.randint(0, 100) for _ in range(10000000)]
# watch.add_now('Сгенерирован список случайных чисел')
#
# all_data = []
# for link in ['youtube.com', 'vk.com', 'instagram.com', 'facebook.com']:
#     data = скачать_чтото(откуда=link)
#     all_data.append(data)
#     watch.add_now(f"Скачано из {link}")
#
# result = проанализировать_данные(данные=all_data)
# watch.add_now('Данные проанализированны')
#
# print(watch.get_statistic_string())

from time import time
import random


class StopWatch:
    def __init__(self):
        self.comment = ''
        self.history = []
        self.total = 0
        self.now_time = None

    def add_now(self, comment):
        self.comment = comment
        if self.now_time is None:
            self.set_now_time()
            self.history.append(f"{self.now_time} - '{self.comment}'")
        else:
            past_time = time() - self.now_time
            self.total += past_time
            self.history.append(f"{self.now_time} - '{self.comment}'(spent {past_time})")

    def set_now_time(self):
        self.now_time = time()

    def get_statistic_string(self):
        text = ''
        for num, el in enumerate(self.history, start=1):
            text += f"{num}. {el}\n"
        text += f"\nTotal: {self.total}"
        return text


watch = StopWatch()
watch.add_now('Старт')
lst = [random.randint(0, 100) for _ in range(10000000)]
watch.add_now('Сгенерирован список случайных чисел')
lst_2 = [random.randint(0, 50) for _ in range(15000000)]
watch.add_now('Сгенерирован список_2 случайных чисел')
print(watch.get_statistic_string())
