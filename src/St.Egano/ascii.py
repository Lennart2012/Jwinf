def ascii_convert(number):
    try:
        number = int(number)
        if 0 <= number <= 127:
            letter = chr(number)
            return letter
        else:
            return "The number must be in the range of 0 to 127."
    except ValueError:
        return "Invalid input. Please enter an integer."
