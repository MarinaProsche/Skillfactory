print("Давай играть в крестики-нолики!")
element_1 = "__|__"
element_2 = "|    "

numbers = {"a1": "|   ",
           "a2": "|   ",
           "a3": "|   ",
           "b1": "|   ",
           "b2": "|   ",
           "b3": "|   ",
           "c1": "|   ",
           "c2": "|   ",
           "c3": "|   "}

def check_cross(cross):
    def wrapper_c(*args):
        win_no_one()
        cross()
        if (numbers["a1"] == numbers["b1"] == numbers["c1"] == "|  X"
        or numbers["a2"] == numbers["b2"] == numbers["c2"] == "|  X"
        or numbers["a3"] == numbers["b3"] == numbers["c3"] == "|  X"
        or numbers["a1"] == numbers["a2"] == numbers["a3"] == "|  X"
        or numbers["b1"] == numbers["b2"] == numbers["b3"] == "|  X"
        or numbers["c1"] == numbers["c2"] == numbers["c3"] == "|  X"
        or numbers["a1"] == numbers["b2"] == numbers["c3"] == "|  X"
        or numbers["c1"] == numbers["b2"] == numbers["a3"] == "|  X") :
            row()
            print("Игра окончена! Крестик победил!")
            quit()
        else:
            row()
            null()
    return wrapper_c

def check_null(null):
    def wrapper_n(*args):
        win_no_one()
        null()
        if (numbers["a1"] == numbers["b1"] == numbers["c1"] == "|  0"
        or numbers["a2"] == numbers["b2"] == numbers["c2"] == "|  0"
        or numbers["a3"] == numbers["b3"] == numbers["c3"] == "|  0"
        or numbers["a1"] == numbers["a2"] == numbers["a3"] == "|  0"
        or numbers["b1"] == numbers["b2"] == numbers["b3"] == "|  0"
        or numbers["c1"] == numbers["c2"] == numbers["c3"] == "|  0"
        or numbers["a1"] == numbers["b2"] == numbers["c3"] == "|  0"
        or numbers["c1"] == numbers["b2"] == numbers["a3"] == "|  0"):
            row()
            print("Игра окончена! Нолик победил!")
            quit()
        else:
            row()
            cross()
    return wrapper_n

def win_no_one():
    step = 0
    for key in numbers:
        if numbers[key] == "|  X" or numbers[key] == "|  0":
            step +=1
    if step > 7:
        print("Победила дружба!")
        quit()

def row():
    print("    a    b     c")
    line = 4
    n = 0
    for i in range(line):
        n = n+1
        print(element_1*4)
        if n == 1:
            print(n, numbers["a1"], numbers["b1"], numbers["c1"], element_2)
        elif n == 2:
            print(n, numbers["a2"], numbers["b2"], numbers["c2"], element_2)
        elif n == 3:
            print(n, numbers["a3"], numbers["b3"], numbers["c3"],  element_2)
        else:
            print(" ", element_2*4)

@check_cross
def cross():
    a = input('Введите код квадрата для крестика ("a1", "b2"): ')
    if a not in numbers:
        print("Неверное число. Попробуйте еще раз")
        cross()
    else:
        for key in numbers:
            if key == a:
                if numbers[key] == "|   ":
                    numbers[key] = "|  X"
                    return numbers
                else:
                    print("Квадратик уже занят!")
                    cross()

@check_null
def null():
    b = input('Введите код квадрата для нолика: ')
    if b not in numbers:
        print("Неверный код. Попробуйте еще раз")
        null()
    else:
        for key in numbers:
            if key == b:
                if numbers[key] == "|   ":
                    numbers[key] = "|  0"
                    return numbers
                else:
                    print("Квадратик уже занят!")
                    null()


@check_cross
@check_null
def final():
    check_cross(cross)

final()

