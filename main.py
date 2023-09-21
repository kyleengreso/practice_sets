class HouseholdAppliances:
    def __init__(self, name:str, power:float, usage_hours:int):
        self.name = name
        self.power = power
        self.usage_hours = usage_hours

    def time_usage_per_day(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power} kW")
        print(f"Usage Hours per Day: {self.usage_hours} hours")

    def power_consumption(self):
        print(f"Total Power Consumption per Day: {self.power * self.usage_hours} kWh")

class Animals:
    def __init__(self, name:str, species:str, owner:str):
        self.name = name
        self.species = species
        self.owner = owner

    def owner_name(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Owner: {self.owner}")

    def call_pet(self):
        print(f"Call {self.name}!")

class Products:
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def product_price(self):
        print(f"Product Name: {self.name}")
        print(f"Price: Php{self.price}")
    
    def product_quantity(self):
        print(f"Quantity: {self.quantity}")

def main():
    print("HOUSEHOLD APPLIANCES!!!")
    print('FIRST APPLIANCES')
    washing_machine = HouseholdAppliances('Washing Machine', 0.5, 4)
    washing_machine.time_usage_per_day()
    washing_machine.power_consumption()

    print('SECOND APPLIANCES')
    laptop = HouseholdAppliances('Laptop', 0.135, 6)
    laptop.time_usage_per_day()
    laptop.power_consumption()
    print()

    print("ANIMALS!!!")
    print('FIRST ANIMAL')
    tiger = Animals('Yabar', 'Cat', 'Ken Roger')
    tiger.owner_name()
    tiger.call_pet()

    print('SECOND ANIMAL')
    monkey = Animals('Ken', 'Primate', "Cutie")
    monkey.owner_name()
    monkey.call_pet()
    print()

    print("PRODUCTS!!!")
    print('FIRST PRODUCT')
    alcohol = Products("Alcohol", 100, 5)
    alcohol.product_price()
    alcohol.product_quantity()

    print('SECOND PRODUCT')
    bag = Products('Gucci', 250000, 1)
    bag.product_price()
    bag.product_quantity()
    print()

if __name__ == "__main__":
    main()

    
