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
        pass

    def __str__(self):
        return f'{self.symbol}'

    def __repr__(self):
        return f'{self.symbol}'

