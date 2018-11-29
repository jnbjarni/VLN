from services.CarService import CarService
from services.CustomerService import CustomerService
from Models.Car import Car
from Models.Customer import Customer


class SalesmanUI:

    def __init__(self):
        self.__car_service = CarService()
        self.__customer_service = CustomerService()

    def add_car(self):
        brand = input("Car Brand: ")
        model = input("Car Model: ")
        category = input("Car Category: ")
        taxti = input("Car rate: ")
        new_car = Car(brand, model, category, taxti)
        self.__car_service.add_car(new_car)

    def add_customer(self):
        name = input("Customer name: ")
        ssn = input("Customer snn: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        cardInfo = input("Card info: ")
        return Customer(name, ssn, phone, email, address, cardInfo)

    def main_menu(self):

        action = " "
        while(action != "q"):
            print("Main menu:")
            # Add or remove a car to database # Add and remove and edit customer functions inside here.
            print("1: Car menu")
            # Here you can get all information about bookings. (Create new order, extend order, return car, remove/unorder car)
            print("2: Customer menu")
            print("3: Bookings menu")
            print("4: Search")
            print("Press q to quit")

            action = input("Choose an option: ").lower()

            if action == "1":
                self.car_menu()

            elif action == "2":
                self.customer_menu()

            elif action == "q":
                exit()

            else:
                print("Invalid option!")

    def car_menu(self):
        action = " "
        while action != "b":
            print("Car menu: ")
            print("1: Add car")
            print("2: Remove car")
            print("3: Car history")
            print("4: Available cars")
            print("5: Unavailable cars")
            print("Enter 'b' to go back.")
            action = input("Choose an option: ").lower()

            if action == "1":
                self.add_car()

            elif action == "4":
                self.__car_service.available_cars()

            elif action == "b":
                self.main_menu()

            elif action == "q":
                exit()

    def customer_menu(self):
        action = " "
        while action != "b":
            print("Customer menu: ")
            print("1: Add customer")
            print("2: Remove customer")

            action = input("Choose an option: ")

            if action == "1":
                new_customer = self.add_customer()
                self.__customer_service.add_customer(new_customer)
            elif action == "b":
                self.main_menu()
            elif action == "q":
                exit()
