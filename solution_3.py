import random
class NavalBattle:
    playing_field = []
  

    def __init__(self, symbol):
        self.symbol = symbol

    @staticmethod
    def show():
        for row in NavalBattle.playing_field:
            for cell in row:
                if cell == 0:
                    print("~", end=" ")
                elif cell == 1:
                    print("~", end=" ")
                else:
                    print(cell, end=" ")
            print()

    def shot(self, x, y):
        if not NavalBattle.playing_field:
            print('игровое поле не заполнено')
        elif NavalBattle.playing_field[y-1][x-1] == 1:
            NavalBattle.playing_field[y-1][x-1] = self.symbol
            print("Попал!")
        elif NavalBattle.playing_field[y - 1][x - 1] == 0:
            NavalBattle.playing_field[y - 1][x - 1] = "o"
            print("Мимо")
        else:
            print('ошибка')

    @staticmethod
    def new_game():
        NavalBattle.playing_field = [[0 for _ in range(10)] for _ in range(10)]  
        ships = [(4, 1), (3, 2), (2, 3), (1, 4)]  

        for ship_size, ship_count in ships:
            for _ in range(ship_count):
                while True:
                    x = random.randint(0, 9) 
                    y = random.randint(0, 9) 
                    orient = random.choice(['h', 'v'])  

                    if orient == 'h' and x + ship_size <= 10: 
                        valid = all(0 <= x+i < 10 and NavalBattle.playing_field[y][x+i] == 0 for i in range(ship_size)) 
                        if valid:
                            intersect = False
                            for i in range(ship_size):
                                if any(0 <= y+j < 10 and 0 <= x+i < 10 and NavalBattle.playing_field[y+j][x+i] == 1 for j in [-1, 0, 1] for i in [-1, 0, 1]):
                                    intersect = True
                                    break
                            if not intersect:
                                for i in range(ship_size):
                                    NavalBattle.playing_field[y][x+i] = 1  
                                break

                    elif orient == 'v' and y + ship_size <= 10: 
                        valid = all(0 <= y+i < 10 and NavalBattle.playing_field[y+i][x] == 0 for i in range(ship_size))  
                        if valid:
                            intersect = False
                            for i in range(ship_size):
                                if any(0 <= y+i < 10 and 0 <= x+j < 10 and NavalBattle.playing_field[y+i][x+j] == 1 for j in [-1, 0, 1] for i in [-1, 0, 1]):
                                    intersect = True
                                    break
                            if not intersect:
                                for i in range(ship_size):
                                    NavalBattle.playing_field[y+i][x] = 1  
                                break

        print(NavalBattle.playing_field)
        for row in NavalBattle.playing_field:
            for cell in row:
                if cell == 0:
                    print(0, end = ' ')
                elif cell == 1:
                    print(1, end=" ")
                else:
                    print(cell, end=" ")
            print()

        return NavalBattle.playing_field

    def __str__(self):
        return f'{self.symbol}'

    def __repr__(self):
        return f'{self.symbol}'
