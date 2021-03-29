# Odd or even
print("Odd or Even 'Calculator' \n")

# Welcome a user then ask her/him for a number between 1 and 1000. 
# When the user gives you the number, you check if it's odd or even and then you print a message letting her/him know.

# Calculator
def OddOrEven(num):
	# If the number chosen is divisible by 2, then it is Even. Return the value.
	if num % 2 == 0: return "even"
	# If it's not, it is Odd. Return the value.
	else: return "odd"

# Ask the user a number necessarily between 1 and 1000.
num = float(input("Hello! Please tell me a number between 1 and 1000. Press 0 to finish the program."))

# While you don't want to finish the programme and you are inputting correct values...
while num != 0:
	# Ask if the number the user have choosen is inside [1,1000].
	if num >= 1 and num <= 1000 and num != 0:
		# Check if it is inside the parameters using Calculator.
		res = OddOrEven(num)
		# Show to the user if the number (s)he has chosen is Odd or Even.
		print("(%d) is an %s number! \n" %(num,res))
		# Ask it again. (It's another round!)
		num = float(input("Tell me a number between 1 and 1000. Press 0 to finish the program."))
  
	# But if you miss it...
	else:
		# It tells you must enter a valid value.
		print("You must enter a number between 1 and 1000. \n")
		# You'll be asked again.
		num = float(input("Tell me a number between 1 and 1000. Press 0 to finish the program."))

# And then you decided you want to finish the programme.
else:
	# It shows you a message!
	print("Bye bye!")
