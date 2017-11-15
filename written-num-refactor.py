"""Convert a number in base-10 into a written out number in English."""
num = int(input('A number between 1 and 99: '))

tens = num // 10
ones = num % 10

def converting_number_tens():
    if tens == 9:
        return 'ninety'
    elif tens == 8:
        return 'eighty'
    elif tens == 7:
        return 'seventy'
    elif tens == 6:
        return  'sixty'
    elif tens == 5:
        return  'fifty'
    elif tens == 4:
        return  'fourty'
    elif tens == 3:
        return 'thirty'
    elif tens == 2:
        return  'twenty'

def converting_number_ones():
    if ones == 9:
        return  'nine'
    elif ones == 8:
        return  'eight'
    elif ones == 7:
        return 'seven'
    elif ones == 6:
        return 'six'
    elif ones == 5:
        return 'five'
    elif ones == 4:
        return 'four'
    elif ones == 3:
        return 'three'
    elif ones == 2:
        return  'two'
    elif ones == 1:
        return  'one'

def converting_number():
    if tens == 0:
        output = ones_word
    elif tens == 1:
        if ones == 1:
            return 'eleven'
        elif ones == 2:
            return 'twelve'
        elif ones == 3:
            return 'thirteen'
        else:
            output = ones_word + 'teen'
    else:
        output = tens_word + '-' + ones_word

tens_written = converting_number_tens(tens)
ones_written = converting_number_ones(ones)

print(tens_written + ones_written)
