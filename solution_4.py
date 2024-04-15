class RomanNumber:
    '''
    Class of RomanNumber

    ...

    Сlass instance attribute:
    rom_value : str 
            roman value of number

    '''
    def __init__(self, rom_value):
        '''
        Function that initializes attributes of class instances

        ...

        Parameters:
        rom_value : str 
            roman value of number

        '''
        if self.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            print('ошибка')
            self.rom_value = None

    @staticmethod
    def is_roman(value):
        '''
        Function which determines whether the number is Roman

        ...

        Parameters:
        value : str
                number
        ...

        return : True / False

        '''
        roman_nums = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        prev_sign = 0
        count = 1
        for sign in value:
            if sign not in roman_nums:
                return False
            if prev_sign == sign:
                count += 1
                if count > 3:
                    return False
            else:
                prev_sign = sign
                count = 1
        return True
                
    def decimal_number(self):
        '''
        Function which converts a number to decimal

        ...

        Parameters:
        rom_value : str 
            roman value of number

        ...

        return : decimal_num

        '''
        roman_dict = {'I': 1,
                      'IV' : 4,
                      'V': 5,
                      'XI' : 9,
                      'X': 10,
                      'XL' : 40,
                      'L': 50,
                      'XC' : 90,
                      'C': 100,
                      'CD' : 400,
                      'D': 500,
                      'CM' : 900,
                      'M': 1000
                      }
        decimal_num = 0
        prev_value = 0

        for sign in self.rom_value:
            value = roman_dict[sign]
            if value > prev_value:
                decimal_num += value - 2 * prev_value
            else:
                decimal_num += value
            prev_value = value

        return decimal_num

    def __str__(self):
        '''

        String representation method
    
        '''  
        return f'{self.rom_value}'

    def __repr__(self):
        '''

        String representation method
    
        '''  
        return f'{self.rom_value}'