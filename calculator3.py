for x in range(1,5,1):
    user_input=input("Enter +,-,*,/,%")
    if user_input=="+":
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        c=a+b
        print(c)
    elif user_input=="-":
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        c=a-b
        print(c)
    elif user_input=="*":
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        c=a*b
        print(c)
    elif user_input=="/":
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        c=a/b
        print(c)
    elif user_input=="%":
        a=int(input("Enter first number"))
        b=9
        c=a%b
        print(c)
    else:
        print("invalid operation!")