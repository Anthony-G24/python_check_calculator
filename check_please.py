#contains the cieling method to round-up floating points.

import math

def split_check(total, number_of_people):
	#error handling for <= 1 value by user
  if number_of_people <= 1:
		raise ValueError("You need more than one to split a bill")
	return math.ceil(total / number_of_people)

try:
	total_due = float(input("What is the total?  "))
	number_of_people = int(input("How many people are there?  "))
	amount_due = split_check(total_due, number_of_people)
except ValueError as err:
  #if the user inputs a string or incorrect value
	print("Sorry, that's not a valid number  ")
	print("({})".format(err))
else:
	print("Each person owes £{}.".format(amount_due))
