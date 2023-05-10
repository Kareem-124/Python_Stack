class Store:
    def __init__(self, name):
        self.name = name
        self.list_of_products = []

    def add_product(self, new_product):
        self.list_of_products.append(new_product)
        return self

    def sell_product(self, id):
        self.list_of_products.pop(id)
        return self

    def inflation(self, percent_increase):
        for i in self.list_of_products:
            i.price += (i.price * percent_increase)
        return self

    def store_products_info(self):
        for i in self.list_of_products:
            i.print_info()

    def set_clearance(self, category, percent_discount):
        for i in self.list_of_products:
            if i.category == category:
                i.price -= (i.price * percent_discount)
        return self


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price*percent_change)
            return self

    def print_info(self):
        print(
            f"\nName:{self.name} \nCategory: {self.category} \nPrice: {self.price}")
        return self


bravo = Store("Bravo")
cola = Product("Cola", 5, "Drinks")
kinder = Product("Kinder", 3, "Chocolate")
arwa = Product("Arwa", 10, "Drinks")

bravo.add_product(cola).add_product(kinder).add_product(arwa).inflation(0.5)
cola.update_price(0.5, True)
bravo.set_clearance("Drinks",0.50).store_products_info()
