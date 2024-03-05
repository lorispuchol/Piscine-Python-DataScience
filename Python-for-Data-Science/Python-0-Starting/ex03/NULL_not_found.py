
def is_NaN(n):
	if n != n:
		return True
	return False
	

def NULL_not_found(object: any) -> int:
	if object == None:
		print("Nothing:", object, type(object))
		return 0
	elif is_NaN(object) == True:
		print("Cheese:", object, type(object))
		return 0
	elif (object is False):
		print("Fake:", object, type(object))
		return 0
	elif (object == 0):
		print("Zero:", object, type(object))
		return 0
	elif (object == ''):
		print("Empty:", type(object))
		return 0
	else:
		print("Type Not found")
	return 1


def main():
	Nothing = None
	Garlic = float("NaN")
	Zero = 0
	Empty = ''
	Fake = False

	NULL_not_found(Nothing)
	NULL_not_found(Garlic)
	NULL_not_found(Zero)
	NULL_not_found(Empty)
	NULL_not_found(Fake)
	print(NULL_not_found("Brian"))

if __name__ == "__main__":
	main()
