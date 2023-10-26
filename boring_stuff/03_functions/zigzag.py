import time
import sys

indent = 0
# Flag if indent increase or not
indentIncrease = True

try:
    while True:
        # end='' removes the new line character
        # keeps the print on the same line
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)  # Pause for 1/10 second

        if indentIncrease:
            # Increase indent
            indent += 1
            if indent == 20:
                # Change direction
                indentIncrease = False
        else:
            # decrease indent
            indent -= 1
            if indent == 0:
                # Change direction
                indentIncrease = True

# exit the program wge key is pressed
except KeyboardInterrupt:
    # Ctrl+C to end
    sys.exit()
