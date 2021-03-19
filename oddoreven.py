print("Odd or Even 'Calculator'")
def OddOrEven(num):
	if num % 2 == 0:
		return "even"
	else:
		return "odd"
num = float(input("Please tell me a number between 1 and 1000: "))
res = OddOrEven(num)
print("The number you provided (%d) is %s." %(num,res))
