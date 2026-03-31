



def get_inventory_report(inventary):
    available = []
    out_of_stock = []
    total_value = 0
    for product in inventary:
        
        if product is None:
            return False
        elif product['stock'] <= 0:
            out_of_stock.append(product['product'])
        else:
            available.append(product['product'])
        
        total_value += product["price"] * product['stock']
    
    return {

    
    "available": available,
    "out_of_stock": out_of_stock,
    "total_value": total_value
    }
inventory = [
    {"product": "laptop", "price": 1200, "stock": 5},
    {"product": "mouse", "price": 25, "stock": 0},
    {"product": "keyboard", "price":75, "stock": 12},
    {"product": "monitor", "price":400, "stock": 3},
    {"product": "headphone", "price": 80, "stock": 0},

]
result = get_inventory_report(inventory)
print(get_inventory_report(inventory), '\n')
print(f"Total value: {result['total_value']}\n")
print(f"available: {result['available']}\n")
print(f"out_of_stock: {result['out_of_stock']}\n")