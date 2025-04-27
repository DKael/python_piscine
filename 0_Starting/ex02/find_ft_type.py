def all_thing_is_obj(object: any) -> int:
	# print(f"{object} : {type(object)}")
	# print(f"{object} : {object.__class__}")

	type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
    }
	obj_class = type(object)

	if obj_class == str:
		print(f"{object} is in the kitchen : {obj_class}")
	elif obj_class in type_names:
		print(f"{type_names[obj_class]} : {obj_class}")
	else:
		print("Type not found")
	return 42