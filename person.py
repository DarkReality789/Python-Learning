# #2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age as of year 2023 - 12 - 31.
# create an object of person class and print his age

class Person:
    name = ""
    country = ""
    DoY = ""

    def __init__(self, name, country, DoY):
        self.name = name
        self.country = country
        self.DoY = DoY

    def determine_age(self):
        new_age = 2023 - self.DoY
        return new_age


new_person = Person("Harshayan", "England", 2006)
print("Your age in 2023 is " + str(new_person.determine_age()))
