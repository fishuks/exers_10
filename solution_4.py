class RomanNumber:

    def __init__(self, rom_value):
        if self.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            print('ошибка')
            self.rom_value = None

    @staticmethod
    def is_roman(value):
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

    def __str__(self):
        return f'{self.rom_value}'

    def __repr__(self):
        return f'{self.rom_value}'