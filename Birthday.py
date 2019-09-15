from datetime import date
import sys

BIRTHDAY_MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November',
                   'December']
ZODIAC_SIGNS = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse',
                'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']

ZODIAC_DESCRIPTIONS = ['quick-witted, resourceful, versatile, and kind',
                       'diligent, dependable, strong, determined',
                       'brave, confident, and competitive',
                       'quiet, elegant, kind, and responsible',
                       'confident, intelligent, and enthusiastic',
                       'enigmatic, intelligent, and wise',
                       'animated, active, and energetic',
                       'calm, gentle, and sympathetic',
                       'sharp, smart, and curiosity',
                       'observant, hardworking, and courageous',
                       'lovely, honest, and prudent',
                       'compassionate, generous, and diligent']

bday_input = input("Please enter your birthday (mmddyyyy): ")

#make sure input is valid
if bday_input.isdigit() == False:
    print("Invalid birthday: numbers only!")
    sys.exit()

if len(bday_input) != 8:
    print("Invalid birthday: use mmddyyyy format!")
    sys.exit()

#parse input, calculate birthday variables
birthday_month = int(bday_input[0:2])
birthday_day = int(bday_input[2:4])
birthday_year = int(bday_input[4:8])

print("Okay. Your birthday is on " + BIRTHDAY_MONTHS[birthday_month - 1] + \
      " " + str(birthday_day) + ", " + str(birthday_year) + ".")

#calculate today's variables
today = date.today().strftime('%m/%d/%Y').replace("/", "")
today_month = int(today[0:2])
today_day = int(today[2:4])
today_year = int(today[4:8])

#calculate age
age = today_year - birthday_year
if (birthday_month >= today_month) and (birthday_day > today_day):
    age = age - 1

print("You are " + str(age) + " years old today.")

#happy birthday message
if (birthday_month == today_month) and (birthday_day == today_day):
    print("Happy Birthday! :-)")

zodiac_index = (birthday_year - 4) % 12
print("You were born in the year of the "  + ZODIAC_SIGNS[zodiac_index] +\
 ". According to Chinese culture, this might mean that you are " + \
 ZODIAC_DESCRIPTIONS[zodiac_index] + ".")
