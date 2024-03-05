import sys

if len(sys.argv) <= 1:
	exit()

try:
	if len(sys.argv) > 2:
		raise AssertionError("AssertionError: more than one argument is provided") 
	try:
		nb = int(sys.argv[1])
		if (nb % 2) == 0:
			print("I'm Even")
		else:
			print("I'm Odd")
	except ValueError:
		raise AssertionError("AssertionError: argument is not an integer")

except AssertionError as err:
	print(err)