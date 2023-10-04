class Animal:
    name = ''
    number_of_legs = 4
    color = '',

    # Constructor - Used to create an object from a class
    def __init__(self, name_, color_, number_of_legs_=4):
        self.name = name_
        self.color = color_
        self.number_of_legs = number_of_legs_

    def navigate(self):
        # print(f'{self.name} navigates with its {self.number_of_legs}')
        print(self.name + ' navigates with its ' + str(self.number_of_legs) + ' legs')


cat1 = Animal('kitty', 'black')

class Dog(Animal):
    breed = ''

    def __init__(self, breed, name, color, number_of_legs=4):
        Animal.__init__(self, name, color, number_of_legs)
        self.breed = breed

    def navigate(self):
        print("I am a dog named " + self.name + ". And I run fast")


dog2 = Dog(breed="German Sheperd", name="Jimmy", color="Black")
dog2.navigate()
