def celsius_to_F(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
celsius=float(input("Enter temperature in degree celsius:"))
converted_temperature=celsius_to_F(celsius)
print("Temperature in degree fahrenheit:",converted_temperature)
