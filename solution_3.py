import random
class NavalBattle:
    '''
    Class of NavalBattle

    ...

    Сlass instance attribute:
    symbol : str 
            symbol of user

    Сlass attribute:
    playing_field : list
            list with a field for the game
       
    '''
    playing_field = []

    def __init__(self, symbol):
        '''
        Function that initializes attributes of class instances

        ...

        Parameters:
        symbol : str 
            symbol of user

        '''
        self.symbol = symbol

    @staticmethod
    def show():
        '''
        Function which print a field for the user

        ...

        Parameters:
        playing_field : list
            list with a field for the game

        ...

        return : none

        '''
        for row in NavalBattle.playing_field:
            for cell in row:
                if cell == 0:
                    print('~', end=' ')
                elif cell == 1:
                    print('~', end=' ')
                else:
                    print(cell, end=' ')
            print()

    def shot(self, x, y):
        '''
        Function which makes the shot

        ...

        Parameters:
        x : int
            the x coordinate
        y : int
            the y coordinate
        ...

        return : none

        '''
        if not NavalBattle.playing_field:
            print('Игровое поле не заполнено')
        elif NavalBattle.playing_field[y-1][x-1] == 1:
            NavalBattle.playing_field[y-1][x-1] = self.symbol
            print('Попал!')
        elif NavalBattle.playing_field[y - 1][x - 1] == 0:
            NavalBattle.playing_field[y - 1][x - 1] = "o"
            print('Мимо')
        else:
            print('Ошибка')

    @staticmethod
    def new_game():
        '''
        Function which creates a field for a new game

        ...

        Parameters:
        playing_field : list
            list with a field for the game

        ...

        return : playing_field

        '''
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

        return NavalBattle.playing_field

    def __str__(self):
        '''

        String representation method
    
        '''   
        return f'{self.symbol}'

    def __repr__(self):
        '''

        String representation method
    
        '''   
        return f'{self.symbol}'
