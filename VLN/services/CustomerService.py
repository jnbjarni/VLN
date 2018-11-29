from repositories.customer_repository import Customer_Repository
import string


class CustomerService:
    def __init__(self):
        self.__customer_repo = Customer_Repository()

    def add_customer(self, new_customer):
        if self.is_valid_ssn(new_customer.get_ssn()):
            self.__customer_repo.add_customer(new_customer)
        else:
            print("Invalid ssn!")

    def is_valid_ssn(self, ssn):
        for i, char in enumerate(ssn):
            if char.isdigit() != True:
                return False

        if len(ssn) != 10:
            return False
        else:
            return True
