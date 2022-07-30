def compute_pay():
    pay = 0
    while True:  # Start input loop:
        hours = input('Enter Hours:')
        rate = input('Enter pay for hour:')
        try:
            # Cast hrs, and rate into floats
            hours = float(hours)
            rate = float(rate)
        # Except a ValueError if input is not a digit, and pass.
        except ValueError as e:
            pass

        # If hrs and rate are not floats:
        if not isinstance(hours, float) or not isinstance(rate, float):
            # Prints error message
            print("Error, Please enter numeric input")
            # skip iteration and continuing asking for input
            continue
        else:
            # If inputs are correct, break from input loop:
            break

    if hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    return pay


if __name__ == '__main__':
    compute_pay()
