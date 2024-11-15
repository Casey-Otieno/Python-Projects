''' Countdown, by AI Swelgart al@inventwithpython.com
Show a countdown timer animation using a seven_segment display.'''

import sys, time
import Seven_Segment_Display_Module as sevseg #import seven segment dispaly module 

secondsleft= int(input('Enter countdown time in seconds>'))

try:
    while True: # Mainn program loop.
        # Clear the screen by printing several newlines
        print('\n' * 60)

        ''' Get the hours/minutes/seconds from secondsleft. For example:
       7265 is 2hours, 1 minute, 5 seconds. So 7265//3600 is 2 hours.'''

        hours= str(secondsleft // 3600)
        minutes=str((secondsleft % 3600) // 60)
        seconds= str(secondsleft % 60)

        # Get the digit strings from the seven segment display module
        hDigits= sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow= hDigits.splitlines()

        mDigits= sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow= mDigits.splitlines()

        sDigits= sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow= sDigits.splitlines()

        # Display the digits
        print(f'{hTopRow}     {mTopRow}     {sTopRow}')
        print(f'{hMiddleRow}  :  {mMiddleRow}  :  {sMiddleRow}')
        print(f'{hBottomRow}  :  {mBottomRow}  :  {sBottomRow}')

        if secondsleft == 0:
            print()
            print( '    *** BOOM ***')
            break
        
        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1) # Insert a one-second pause.
        secondsleft -= 1
except KeyboardInterrupt:
    print('Countdown,  by AI Swelgart al@inventwithpython.com ')
    sys.exit() # When Ctrl-C is passed, end the program.






