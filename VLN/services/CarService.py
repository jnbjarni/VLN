from repositories.car_repository import Car_Repository

class CarService:
    def __init__(self):
        self.__car_repo = Car_Repository()

    
    def add_car(self, car):
        if self.is_valid_car(car):
            self.__car_repo.add_car(car)

    def is_valid_car(self, car):

        return True
