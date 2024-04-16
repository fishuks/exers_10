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
    
    Сlass attribute:
    roman_dict : dictionary
            dict with roman numbers and their value
    
    '''
    roman_dict = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    
    def __init__(self, value):
        '''
        Function that initializes attributes of class instances

        ...

        Parameters:
        value : str 
                value of number

        '''
        self.value = value
        if isinstance(value, str):
            if RomanNumber.is_roman(value):
                self.rom_value = value
                self.int_value = self.decimal_number()
            else:
                print('Ошибка')
                self.int_value = None
                self.rom_value = None

        elif isinstance(value, int):
            if RomanNumber.is_int(value):
                self.int_value = value
                self.rom_value = self.roman_number()
            else:
                print('Ошибка')
                self.int_value = None
                self.rom_value = None

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
        if isinstance(value, int) and value > 0 and value < 3999:
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
        if value in RomanNumber.roman_dict:
            return True
        
        prev_sign = 0
        count = 0

        for sign in value:
            if sign not in RomanNumber.roman_dict:
                return False
            
            if RomanNumber.roman_dict[sign] > prev_sign:
                if count > 0:
                    return False
                if prev_sign in [5, 50, 500]:
                    return False
                
                count = 1

            if prev_sign == sign:
                count += 1
                if prev_sign in [5, 50, 500]:
                    return False
                if count > 3:
                    return False
            
            else:
                count = 0

            prev_sign = RomanNumber.roman_dict[sign]

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

        if self.rom_value is None:
            return None

        decimal_num = 0
        prev_value = 0

        for sign in self.rom_value:
            value = RomanNumber.roman_dict[sign]
            if value > prev_value:
                decimal_num += value - 2 * prev_value
            else:
                decimal_num += value
            prev_value = value

        return decimal_num
    
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
        
        saved_value = self.int_value
        roman_number = ''
        dictnr = {}
        for key, value in RomanNumber.roman_dict.items():
            dictnr[value] = key
        for value, _ in sorted(dictnr.items(), reverse=True):
            while self.int_value >= value:
                roman_number += dictnr[value]
                self.int_value -= value
        self.int_value = saved_value
        return roman_number

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