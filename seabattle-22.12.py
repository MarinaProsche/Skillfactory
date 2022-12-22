from random import randint

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Boardexception(Exception):
    pass

class BoardOutException(Boardexception):
    def __str__(self):
        print("Вы стреляете за доску")

class BoardRepeatException(Boardexception):
    def __str__(self):
        print("Вы уже стреляли сюда")

class Ship:
    def __init__(self, x, y, length, rotation):
        self.x = x
        self.y = y
        self.length = length
        self.rotation = rotation
        self.left = length

    @property
    def construct_ship(self):
        full_ship = []
        x_next = self.x
        y_next = self.y
        for i in range(self.length):
            if self.rotation == "-":
                x_next = x_next + i
            elif self.rotation == "|":
                y_next = y_next + i

            new_dot = (x_next, y_next)
            full_ship.append(new_dot)

        return full_ship

    def check_shoot(self, shoot):
        if shoot in self.construct_ship:
            return True
        else:
            return False

class Board:
    def __init__(self, visibility = False, size = 6):
        self.visibility = visibility
        self.size = size
        self.field = [["0"] * (self.size) for a in range(self.size)]
        self.count = 0 #количество пораженных кораблей

        self.busy = [] #занятые точки
        self.ships = [] #все корабли на доске

    def field_full(self):
        print("  | 1 | 2 | 3 | 4 | 5 | 6 |")

        for i, row in enumerate(self.field):
            field_full = f'{i+1} | {" | ".join(row)} |'
            print(field_full)

        if self.visibility == True:
            field_full = field_full.replace("■", "O")
            return field_full

    def out_field(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def contour(self, ship, verb = False):
        near = [
            (-1, -1), (-1, 0) , (-1, 1),
            (0, -1), (0, 0) , (0 , 1),
            (1, -1), (1, 0) , (1, 1)
        ]
        for d in ship.construct_ship:
            for dx, dy in near:
                around = Dot(d.x + dx, d.y + dy)
                if not(self.out_field(around)) and around not in self.busy:
                    if verb:
                        self.field[around.x][around.y] = "."
                    self.busy.append(around)

    def add_ship(self, ship):
        for d in ship.construct_ship:
            if self.out_field(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.construct_ship:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)


ship = Ship(2,3,2,"-")
print(ship.construct_ship)

b = Board()

desk = b.field_full()
desk.add_ship(Ship(2,3,2,"-"))
print(desk.busy())


