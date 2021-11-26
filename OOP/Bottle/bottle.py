class Bottle:
    v = 5
    material = 'пластик'
    liquids = {}

    def add_liquid(self, liquid, v) -> float:
        if liquid not in self.liquids:
            self.liquids[liquid] = 0

        free_v = self.v - self.filled_v()
        if v > free_v:
            v = free_v
        self.liquids[liquid] += v

    def poor_out(self, v) -> dict:
        filled_v = self.filled_v()
        remaining_v = filled_v - v if v < filled_v else 0

        k = remaining_v / filled_v  # 0.6

        return_dict = {}
        for liquid in list(self.liquids):
            v = self.liquids[liquid]
            self.liquids[liquid] = v * k
            return_dict[liquid] = v * (1 - k)
            if self.liquids[liquid] == 0:  # удаление нулевых жидкостей
                self.liquids.pop(liquid)
        return return_dict

    def calculate_in_percents(self) -> dict:
        """
        бутылка: 8
        {
            'вода': 4,
            "молоко": 1
        }
        ->
        {
            'вода': 80,
            "молоко": 20
        }
        :return:
        """
        pass

    def how_much(self, liquid) -> float:
        """
        Обязательно!
        бутылка: 8
        {
            'вода': 4,
            "молоко": 1
        }

        b.how_much('вода') -> 4
        b.how_much('слизь') -> 0
        """
        pass

    def filled_v(self) -> float:
        return sum(self.liquids.values())

    def add_liquids(self, liquids: dict):
        # нужно предусомтреть вариант с переполнением бутылки и пропорционально вылить часть каждой из жидкостей из
        # liquids перед заливанием в self.liquids

        for liquid, v in liquids.items():
            self.add_liquid(liquid, v)


b1 = Bottle()
b1.v = 9
b1.liquids = {}

b1.add_liquid('вода', 3)
b1.add_liquid('молоко', 3)
b1.add_liquid('слизь', 1)


b2 = Bottle()
b2.v = 10
b2.add_liquid('сера', 2)

b2.add_liquids(b1.poor_out(4))

print(b1.liquids)
print(b2.liquids)
