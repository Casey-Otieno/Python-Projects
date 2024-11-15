''' Sevseg, by AI Swelgart al@inventwithpython.com
A seven_segment number module, used by the Countdown and Digital Clock Program.

A labeled seven_segment display, with each segment labeled A to G:

 _A_
|   |       Each digit in a seven_segment display:
F   B        _     _   _       _   _  _   _   _
|_G_|       | | |  _|  _| |_| |_  |_   | |_| |_|
|   |       |_| | |_   _|   |  _| |_|  | |_|  _|
E   C        
|_D_|'''


def getSevSegStr(number, minwidth=0):
    '''Return a seven_sgment display string of number. The returned string
     will be padded with zeros if it is smaller than minwidth.'''

     # Convert number to string in case it's an int or float
    number=str(number).zfill(minwidth)

    rows=['', '', '']
    for i, numeral in enumerate(number):
        if numeral ==".": # Render the decimal point.
            rows[0] +=' '
            rows[1] +=' '
            rows[2] +='.'
            continue # Skip the space in between digits.
        elif numeral== '-': # Render the negative sign
            rows[0] +=''
            rows[1] +=''
            rows[2] +='-'
        elif numeral== '0': # Render the 0
            rows[0] +=' _ '
            rows[1] +='| |'
            rows[2] +='|_|'
        elif numeral== '1': # Render the 1
            rows[0] +='   '
            rows[1] +='  |'
            rows[2] +='  |'
        elif numeral== '2': # Render the 2
            rows[0] +=' _ '
            rows[1] +=' _|'
            rows[2] +='|_ '
        elif numeral== '3': # Render the 3
            rows[0] +=' _ '
            rows[1] +=' _|'
            rows[2] +=' _|'
        elif numeral== '4': # Render the 4
            rows[0] +='   '
            rows[1] +='|_|'
            rows[2] +='  |'
        elif numeral== '5': # Render the 5
            rows[0] +=' _ '
            rows[1] +='|_ '
            rows[2] +=' _|'
        elif numeral== '6': # Render the 6
            rows[0] +=' _ '
            rows[1] +='|_ '
            rows[2] +='|_|'
        elif numeral== '7': # Render the 7
            rows[0] +=' _ '
            rows[1] +='  |'
            rows[2] +='  |'
        elif numeral== '8': # Render the 8
            rows[0] +=' _ '
            rows[1] +='|_|'
            rows[2] +='|_|'
        elif numeral== '9': # Render the 9
            rows[0] +=' _ '
            rows[1] +='|_|'
            rows[2] +=' _|'


        # Add a space in between numerals if this isn't the last numeral
        if i != len(number) -1:
            rows[0] +=' '
            rows[1] +=' '
            rows[2] +=' '

    return '\n'.join(rows)

my_num= getSevSegStr(53, 3)
print(my_num)

# If this program isn't being imported, display the numbers 00 to 99.





        