ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"

ft_tuple = (ft_tuple[0], "Korea!")

ft_set = list(ft_set)
ft_set.remove("tutu!")
ft_set.append("Seoul!")
ft_set = set(ft_set)

ft_dict["Hello"] = "42Seoul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
