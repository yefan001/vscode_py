#chapter9
class Car():
    def __init__(self,make,model,year):
        self.make=make             #定义类属性
        self.model=model
        self.year=year
        self.odometer_reading=0     #里程数，给属性指定默认值

    def get_dsecriptive_name(self):
        long_name=str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        #self.odometer_reading=mileage
        if mileage >= self.odometer_reading:   #禁止里程数回调
            self.odometer_reading=mileage
        else:
            print("You can't roll back odometer!")
        
    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def fill_gas_tank():                      #被重写的方法
        print("ohhhhhhhhhhhhh")

class ElectricCar(Car):
    --ship--

