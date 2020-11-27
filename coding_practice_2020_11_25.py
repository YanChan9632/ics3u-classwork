#QUESTION 34
number = int(input("Enter an integer: "))

if(number % 2 == 0):
    print("It is an even number")
else:
    print("It is an odd number")

#QQUESTION 36
letter = input("Enter a letter: ")

if letter in ["a", "e", "i", "o", "u"]:
    print("The letter you have entered is a vowel.")
elif letter == "y":
    print("Y can sometimes be a value amd sometimes a consonant.")
else:
    print("The letter is as consonant.")    

#QUESTION 37
shape = int(input("Number of sides: "))

while shape >= 3 or shape <= 10:
    if shape == 3:
        print("The shape is a triangle")
        break
    elif shape == 4: 
        print("The shape is a quadrilateral")
        break
    elif shape == 5:
        print("The shape is a pentagon")
        break
    elif shape == 6:
        print("The shape is a hexagon")
        break
    elif shape == 7:
        print("The shape is a heptagon")
        break
    elif shape == 8:
        print("The shape is an octogon")
        break
    elif shape == 9:
        print("The shape is a nonagon")
        break
    elif shape == 10:
        print("The shape is a decagon")
        break
    else:
        print("The number you have inputted is invalid.")
        break

#QUESTION 38
month = input("Enter a month: ")

if month in ["September", "April", "June", "November"]:
    print("There are 30 days in this month.")
elif month == "February":
    print("There can be 28 or 29 days in this month.")
else:
    print("There are 31 days in this month.")

#QUESTION 40
Side_A = int(input("Length of the first side: "))
Side_B = int(input("Length of the second side: "))
Side_C = int(input("Length of the third side: "))

if Side_A == Side_B == Side_C:
    print("It is an equilateral triangle.")
elif Side_A == Side_B:
    print("It is an isosceles triangle.")
elif Side_A == Side_C:
    print("It is an isosceles triangle.")
elif Side_B == Side_C:
    print("It is an isosceles triangle.")
else:
    print("It is a scalene triangle")

#QUESTION 43
bill = int(input("What is the denomination of the banknote: "))
while bill in [1, 2, 5, 10, 20, 50, 100]:
    if bill == 1:
        print("George Washington is on the Banknote.")
        break
    elif bill == 2: 
        print("Thomas Jefferson is on the Banknote.")
        break
    elif bill == 5:
        print("Abraham Lincoln is on the Banknote.")
        break
    elif bill == 10:
        print("Alexander Hamilton is on the Banknote.")
        break
    elif bill == 20:
        print("Andrew Jackson is on the Banknote.")
        break
    elif bill == 50:
        print("Ulysses S. Grant is on the Banknote.")
        break
    elif bill == 100:
        print("Benjamin Franklin is on the Banknote.")
        break
else:
    print("There is no such Banknote.")

#QUESTION 46
month = input("What is the month: ")
day = int(input("What is the date: "))

if month == "January" or "February":
    print("It is winter")       
elif month == "March":
    if day < 20:
        print("It is winter")
    else:
        print("It is spring")
elif month == "April" or "May":
    print("It is spring")
elif month == "June":
    if day < 21:
        print("It is spring")
    else:
        print("It is summer")
elif month == "July" or "August:
    print("It is summer")
elif month == "September":
    if day < 22:
        print("It is summer")
    else:
        print("It is fall")
elif month == "October" or "November":
    print("It is fall")
elif month == "December":
    if day < 21:
        print("It is fall")
    else:
        print("It is winter")

#QUESTION 47
month = input("What is the month: ")
day = int(input("What is the day: "))

if month == "January":
    if day < 20:
        print("You are a Capricorn")
    else:
        print("You are an Aquarius")
elif month == "February":
    if day < 19:
        print("You are an Aquarius")
    else:
        print("You are a Pisces")
elif month == "March":
    if day < 21:
        print("You are a Pisces")
    else:
        print("You are an Aries")
elif month == "April":
    if day < 20:
        print("You are an Aries")
    else:
        print("You are a Taurus")
elif month == "May":
    if day < 21:
        print("You are a Taurus")
    else:
        print("You are a Gemini")
elif month == "June":
    if day < 21:
        print("You are a Gemini")
    else:
        print("You are a Cancer")
elif month == "July":
    if day < 23:
        print("You are a Cancer")
    else:
        print("You are a Leo")
elif month == "August":
    if day < 23:
        print("You are a Leo")
    else:
        print("You are a Virgo")
elif month == "September":
    if day < 23:
        print("You are a Virgo")
    else:
        print("You are a Libra")
elif month == "October":
    if day < 23:
        print("You are a Libra")
    else:
        print("You are a Scorpio")
elif month == "November":
    if day < 23:
        print("You are a Scorpio")
    else:
        print("You are a Sagittarius")
elif month == "December":
    if day < 22:
        print("You are a Sagittarius")
    else:
        print("You are a Capricorn")

#QUESTION 48
year = int(input("What year is it: "))

if year % 12 == 0:
    print("It is the year of the Monkey.")
elif year % 12 == 1:
    print("It is the year of the Rooster.")
elif year % 12 == 2:
    print("It is the year of the Dog.")
elif year % 12 == 3:
    print("It is the year of the Pig.")
elif year % 12 == 4:
    print("It is the year of the Rat.")
elif year % 12 == 5:
    print("It is the year of the Ox.")
elif year % 12 == 6:
    print("It is the year of the Tiger.")
elif year % 12 == 7:
    print("It is the year of the Hare.")
elif year % 12 == 8:
    print("It is the year of the Dragon.")
elif year % 12 == 9:
    print("It is the year of the Snake.")
elif year % 12 == 10:
    print("It is the year of the Horse.")
else:
    print("It is the year of the Sheep.")

#QUESTION 49
scale = float(input("What was the magnitude of the earthquake: "))

if scale < 2:
    print("It is a micro earthquake.")
elif 2 <= scale < 3:
    print("It is a very minor earthquake.")
elif 3 <= scale < 4:
    print("It is a minor earthquake.")
elif 4 <= scale < 5:
    print("It is a light earthquake.")
elif 5 <= scale < 6:
    print("It is a moderate earthquake.")
elif 6 <= scale < 7:
    print("It is a strong earthquake.")
elif 7 <= scale < 8:
    print("It is a major earthqyake.")
elif 8 <= scale < 10:
    print("It is a great earthquake")
else:
    print("It is a meteoric earthquake.")


#STRING 1 - CODINGBAT

#HELLO_NAME
def hello_name(name):
  return "Hello " + name  + "!"
  
#MAKE_ABBA
def make_abba(a, b):
  return a + b + b + a

#MAKE_TAGS
def make_tags(tag, word):
  html = "<{}>{}</{}>".format(tag, word, tag)
  return html

#MAKE_OUT_WORDS
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#FIRST_TWO
def first_two(str):
  if len(str) <= 2:
    return str
  return str[:2]

#FIRST_HALF
def first_half(str):
  return str[:len(str)/2]
  
#WITHOUT_END
def without_end(str):
  return str[1:-1]

#COMBO_STRING
def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  return a + b + a

#NON_START
def non_start(a, b):
  return a[1:] + b[1:]

#LEFT2
def left2(str):
  return str[2:] + str[:2]
