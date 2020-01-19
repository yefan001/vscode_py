###函数###
#  定义函数  #
#向函数传递信息
""" def greet(user_name):
    print('Hello,' + user_name.title() + '.')

greet('jesse') """

#实参和形参

#  传递实参  #
#位置实参
""" def describe_pets(animal_type,pet_name='dog'):  #可以设置默认值
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name + '.')

describe_pets('hamster','harry')  
describe_pets('dog','willie')  #注意参数的位置，避免实参错误
#关键字实参
describe_pets(pet_name='NB',animal_type='pig') """

#  返回值  #
""" def get_formatted_name(first_name,last_name,middle_name=''):   #让参数可选
    if middle_name:
        full_name=first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name=first_name + ' ' + last_name
    
    return full_name

musician=get_formatted_name('jimi','hendrix')
print(musician)

musician=get_formatted_name('jimi','midd','hendrix')
print(musician) """

#返回字典
""" def build_persion(first_name,last_name,age=''):
    persion={'first':first_name,'last':last_name}
    if age:
        persion['age']=age
    return persion

musician=build_persion('jimi','hendrix',age=27)
print(musician) """

#结合使用函数和while循环
""" def get_formatted_name(first_name,last_name):   
    full_name=first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit )")
    f_name=input('First name:')
    if f_name=='q':
        break

    l_name=input('Last name:')
    if l_name == 'q':
        break

    formatted_name=get_formatted_name(f_name,l_name)   #没有冒号
    print('\nHello, ' + formatted_name + '!') """

#  传递列表  #
""" def greet_users(names):
    for name in names:
        msg='Hello, ' + name + '!'
        print(msg)

usernames=['ohhhh','sb','nba']
greet_users(usernames) """

#在函数中修改列表
""" unprinted_designs=['iphone case','robbot pendant','dodecahedron']
completed_models=[]
while unprinted_designs:
    current_design=unprinted_designs.pop()
    print('Printing model:' + current_design)
    completed_models.append(current_design)

print('The following models have been printed:')   
for completed_model in completed_models:
    print(completed_model)

#也可封装为转移和显示两个函数，更加清晰
def print_models(unprinted_designs, completed_models):
	#模拟打印每个设计 直到 有未打印的设计为止
	#打印每个设计后 都将其移到列表completed_models中
	while unprinted_designs:
  		current_design = unprinted_designs.pop()

  		# 模拟根据设计制作3D打印模型的过程 
  		print("Printing model: " + current_design) 
  		completed_models.append(current_design)

def show_completed_models(completed_models): 
	#显示打印 的所有模型
	print("\nThe following models have been printed:") 
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = []
print_models(unprinted_designs, completed_models) 
show_completed_models(completed_models)
 """

 #禁止函数修改列表
 #print_model(unprinted_designs[:],completed_models)  #使用切片生成原列表副本

#  传递任意数量的实参  #
""" def make_pizza(size,*toppings):    #结合位置实参和任意参数实参
    print('\nMaking a ' + str(size) +'-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)
    
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese') """

#使用任意数量的关键字实参
""" def buile_profile(first,last,**user_info):   #是两个*，创造空字典
    profile={}                               #一个*，创建空元组
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    
    return profile

user_profile=buile_profile('albert','einstein',location='princetion',feild ='physics')
print(user_profile) """

#  将函数存储在模块中  #
import pizza 

pizza.make_pizza(16,'pepperion','mushroom','extra cheese')

#导入特定的函数
from pizza import make_pizza

#使用as 给函数指定别名（不常用）
from pizza import make_pizza as mp

#使用as给模块指定别名
import pizza as p

#导入模块中所有函数
from pizza import *

make_pizza(16.'green pepper')  #不用再pizza.make_pizza









