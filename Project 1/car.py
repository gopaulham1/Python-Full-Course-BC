class Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")