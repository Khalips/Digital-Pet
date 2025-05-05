class Pet:
    def __init__(self):
        self.name = "Spike"
        self.hunger = 10              # Scale of 0 to 10
        self.energy = 0               # Scale of 0 to 10
        self.happiness = 0            # Scale of 0 to 10
        self.tricks = []              # List to store learned tricks

    # Method to feed the pet
    # Should reduce hunger by 3 points 
    # Should increase happiness by 1
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    # Method to make the pet go to sleep. 
    # Should increase the energy of the pet by 5
    def sleep(self):
        self.energy = min(10, self.energy + 5)

    # Method to make the pet play
    # Should decrease the energy by 2
    # Should increase happiness by 2
    # Should increase hunger by 1
    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    # Method to teach the pet some new tricks
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
        else:
            print(f"{self.name} already knows {trick}!")

    # Method to list all the pet's tricks
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet!")

    # Method to display the current state of the pet. 
    # This includes hunger, energy and happiness
    def get_status(self):
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        self.show_tricks()

#Main program
def main():
    # Create a new pet
    my_pet = Pet()

    # Check initial status
    print(f"{my_pet.name}'s Status")
    my_pet.get_status()

    # Feed the pet
    print(f"\n{my_pet.name} had something to eat")
    my_pet.eat()
    print(f"{my_pet.name}'s Status")
    my_pet.get_status()

    # Make the pet sleep
    print(f"\n{my_pet.name} went to sleep")
    my_pet.sleep()
    print(f"{my_pet.name}'s Status")
    my_pet.get_status()

    # Play with the pet
    print(f"\n{my_pet.name} enjoyed playtime")
    my_pet.play()
    print(f"{my_pet.name}'s Status")
    my_pet.get_status()

    # Teach tricks
    print(f"\n{my_pet.name} Learned new tricks")
    my_pet.train("sit")
    my_pet.train("roll over")
    my_pet.train("fetch")
    my_pet.show_tricks()

    # Play again
    print(f"\n{my_pet.name} enjoyed playtime")
    my_pet.play()
    print(f"{my_pet.name}'s Status")
    my_pet.get_status()


# Run the main program
if __name__ == "__main__":
    main()