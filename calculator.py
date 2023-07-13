user_input=input("Enter +,-,*")
if user_input=="-":
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    c=a-b
    print(c)
elif user_input=="+":
    e=int(input("Enter first number"))
    f=float(input("Enter second numner"))
    g=e+f
    print(g)
elif user_input=="*":
    r=int(input("Enter first number"))
    s=int(input("Enter second number"))
    t=r*s
    print(t)
else:
    print("You have entered wrong!")