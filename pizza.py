def greet():
    greet=("welcome to the pizza world")
    print(greet)
greet()
customer_name=input("Enter customer name:")
pizza_types={
    "cheese pizza":550,
    "pepporoni pizza":450,
    "margherita pizza":590,
    "veggie pizza":330,
    "BBQ Chicken Pizza":700
}
for key,value in pizza_types.items():
    print(key,value)
    
cp=0
x=input("Select pizza:")
cp+=pizza_types[x]
print(f"cost of pizza is:{cp}")

pizza_toppings={
    "cheese":350,
    "pepperoni":500,
    "mushrooms":400,
    "spinach":250,
    "green peppers":200,
    "pineapple":450,
    "garlic":300
}
for key,value in pizza_toppings.items():
    print(key,value)
cp=0
while True:
    y=input("select toppings and write done if you are done with selection:")
    if y=="done":
        break
    cp+=pizza_toppings[y]
print(f"total amount of toppings:{cp}")
Total_cost=cp+cp
print(f"total amount including price of pizza and toppings:{Total_cost}")






