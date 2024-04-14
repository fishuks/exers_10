class RomanNumber:

    def __init__(self, value):
        if self.is_roman(value):
            self.rom_value = value
            self.int_value = self.decimal_number()
        elif self.is_int(value):
            self.int_value = value
            self.rom_value = self.roman_number()
        else:
            print('Ошибка')
            self.rom_value = None
            self.int_value = None

    @staticmethod
    def is_int(value):
        if isinstance(value, int) and value > 0:
            return True
        else:
            return False
        
    @staticmethod
    def is_roman(value):
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
        roman_dict = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
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
    
    def roman_number(self):
        roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
                      400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        result = ''
        for value, numeral in sorted(roman_dict.items(), reverse=True):
            while self.int_value >= value:
                result += numeral
                self.int_value -= value
        return result

    def __str__(self):
        return f'{self.rom_value}'

    def __repr__(self):
        return f'{self.rom_value}'