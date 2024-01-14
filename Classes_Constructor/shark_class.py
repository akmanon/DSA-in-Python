class Shark:
    animal = "fish"
    place = "ocean"

    def __init__(self, name, food, age=1):
        self.name = name
        self.age = age
        self.food = food

    def swim(self):
        print(self.name + " is swimming in" + self.animal)

    def eat(self):
        print(self.name + " is eating : " + self.food)

def main():
    dextor = Shark("Dextor", "guppy", 12)
    dextor.swim()
    dextor.eat()

if __name__ == "__main__" :
    main()  