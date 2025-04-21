class car:
    def __init__(self):
        print("object of car is created")
    def car_colour(self,colour):
        self.colour=colour
        print(f"my car colour is {colour}")
audi=car()
audi.car_colour("white")

