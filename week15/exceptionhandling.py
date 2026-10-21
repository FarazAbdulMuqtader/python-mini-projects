#Exceptions
class InventoryError(Exception):
    pass
class OutOfStockError(InventoryError):
    def __init__(self,name,availablity):
        self.name=name
        self.availablity=availablity
        super().__init__(f"{name} is out of stock. Available quantity: {availablity}")

class ItemNotFoundError(InventoryError):
    def __init__(self,name):
        self.name=name
        super().__init__(f"{name} not found in inventory.")


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.items[name]=self.items.get(name,0)+quantity

    def remove_item(self, name, quantity):
        if name not in self.items:
            raise ItemNotFoundError(name)
        if self.items[name] < quantity:
            raise OutOfStockError(name, self.items[name])
        self.items[name] -= quantity


inv=Inventory()
inv.add_item("pen",5)

try:
    inv.remove_item("pen",10)
except InventoryError as e:
    print("Inventrory problem: ",e)

try:
    inv.remove_item("Book",1)
except InventoryError as e:
    print("Inventory prob: ",e)   

try:
    inv.remove_item("pen",10)
except OutOfStockError as e:
    print(f"Only. {e.availablity} of {e.name} left")
except ItemNotFoundError as e:
    print(f"we dont sell {e.name}")
except InventoryError as e:
    print("Other inventory error: ",e)

try:
    inv.add_item("pen",-3)
except ValueError as e:
    print("Bad Quantitiy: ",e) 
