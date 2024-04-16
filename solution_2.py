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
        if NavalBattle.playing_field[y-1][x-1] == 1:
            NavalBattle.playing_field[y-1][x-1] = self.symbol
            print('Попал!')
        elif NavalBattle.playing_field[y - 1][x - 1] == 0:
            NavalBattle.playing_field[y - 1][x - 1] = "o"
            print('Мимо')
        
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

