TICKET_PRICE = 10

tickets_remaining = 100  

# Run code until we run out of tickets

while tickets_remaining >= 1:
	
	# Output how many tickets are remaining using the tickets_remaining variable
	print("There are {} tickets remaining.".format(tickets_remaining))
	
	# Gather the user's name and assign it to a new variable
	name = input("Hello! What's your name?  ")
	
	# Prompt the user by name and ask how many tickets they would like
	number_of_tickets = int(input("How many tickets would you like, {}?  ".format(name)))

	# Calculate the price (number of tickets mulitplied by price) assign to variable
	total_price = number_of_tickets * TICKET_PRICE
	# Output price to the screen
	
	#tickets_remaining >= number_of_tickets
	print("Your total comes to ${}".format(total_price))
	#else :
		#break					
	# Prompt user if they want to proceed Y/N?
	decision = input("Do you want to proceed? Y/N  ")

	#If they want to proceed
	if decision.lower() == "y":
		# print out sold to confirm
		print("SOLD!")
		# and them decrement the tickets remaining by the number of tickets purchased
		tickets_remaining -= number_of_tickets
	
	# Otherwise...
	else:
		#Thank them by name
		print("Thanks {}, for your interest in our tickets, see you soon".format(name))

# Notify the users the tickets are sold out
print("Im sorry {}, the tickets are sold out".format(name))	
