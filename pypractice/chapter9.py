###类###
#  创建和使用类  #
#创建dog类
""" class Dog():    #类名开头大写
    def __init__(self,name,age):    #开头结尾各两个下划线，自动调用
        self.name=name              #self为这个对象
        self.age=age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')

#根据类创建实例

my_dog=Dog('willie',6)
print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + 'years old.')

my_dog.sit()
my_dog.roll_over() """

#  使用类和实例  #
""" class Car():
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

my_new_car=Car('audi','a4','2016')     #对象的实例
print(my_new_car.get_dsecriptive_name())
my_new_car.update_odometer(18)  #通过方法修改类属性
my_new_car.read_odometer()
my_new_car.odometer_reading=66  #直接修改属性值
my_new_car.read_odometer()

my_used_car=Car('subaru','ouback','2013')
print(my_used_car.get_dsecriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer() """

#  继承  #
#子类的方法__init__()
""" class Car():
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
    def __init__(self,make,model,year):  #初始化父类的属性
        super().__init__(make,model,year)   #super是父类的    #super记得加（）
        self.battery_size=70

    def describe_battery(self):       #给子类定义属性和方法
        print("This car has a " + str(self.battery_size) + "-kWh battery." )

    def fill_gas_tank():  #重写父类的方法
        pass

my_tesla=ElectricCar('tesla','model s','2016')
print(my_tesla.get_dsecriptive_name())                       #记得加（）
my_tesla.describe_battery() """

#将实例用作属性
""" class Car():
    --ship--

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    def __init__(self,make,model,year): 
        super().__init__(make,model,year)   
        self.battery=Battery()       #将实例用作属性，不同种类车子都有电池时，方便

my_tesla=ElectricCar('tesla','model s','2016')
print(my_tesla.get_dsecriptive_name())   
my_tesla.battery.describe_battery()   #my_tesla的bettery属性为Battery的实例 """

#  导入类  #
""" #导入单个类
from car import Car
#一个模块导入多个类
from car import Car,ElectricCar
#导入模块中所有类
from car import *
#也可在一个模块导入另一个模块 """


#  python标准库  #
from collections import OrderedDict

favorite_language=OrderedDict()  #记录键值对的添加顺序，按照添加顺序排列




        

        
