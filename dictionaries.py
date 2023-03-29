# Dictionaries
my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Name": "Antony", "Surname": "John", "Age": 30, 1: "Python"}
my_dict = {"Name": "Antony", "Surname": "John",
           "Age": 30, "Languages": {"Python", "C#", "Java"}, 1: 1.75}
print(my_other_dict)
print(my_dict)
print(len(my_other_dict))
print(len(my_dict))
print(my_dict["Name"])

my_dict["Name"] = "Pedro"
print(my_dict["Name"])
print(my_dict[1])

del my_dict["Age"]
print(my_dict)

print("Antony" in my_dict)
print("Languages" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = my_other_dict.fromkeys(("Name", 1))
print(my_new_dict)

my_list = ["Name", 1, "Description"]
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ["Antony", "Jordan"])
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
print(my_other_dict.popitem())
print(my_other_dict.get("Name"))

my_other_dict.clear()
print(my_other_dict)
