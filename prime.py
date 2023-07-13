def is_prime(num):
    a=0
    for i in range(1,num+1,1):
        if num%i==0:
            a+=1
    if a<=2:
        return True
    else:
        return False
num=int(input("Enter a number"))
if is_prime(num)==True:
        print(f"{num}is prime")
else:
        print(f"{num}is composite")