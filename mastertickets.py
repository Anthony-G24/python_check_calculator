# Ticket system that shows number of tickets remaining, how much total order value is and decrements num of tickets remaining once user confirms choice.
# Uses functions, while loop, error handling and if statement


TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100  



def calculate_price(number_of_tickets):
	return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
	print("There are {} tickets remaining.".format(tickets_remaining))
	name = input("Hello! What's your name?  ")
	number_of_tickets = (input("How many tickets would you like, {}?  ".format(name)))
	try:
		number_of_tickets = int(number_of_tickets)
		if number_of_tickets > tickets_remaining:
			raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
	except ValueError as err:
		print("Sorry we ran into an issue. {}. Please try again.".format(err))
	else:
		total_price = calculate_price(number_of_tickets)
		print("Your total comes to ${}".format(total_price))
		decision = input("Do you want to proceed? Y/N  ")
		if decision.lower() == "y":
			print("SOLD!")
			tickets_remaining -= number_of_tickets
		else:
			print("Thanks {}, for your interest in our tickets, see you soon".format(name))

print("Im sorry {}, the tickets are sold out".format(name))	
