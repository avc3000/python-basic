# Tuples -> The tuple is not mutable
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (30, 1.75, "Antony", "Villa")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple.count(30))
print(my_tuple.index("Antony"))

my_other_tuple = (10, 20, 30, 40, 50)
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:7])

my_tuple = list(my_sum_tuple)
print(type(my_tuple))

my_tuple[4] = "Antony Jordan"
my_tuple.insert(0, "Red")
print(my_tuple)

my_tuple = tuple(my_tuple)
print(type(my_tuple))
