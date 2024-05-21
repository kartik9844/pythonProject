class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(self.brand,self.model,self.year)
    def start(self):
        print("Engine started")

car1 = car("Toyota","Camry",2020)
car2 = car("Honda", "Civic", 2018)

car1.display()
car2.display()

car1.start()
car2.start()