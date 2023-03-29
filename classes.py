# Classes

class EmptyPerson:
    pass


print(EmptyPerson)
print(EmptyPerson())


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


my_person = Person("Antony", "Jordan")
print(f"{my_person.name} {my_person.surname}")


class Person_Two:
    def __init__(self, name, surname, alias="No alias"):
        self.full_name = f"{name} {surname} {alias}"  # Properly public
        self.__name = name  # Property private
        self.__surname = surname  # Property private

    def get_name(self):
        return self.__name + " " + self.__surname

    def walk(self):
        print(f"{self.full_name} is walking")


my_person_two = Person_Two("Juan", "Valdez")
print(my_person_two.full_name)
my_person_two.walk()

my_other_person = Person_Two("Antony", "Jordan", "Engineer")
print(my_other_person.full_name)
print(my_other_person.get_name())
