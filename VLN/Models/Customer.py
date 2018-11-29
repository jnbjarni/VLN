class Customer(object):

    def __init__(self, name, ssn, phone, email, address, card):
        self.__name = name
        self.__ssn = ssn
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__card = card

    def get_name(self):
        return self.__name

    def get_ssn(self):
        return self.__ssn

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def get_card(self):
        return self.__card
