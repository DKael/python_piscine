def NULL_not_found(object: any) -> int:
	type_names = {
		float: ["Cheese",float("NaN")],
		int: ["Zero", 0],
		str: ["Empty", ""],
		bool: ["Fake", False],
        list: ["Empty_List", []],
        tuple: ["Empty_Tuple", ()],
        set: ["Empty_Set", set()],
        dict: ["Empty_Dict", {}],
    }
	obj_class = type(object)

	if obj_class == type(None):
		print(f"Nothing: {object} {type(object)}")
	elif obj_class == float and object != object:
		print(f"Cheese: {object} {type(object)}")
	elif obj_class == str and object == '':
		print(f"Empty: {object}{type(object)}")
	elif obj_class in type_names and object == type_names[obj_class][1]:
		print(f"{type_names[obj_class][0]}: {object} {obj_class}")
	else:
		print("Type not Found")
		return 1

	return 0