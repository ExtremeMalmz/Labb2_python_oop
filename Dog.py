#Eric Malmström IA 2022

class Dog:
    doglist = []

    def __init__(self,name:str, race:str, age:int, furColorList:list) -> None:
        '''
        The initializor
        '''
        self.name = name
        self.race = race
        self.age = age
        self.furColorList = furColorList
        self.sleeping = True
        Dog.doglist.append(self)

    def is_asleep(self) -> str:
        '''
        returnerar bool sleeping 
        '''
        return self.sleeping

    def wake_up(self) -> None:
        '''
        sätter sleeping till false
        '''
        self.sleeping = False

    def sleep(self) -> None:
        '''
        sätter sleeping till true
        '''
        self.sleeping = True

    def get_name(self) -> str:
        '''
        returnerar namnet på hunden
        '''
        return self.name

    def print_fur_colors(self) -> str:
        '''
        printar ut alla fur colors
        '''
        print(f"{self.name} has the following fur colors: {','.join(self.furColorList)}")
        
    def __str__(self) -> str:
        '''
        skriver ut allt 
        '''
        return f'"Woof! Im {self.name} the {self.race} ({self.age} years)."'

    


# Vår instans av klassen Dog
dog = Dog("Doug", "Pug", 8, ["black", "white", "beige"])

print(dog)
# => "Woof! I'm Doug the pug (8 years)."

# Testa gärna att köra dog.sleep() innan if-satsen
# för att se så att båda delarna ger utskrifter


if dog.is_asleep():
    dog.wake_up()
    print(dog.get_name(), "just woke up!")
    # => "Doug just woke up!"
else:
    dog.sleep()
    print(dog.get_name(), "is fast asleep!")
    # => "Doug is fast asleep!"


dog.print_fur_colors()
# => "Doug has the following fur colors: black, white, beige."

print("\nHär börjar iteration!")

Dog("Fluffy", "Pitbull", 1, ["white"])
Dog("Puddles", "Wolf", 27, ["yellow, red"])
Dog("Missy", "Rottweiler", 8, ["red", "blue", "green"])

for i in Dog.doglist:
    i.print_fur_colors()