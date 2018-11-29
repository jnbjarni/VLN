from Models.Customer import Customer


class Customer_Repository():
    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        with open("./data/customers.csv", "a+") as customer_file:
            name = customer.get_name()
            ssn = customer.get_ssn()
            email = customer.get_email()
            address = customer.get_address()
            phone = customer.get_phone()
            cardInfo = customer.get_card()
            customer_file.write("{},{},{},{},{},{} \n".format(
                name, ssn, email, address, phone, cardInfo))
        print("Customer successfully added")

    def remove_customer(self, customer_ssn):
        pass
