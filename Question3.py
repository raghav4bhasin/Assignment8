'''
Q.3- Create a Temprature class and create two methods: 
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
'''

class Temperature:
    def convertFahrenheit(self, tempC):
        CtempF = (tempC * 1.8) + 32
        return CtempF

    def convertCelsius(self, tempF):
        FtempC = (tempF - 32) / 1.8
        return FtempC

t1 = Temperature()

print("Enter 1 to Convert Fahrenheit to Celsius.")
print("Enter 2 to Convert Celsius to Fahrenheit.")

ch = int(input("\tEnter your option: "))
print(" ")

if ch is 1:
    temp_Cel = int(input("Enter temperature in deg. Celsius: "))
    res = t1.convertFahrenheit(temp_Cel)
    print("Result: ", res, "deg.C")

elif ch is 2:
    temp_Fah = int(input("Enter temperature in Fahrenheit: "))
    res = t1.convertCelsius(temp_Fah)
    print("Result: ", res, "F")
else:
    print("ERROR!! Invalid choice input.")
        

