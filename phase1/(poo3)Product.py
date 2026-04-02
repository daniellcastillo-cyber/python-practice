
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self. price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity > self.stock:
            return "Not enough stock"
        else:
            self.stock -= quantity
        
    def restock(self, quantity):
        self.stock += quantity
    
    def get_info(self):
        return f"name: {self.name} | price: {self.price} | stock: {self.stock}"
    

p = Product("tomate", 2000, 50)
print(p.get_info())
p.sell(3)
print(p.get_info())
p.sell(10)
p.restock(8)
print(p.get_info())