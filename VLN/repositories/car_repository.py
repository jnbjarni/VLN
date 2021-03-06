from Models.Car import Car


class Car_Repository:

    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        with open("./data/cars.csv", "a+") as car_file:
            brand = car.get_brand()
            model = car.get_model()
            category = car.get_category()
            taxti = car.get_taxti()
            car_file.write("{},{},{},{} \n".format(
                brand, model, category, taxti))
        print("Car successfully added")

    #
    # def remove_car(self, car):
    #    with open("./data/cars.csv", "r+") as car_file:
    #        for line in car_file:
    #            line = line.split()

    def available_cars(self):
        with open("./data/cars.csv", "r") as car_file:
            for line in car_file:
                print(line)
