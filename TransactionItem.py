class TransactionItem:

    # attributes
    def __init__(self):
        pass

    def __str__(self):
        return f"{self.__id}\t{self.__name:<13}\t\t{ self.__quantity:<1}\t {'$' + self.get_price():<8}\t\t{'$' + self.calc_cost():2}"

    
    # methods

    def set_id(self, new_id):
        self.__id = new_id

    def set_name(self, new_name):
        self.__name = new_name

    def set_qty(self, new_qty):
        self.__quantity = new_qty

    def set_price(self, new_price):
        self.__price = new_price


    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_qty(self):
        return self.__quantity

    def get_price(self):
        return format(self.__price, '.2f')


    def calc_cost(self):
        return format(self.__quantity * self.__price, '.2f')


    