'''
                                        Title: Animal Sounds



Create a simple program that represents different animals and their sounds. 
Follow the steps below to complete the assignment:

Step 1: Create a base class Animal with a method make_sound(). 
This method should print a generic animal sound.
Step 2: Create two subclasses Dog and Cat, each inheriting from the Animal class.
Step 3: Override the make_sound() method in the Dog and Cat classes with their respective sounds (bark and meow).
Step 4: Implement a function called animal_sound_in_zoo() that takes an animal object as a parameter and
calls its make_sound() method.
Step 5: Create instances of Dog and Cat classes and 
call the animal_sound_in_zoo() function with these instances as arguments to observe their unique sounds.    Hints:
You can use the print() function to display the output.

Remember to use the super() function inside the make_sound() method of the
derived classes to call the base class's make_sound() method.

Your Answer:
# Step 1: Create a base class Animal with a method make_sound(). 
# This method should print a generic animal sound.
'''


class Animal:
    def make_sound(self):
        print("Generic animal sound")

# Step 2: Create two subclasses Dog and Cat, each inheriting from the Animal class.
class Dog(Animal):
    # Step 3: Override the make_sound() method in the Dog class with its respective sound (bark).
    def make_sound(self):
        super().make_sound()  # Call the base class's make_sound() method using super()
        print("Bark! Bark!")

class Cat(Animal):
    # Step 3: Override the make_sound() method in the Cat class with its respective sound (meow).
    def make_sound(self):
        super().make_sound()  # Call the base class's make_sound() method using super()
        print("Meow!")

# Step 4: Implement a function called animal_sound_in_zoo() that takes an animal object as a parameter and calls its make_sound() method.
def animal_sound_in_zoo(animal):
    animal.make_sound()

# Step 5: Create instances of Dog and Cat classes and call the animal_sound_in_zoo() function with these instances as arguments to observe their unique sounds.
if __name__ == "__main__":
    dog_instance = Dog()
    cat_instance = Cat()

    print("Dog in the zoo:")
    animal_sound_in_zoo(dog_instance)

    print("\nCat in the zoo:")
    animal_sound_in_zoo(cat_instance)
