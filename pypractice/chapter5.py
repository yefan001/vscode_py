###if语句###
#  一个简单的例子  #
""" cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title()) """

#  条件测试  #
#区分大小写
#不等于使用 !=
#比较数字 >,<,>=,<=
#查询多个条件 and，or。为了改善可读性要加括号
#检查特定值是否包含在列表中用 in，not in
""" banned_user=['andrew','carolina','david']
user='marie'
if user not in banned_user:
    print(user.title() + ',you can pose a response if you wish.') """
#布尔表达式是跟踪程序状态的有效工具

#  if语句  #
""" age=17
if age>=18:
    print('You are old enuoge to vote!')
    print('Have you registered to vote?')
else:
    print('Sorry,you are too young to vote.')
    print('Please register to vote as soon as you turn 18.')
 """
""" age=12
if age<14:
    print('Your admission cost is $0')
elif age<18:
    print('Your admission cost is $5')    #可以使用多个elif
else:
    print('Your admission cost is $10') """

#测试多个条件
""" required_toppings=['mushrooms','extra cheese']
if 'mushrooms' in required_toppings:     #区别于使用if-elif-else
    print('Adding mushrooms')

if 'pepperoni' in required_toppings:
    print('Adding pepperoni')

if 'extra cheese' in required_toppings:
    print('Adding extra cheese')

print('\nFinished making your pizza!') """

#  使用if语句处理列表  #
""" required_toppings=['mushrooms','green peppers','extra cheese']
for required_topping in required_toppings:
    if required_topping == 'green peppers':
        print('Sorry,we are out of green peppers right now')
    else:
        print('Adding' + required_topping +'.')

print('\nFinished making your pizza!') """
#确定列表是否为空
""" required_toppings=[]
if required_toppings:             
    for required_topping in required_toppings:
        print('Adding' + required_topping +'.')

    print('\nFinished making your pizza!') 

else:
    print('Are you sure you want a plain pizza?') """
#使用多个列表
""" available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple',
                    'extra cheese']
required_toppings=['mushrooms','french fries ','extra cheese']
for required_topping in required_toppings:
    if required_topping in available_toppings:
        print('Adding' + required_topping +'.')
    else:
        print("Sorry,we don't have " + required_topping +'.')

print('\nFinished making your pizza!')"""


