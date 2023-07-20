def main():
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        result=factorial(6)
        print(f"The factorial of {n}is:{result}")

if __name__ == "__main__":
    main()
