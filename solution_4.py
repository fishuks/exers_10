class RomanNumber:

    def __init__(self, rom_value):
        if self.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            print('ошибка')
            self.rom_value = None

    @staticmethod
    def is_roman(value):
        count_of_signs = {}
        roman_nums = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        for sign in value:
            if sign in roman_nums:
                count_of_signs[sign] = count_of_signs.get(sign, 0) + 1 #исправить то что в конце фолс
        for key, value in count_of_signs.items():
            if value <= 3:
                return True
            else:
                return False

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
        print(decimal_num)

    def __str__(self):
        return f'{self.rom_value}'

    def __repr__(self):
        return f'{self.rom_value}'
