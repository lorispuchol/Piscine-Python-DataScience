def all_thing_is_obj(object: any) -> int:
	type_bank = {
		list : "List",
		set : "Set",
		dict : "Dict",
		tuple : "Tuple",
	}
	if type(object) == str:
		print (object, "is in the kitchen :", type(object))
	elif (type(object) in type_bank):
		print(type_bank.get(type(object)), ":", type(object))
	else:
		print(type_bank.get(type(object), "Type not found"))
	return 42

def main():
	ft_list = ["Hello", "tata!"]
	ft_tuple = ("Hello", "toto!")
	ft_set = {"Hello", "tutu!"}
	ft_dict = {"Hello" : "titi!"}

	all_thing_is_obj(ft_list)
	all_thing_is_obj(ft_tuple)
	all_thing_is_obj(ft_set)
	all_thing_is_obj(ft_dict)
	all_thing_is_obj("Brian")
	print(all_thing_is_obj(10))

if __name__ == "__main__":
	main()