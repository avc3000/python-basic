### Exception Handling ###
number_one = 5
number_two = 6
number_two = "1"

try:
    print(number_one + number_two)
    print("No error ocurred")
except:
    print("An error has occurred")

# Try exception else and finally
try:
    print(number_one + number_two)
    print("No error ocurred")
except:
    print("An error has occurred")
else:
    print("Continue the execution")  # No executed if the exception occurred
finally:
    print("The execution continue")

# Type of exceptions
try:
    print(number_one + number_two)
    print("No error ocurred")
except ValueError:
    print("An error has occurred a ValueError")
except TypeError:
    print("An error has occurred a TypeError")

# Capture the information error
try:
    print(number_one + number_two)
    print("No error has occurred")
except TypeError as error:
    print(error)
except Exception as e:
    print(e)

# Capture the information error exception
try:
    print(number_one + number_two)
    print("No error has occurred")
except Exception as ex:
    print(ex)
