from datetime import date
import sys

BIRTHDAY_MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November',
                   'December']

bday_input = input("Please enter your birthday (mmddyyyy): ")

#make sure input is valid
if bday_input.isdigit() == False:
    print("Invalid birthday: numbers only!")
    sys.exit()

if len(bday_input) != 8:
    print("Invalid birthday: use mmddyyyy format!")
    sys.exit()

#parse input
birthday_month = int(bday_input[0:2])
birthday_day = int(bday_input[2:4])
birthday_year = int(bday_input[4:8])

print("Okay. Your birthday is on " + BIRTHDAY_MONTHS[birthday_month - 1] + \
      " " + str(birthday_day) + ", " + str(birthday_year))
