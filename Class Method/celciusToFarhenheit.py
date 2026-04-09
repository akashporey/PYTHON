class Temperature:
    def __init__(self,temp):
        self.t=temp
    
    def to_celcius(self):
        tempinCelcius=(self.t-32)*(5/9)
        print(f"Temperature in celcius: {tempinCelcius:.2f}°C ")
        # return tempinCelcius
    
temp=float(input("Enter temperature in farhenheit: "))
t1=Temperature(temp)
t1.to_celcius()
