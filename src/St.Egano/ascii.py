def ascii_convert(number):

    number = int(number)
    if 0 <= number <= 127:
        letter = chr(number)
        return letter
    else:
        return "?"
