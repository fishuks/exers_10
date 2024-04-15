from solution_5 import RomanNumber

num_1 = RomanNumber(214)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)
num_2 = RomanNumber(5690)
print(num_2.int_value)
num_3 = RomanNumber('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)
print(RomanNumber.is_int(-614))
print(RomanNumber.is_int(3758))
{'I': 1,
                      'IV' : 4,
                      'IV' : 6,
                      'V': 5,
                      'IX' : 9,
                      'X': 10,
                      'XI' : 11,
                      'XL' : 40,
                      'L': 50,
                      'LX' : 60,
                      'XC' : 90,
                      'C': 100,
                      'CX' : 110,
                      'CD' : 400,
                      'D': 500,
                      'DC' : 600,
                      'CM' : 900,
                      'M': 1000,
                        'MC' : 1100
                      }