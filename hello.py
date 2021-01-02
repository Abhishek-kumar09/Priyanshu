# import only system from os
import os

# import sleep to show output for                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t❌_❌_TABLE CONTENTS_❌_❌\n") some time period
from time import sleep


# define our clear function
def clear(n):
    # for windows
    if name == 'nt':
        _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

    # print out some text


print('hello geeks\n' * 10)

# sleep for 2 seconds after printing output
sleep(2)

# now call function we defined above
clear()
