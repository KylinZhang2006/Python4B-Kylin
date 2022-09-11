class LivingThing:
    def __init__(self, habit):
        self.habit = habit

    def set_habit(self, habit):
        self.habit = habit

    def get_habit(self):
        return self.habit


class Animal(LivingThing):
    def __init__(self, habit, is_carnivore):
        super().__init__(habit)
        self.is_carnivore = is_carnivore

    def get_is_carnivore(self):
        return self.is_carnivore


class Plant(LivingThing):
    def __init__(self, habit):
        super().__init__(habit)


class Flower(Plant):
    def __init__(self, habit, colour):
        super().__init__(habit)
        self.colour = colour


class Tree(Plant):
    def __init__(self, habit, branch_num):
        self.branch_num = branch_num
        super().__init__(habit)


class Caribou(Animal):
    def __init__(self, habit, is_carnivore):
        super().__init__(habit, is_carnivore)


class Wolf(Animal):
    def __init__(self, habit, is_carnivore, pack_leader):
        self.pack_leader = pack_leader
        super().__init__(habit, is_carnivore)


class Dandelion(Flower):
    def __init__(self, colour, habit):
        super().__init__(colour, habit)


class Rose(Flower):
    def __init__(self, colour, habit):
        super().__init__(colour, habit)


class Maple(Tree):
    def __init__(self, branch_num, habit):
        super().__init__(branch_num, habit)