def number_to_numeral(number):
    numerals_dict = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
        6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
        20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L',
        60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
        100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
        600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
        1000: 'M', 2000: 'MM', 3000: 'MMM'
    }

    if number in numerals_dict:
        return numerals_dict[number]

    result = ''
    for place_value in [1000, 100, 10, 1]:
        digit = number // place_value
        if digit > 0:
            result += numerals_dict[digit * place_value]
            number %= place_value
    return result

def main():
    entered = input("Enter a decimal number: ")
    print(number_to_numeral(int(entered)))

if __name__ == '__main__':
    main()
