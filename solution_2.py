class NavalBattle :

    playing_field = []

    def __init__(self, symbol):
        self.symbol = symbol


    @staticmethod
    def show():

        for field in NavalBattle.playing_field:
            for sign in field:
                if sign == 0 or sign == 1:
                    NavalBattle.playing_field[NavalBattle.playing_field.index(field)][sign] == '~'
                    return NavalBattle.playing_field
                else:
                    NavalBattle.playing_field[field][sign] == sign
                    return NavalBattle.playing_field
    
    def shot(self, x, y):
        if self.playing_field[x - 1][y - 1] == 0:
            self.playing_field[x - 1][y - 1] == 'o'
            return 'мимо'
        elif self.playing_field[x - 1][y - 1] == 1:
            self.playing_field[x - 1][y - 1] == self.symbol
            return 'попал'
        
    def __str__(self):
        return f'{self.symbol}'

    def __repr__(self):
        return f'{self.symbol}'

