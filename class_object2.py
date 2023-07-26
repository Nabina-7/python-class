class Fruits():
    greet=("welcome to the shop")
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def shopping(self):
        print(f"{self.greet},item name:{self.item},price:{self.price}")

apple_object= Fruits("apple",450)
mango_object= Fruits("mango",100)
orange_object= Fruits("orange",350)
avocado_object= Fruits("avocado",500)

apple_object.shopping()
mango_object.shopping()
orange_object.shopping()
avocado_object.shopping()
