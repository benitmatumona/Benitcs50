# Problem sets from the CS50 course in python all in one repository 

These are project from CS50 course starting from the basics (like a simple program 
that prompts the user from and input returns it all in lowercaes) to an advance 
level (like dealing with unit test, JASON, and APIs).

## Indoor Voice
This is a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should will be outputted unchanged
## Playback Speed
This is a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... this is in order to give an effect of slowing down the speech.
## Making Faces
This is a function that accepts a str as input and returns that same input with any :) converted to 🙂 and any :( converted to 🙁 . All other text will be returned unchanged.
## Einstein 
This is a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assuming that the user will input an integer.
## Tip Calculator 
This file will have two functions (apart from the main function). listed below 
The first one is called dollars_to_float, which accepts a str as input (e.g $120.00), remove the leading $, and return the amount as a float( e.g from $120.00 to 120.00). 
The second one is percent_to_float, which should accept a str as input (e.g 70%), remove the trailing %, and return the percentage as a float(e.g from 70% to 70.00.

## Deep Thought 
This is a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. If none of the previous options are tyed it outputs No.

## Home Federal Savings Bank
This is a program that prompts the user for a greeting. If the greeting starts with “hello” the output is $0. If the greeting starts with an “h” (but not “hello”) the output is $20. Otherwise the output is $100. It will ignore any leading whitespace in the user’s greeting and it will treat the user’s greeting case-insensitively.

## File Extensions
This is a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends (case-insensitively) in any of these suffixes: jpg, jpeg, gif, jng, text, pdf and zip. If the file name doesn't end wih any of the above it will output application/octet-stream.

## Math Interpreter

This is a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point rounded off to one decimal place. This program assumes that the user’s input will be formatted as x y z with one space between characters(e.e 1 + 4 / 3) and it also assumes that the denominator is not equals to zero.

## Meal Time 
This is a program that prompts the user for a time(weather it's 24 hour format e.g 17:00, or 12 hour format e.g 9:00 a.m. or 9:00 p.m.) outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, it won't output anything at all. Each meal’s time range is inclusive.The program assumes the the user will enter valid input according to the examples in the brackets above.

## Camel Case
This is a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case(e.g from "camelCase" to "camel_case". This program assume that the user’s input will indeed be in camel case.

## Coke Machine 
This is a program that prompts the user to insert a coin, into a machine that sells coke do 50 cents. The machine only accept 5, 10 and 25 cents. Each time the user inserts a coin it informs the user of the amount due. Once the user has inputted at least 50 cents it will output how many cents in change the user is owed. This program assumes that the user will only input integers and ignores any integer that isn’t an accepted

## Just Setting Up My TWTTR.

This is a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase. this program mimics Twitter shortcut by removing vowels for works (e.g from "How are you doing" to "Hw r y dng").

## Vanity Plates

This is a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.(the requirements are listed below)

1. All vanity plates must start with at least two letters.
2. vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
3. Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
4. The first number used cannot be a ‘0’.
5. No periods, spaces, or punctuation marks are allowed.

## Nutrition Facts 
This is a program that prompts consumers to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits

## Fuel Gauge 
This is a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, outputs E instead to indicate that the tank is essentially empty. And if 99% or more remains, outputs F instead to indicate that the tank is essentially full.

## Felipe's Taqueria 
This is a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, it will display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. It treats the user’s input case insensitively. This program ignores any input that isn’t an item, it also assumes that every item on the menu will be titlecased.

## Outdated 
This is a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like "9/8/1636" or "September 8, 1636" then outputs that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, it will prompt the user again. This program assume that every month has 31 days.

## Grocery list
This is a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then outputs the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. It treats the user’s input case-insensitively.

## Emojize
This is a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji, for instance ":thumbs_up:" which will be automatically converted to 👍.

## Figlet
This is a program that: takes in a strig then deplayes large text in the desired font

This program expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.

If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program will exit via sys.exit with an error message.

## Adieu, Adieu
This is a program that prompts the user for names, one per line, until the user inputs control-d. It assumes that the user will input at least one name. Then bids adieu to those names, separating two names with one and, three names with two commas and one and, and names with commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

## Guessing Game 
This is a program that:

Prompts the user for a level, 
If the user does not input a positive integer, the program will prompt again.
The program randomly generates an integer between 1 and 
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program will prompt the user again. 
If the guess is smaller than that integer, the program will output Too small! and prompt the user again.
If the guess is larger than that integer, the program will output Too large! and prompt the user again.
If the guess is the same as that integer, the program will output Just right! and exit.

## Little Professor 
This is program that:

Prompts the user for a level, 
If the user does not input 1, 2, or 3, the program will prompt again.

Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. 

## Bitcoin Price Index
This is a program that expects the user to specify as a command-line argument the number of Bitcoins, that they would like to buy. This program uses an API call to get the current price in dollars 

If that argument cannot be converted to a float, the program will exit via sys.exit with an error message.

## Testing My Twttr
This is a program that tests my Twttr program using a group of test functions but with the function renamed as "shorten".

## Back To The Bank
This is a program that uese a group of test_functions to test my Bank program but with the function renamed as "Value".

## Re-requesting My Vanity Plates
This is a program that uses pytest to test my Vanity Plates program.

## Refueling 
This is a program that uses a group of test_functions to test my Fuel program.

## Lines Of Code
a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. 

If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program will instead exit via sys.exit.

## Pizza.py
This is a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI and will format the table using the library’s grid format. 
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program will exit via sys.exit.

## Scourgify
This is a program that opens a file and rearranges the order from surname and name to name and surname 

This program expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. This program assumes that each student will have both a first name and last name.

## CS50 P-Shirt
This is a program that overlays a picture of a cs50 t-shirt on a picture of any person so that is looks like a person is wearing it.
This program that expects exactly two command-line arguments in addition to the name of the program the first one will be the name (or path) of a JPEG or PNG to read (i.e., open) as input and the second will be the name (or path) of a JPEG or PNG to write (i.e., save) as output

## more information 
this readme file will be updated to cater for many other projects that exists in this repository that have not been mentioned.
