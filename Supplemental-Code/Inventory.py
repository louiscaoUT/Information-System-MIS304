class Inventory():

    # init
    def __init__(self, new_id, new_name, new_stock, new_price):
        
        self.__id = new_id
        self.__name = new_name
        self.__stock = new_stock
        self.__price = new_price

    def __str__(self):
        return f"{self.get_id()}\t{self.get_name():<18}\t{self.get_price():>6.2f} {self.get_stock():>12}"

    # methods
    def get_id(self):
        return self.__id    

    def get_name(self):
        return self.__name
    
    def get_stock(self):
        return self.__stock

    def get_price(self):
        return self.__price

    def restock(self, new_stock):
        if new_stock <= 0:
            self.__stock += abs(new_stock) 
            return True
            
        return False
        

    def purchase(self, purch_qty):
        if purch_qty > self.__stock:
            return False
        
        self.__stock -= purch_qty
        return True


        


