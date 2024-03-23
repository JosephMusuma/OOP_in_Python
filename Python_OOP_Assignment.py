class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, my name is {self.name} and I'm a {self.age} years old  {self.gender}.")

# Create an instance of the Person class
person1 = Person("Joseph", 23, "Male")

# Call the introduce method to display the person's information
person1.introduce()
