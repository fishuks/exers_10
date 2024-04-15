class RomanNumber:
    '''
    Class of RomanNumber

    ...

    Сlass instance attribute:
    value : str 
            value of number
    rom_value : str 
            roman value of number
    int_value : int
            integer value of number
    
    '''
    def __init__(self, value):
        '''
        Function that initializes attributes of class instances

        ...

        Parameters:
        value : str 
                value of number

        '''
        if self.is_roman(value):
            self.rom_value = value
            self.int_value = 0
        elif self.is_int(value):
            self.int_value = value
            self.rom_value = ''
        else:
            print('Ошибка')
            self.rom_value = None
            self.int_value = None

    @staticmethod
    def is_int(value):
        '''
        Function which determines whether a number is an integer
        ...

        Parameters:
        value : str
                number
        ...

        return : True / False

        '''
        if isinstance(value, int) and value > 0:
            return True
        else:
            return False
        
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
        for sign in str(value):
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
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000
                      }
        if not self.decimal_number:
            decimal_num = 0
            prev_value = 0

            for sign in self.rom_value:
                value = roman_dict[sign]
                if value > prev_value:
                    decimal_num += value - 2 * prev_value
                else:
                    decimal_num += value
                prev_value = value
            self.decimal_number = decimal_num
        return self.decimal_number
    
    def roman_number(self):
        '''
        Function which converts a number to decimal

        ...

        Parameters:
        int_value : int
            integer value of number

        ...

        return : rom_value

        '''
        roman_dict = {1: 'I', 5: 'V',10: 'X', 50: 'L',100: 'C',
                      500: 'D',1000: 'M'}
        if not self.rom_value:
            roman_number = ''
            for value, numeral in sorted(roman_dict.items(), reverse=True):
                while self.int_value >= value:
                    roman_number += numeral
                    self.int_value -= value
            roman_number = self.rom_value
        return self.rom_value

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