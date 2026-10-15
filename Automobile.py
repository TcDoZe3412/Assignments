
class Automobile:
    def __init__(self, brand, color, wheels):
        self.brand = brand
        self.color = color
        self.wheels = wheels

    def show_details(self):
        print("Brand:", self.brand)
        print("Color:", self.color)
        print("Number of wheels:", self.wheels)

    def move(self):
        print("The automobile is moving.")


class Bike(Automobile):
    def __init__(self, brand, color):
        super().__init__(brand, color, 2)

    def start_engine(self):
        print("The bike engine has started.")


class Cycle(Automobile):
    def __init__(self, brand, color):
        super().__init__(brand, color, 2)

    def pedal(self):
        print("The cycle is moving by pedalling.")


bike1 = Bike("Honda", "Black")
cycle1 = Cycle("Hero", "Blue")

print("--- Bike Details ---")
bike1.show_details()
bike1.start_engine()
bike1.move()

print("\n--- Cycle Details ---")
cycle1.show_details()
cycle1.pedal()
cycle1.move()
