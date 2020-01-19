###类###
#  创建和使用类  #
#创建dog类
class Dog():    #类名开头大写
    def __init__(self,name,age):    #开头结尾各两个下划线，自动调用
        self.name=name
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
my_dog.roll_over()

#  使用类和实例  #


        
