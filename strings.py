# Strings #
my_string = "Antony"
my_other_string = "John"

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_string_new_line = "This is string\nwith new line"
print(my_string_new_line)

my_tab_string = "\tThis is string with tabulation"
print(my_tab_string)

# Format
name, surname, age = "Antony", "John", 25
print("My name is {} {} and my age is {}".format(name, surname, age))
print("My name is %s %s and my age is %i" % (name, surname, age))
print(f"My name is {name} {surname} and my age is {age}")

# Character unpacking
language = "Python"
a, b, c, d, e, f = language
print(a, b, f)

# Division
language_slice = language[1:3]
print(language_slice)
language_slice = language[1:]
print(language_slice)
language_slice = language[-1]
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)
reversed_language = language[::-2]
print(reversed_language)
reversed_language = language[1::2]
print(reversed_language)

# Functions
print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count("t"))
print(language.isnumeric())
print(language.upper().isupper())
print(language.replace("n", "N"))
print(language.startswith("Py"))
