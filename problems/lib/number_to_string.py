"""
Function: Converts a number to the correct British English
words, accepts up to 999 sextillion
"""


def convert_number_to_string(num, use_comma=True):
    if num >= int(1E+25):
        raise ValueError("{:,}: Too large to convert".format(num))

    numbers = [
        int(num / int(1E+21)),
        int(num % int(1E+21) / int(1E+18)),
        int(num % int(1E+18) / int(1E+15)),
        int(num % int(1E+15) / int(1E+12)),
        int(num % int(1E+12) / int(1E+9)),
        int(num % int(1E+9) / int(1E+6)),
        int(num % int(1E+6) / int(1E+3)),
        int(num % int(1E+3))]
    strings = [
        " sextillion",
        " quintillion",
        " quadrillion",
        " trillion",
        " billion",
        " million",
        " thousand",
        ""]
    num_str = []
    for index, i in enumerate(numbers):
        if i > 0:
            num_str.append(_num_to_str(
                numbers[index]) + strings[index])

    if use_comma:
        return ", ".join(num_str)
    else:
        return " ".join(num_str)


def _num_to_str(num):
    tens = _get_str_tens(num % 100)
    hundreds = _get_str_hundreds(num / 100)
    join_array = []
    if hundreds:
        join_array.append(hundreds)
    if tens:
        join_array.append(tens)
    return " and ".join(join_array)


def _get_str_hundreds(num):
    if num > 10:
        raise ValueError(num)
    elif num == 0:
        return None
    elif num == 10:
        return "one thousand"
    else:
        return _get_str_ones(num) + " hundred"


def _get_str_tens(num):
    if num > 99:
        raise ValueError(num)
    if num < 20 and num > 9:
        return _get_str_teens(num)
    elif num < 10:
        return _get_str_ones(num)
    else:
        join_array = []
        ones = _get_str_ones(num % 10)
        tens = _get_twenty_to_ninety(num / 10)
        if tens:
            join_array.append(tens)
        if ones:
            join_array.append(ones)
        return "-".join(join_array)


def _get_str_teens(num):
    if num < 20 and num > 9:
        if num == 19:
            return "nineteen"
        elif num == 18:
            return "eighteen"
        elif num == 17:
            return "seventeen"
        elif num == 16:
            return "sixteen"
        elif num == 15:
            return "fifteen"
        elif num == 14:
            return "fourteen"
        elif num == 13:
            return "thirteen"
        elif num == 12:
            return "twelve"
        elif num == 11:
            return "eleven"
        else:
            return "ten"
    else:
        raise ValueError(num)


def _get_twenty_to_ninety(num):
    if num > 9 or num < 2:
        raise ValueError
    elif num == 9:
        return "ninety"
    elif num == 8:
        return "eighty"
    elif num == 7:
        return "seventy"
    elif num == 6:
        return "sixty"
    elif num == 5:
        return "fifty"
    elif num == 4:
        return "forty"
    elif num == 3:
        return "thirty"
    else:
        return "twenty"


def _get_str_ones(num):
    if num > 9:
        raise ValueError(num)
    elif num == 9:
        return "nine"
    elif num == 8:
        return "eight"
    elif num == 7:
        return "seven"
    elif num == 6:
        return "six"
    elif num == 5:
        return "five"
    elif num == 4:
        return "four"
    elif num == 3:
        return "three"
    elif num == 2:
        return "two"
    elif num == 1:
        return "one"
    else:
        return None
