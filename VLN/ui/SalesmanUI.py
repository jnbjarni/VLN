from services.CarService import CarService
from Models.Car import Car

class SalesmanUI:

    def __init__(self):
        self.__car_service = CarService()

    def main_menu(self):

        action = " "
        while(action != "q"):
            print("Possible to do the following:")
            print("1: Add a car")
            print("Press q to quit")

            action = input("Choose an option: ").lower()

            if(action == "1"):
                brand = input("Car Brand: ")
                model = input("Car Model: ")
                category = input("Car Category: ")
                taxti = input("Car rate: ")
                new_car = Car(brand,model,category, taxti)
                self.__car_service.add_car(new_car)

