class Car:

    def __init__(self, brand, model, category, taxti):
        self.__brand = brand
        self.__model = model
        self.__category = category
        self.__taxti = taxti


    def __str__(self):
        return "{},{},{},{}.".format(self.__brand, self.__model, self.__category, self.__taxti)

    def get_model(self):
        return self.__model

    def get_brand(self):
        return self.__brand

    def get_category(self):
        return self.__category

    def get_taxti(self):
        return self.__taxti

    