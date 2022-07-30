import sys

while True:  # Start "main loop":
    while True:  # Start input loop:
        hrs = input('Enter Hours:')
        rate = input('Enter pay for hour:')
        try:
            # Cast hrs, and rate into floats
            hrs = float(hrs)
            rate = float(rate)
        # Except a ValueError if input is not a digit, and pass.
        except ValueError as e:
            pass

        # Check if hrs and rate are not floats:
        if not isinstance(hrs, float) or not isinstance(rate, float):
            # Prints error message
            print("Error, Please enter numeric input")
            # skip iteration and continuing asking for input
            continue
        else:
            # If inputs are correct, break from input loop:
            break

    if hrs > 40:
        w = 40 * rate + (hrs - 40) * rate * 1.5
    else:
        w = hrs * rate
        print('pay:', w)

    # Ask user if they would like to continue or quit:
    print('Press "C" to continue or "Q" to quit')

    while True:  # Start input loop:
        user_input = input('> ')
        # If user_input not C or Q
        if user_input.lower() not in ["C", "Q"]:
            # print error message
            print('Incorrect input! Enter either "C" or "Q"\n')
            # Continue asking for input 
            continue
        else:
            break
    # If user selected "C" continue "main loop"
    if user_input.lower().startswith('c'):
        continue
    # If user selected "Q" quit the game.
    elif user_input.lower().startswith('q'):
        print("Goodbye!")
        sys.exit()
