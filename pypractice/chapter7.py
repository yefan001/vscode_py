###用户输入和while循环###
#  函数input()的工作原理  #
#编写清晰的程序
""" message=input('Tell me something, and I will repeat it back to you:')
print(message)

promot='If you tell me who you are,we can personalize the message you see.'
promot += '\nWhat is your first name?'
name=input(promot)
print('\nHello,' + name + '!')
 """

#使用int()获取数值输入
""" heigh=input('How tell are you? in inches.')
heigh=int(heigh)
if heigh >= 36:
     print('\nYou are tall enough to ride.')
else:
    print('\nYou are be allow to ride when you are a little older.') """

#求模运算符
""" number=input("Tell me a number,and I'll tell you if it's even or odd:")
number=int(number)
if number%2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else:
    print('\nThe number ' + str(number) + ' is odd.') """

#  while循环简介  #  
#使用while循环
""" current_number=1
while current_number <=5:
    print(current_number)
    current_number +=1 """

#让用户选择何时退出
""" promot='If you tell me who you are,we can personalize the message you see.'
promot += "\nEnter 'quit' to end the progrom." 
message=''
while message != 'quit':
    print(message)
    if message != 'quit':
        message=input(promot) """

#使用标志
""" promot='If you tell me who you are,we can personalize the message you see.'
promot += "\nEnter 'quit' to end the progrom." 

active=True
while active:
    message=input(promot)
    if message == 'quit':
        active=False
    else:
        print(message) """

#使用break退出循环
""" promot='\nPlesae enter the name of a city you have visited:'
promot += "\n(Enter 'quit' when you are finish.)"

while True:
    city=input(promot)  

    if city == 'quit':   #是== 不是=
        break
    else:
        print("\nI'd love to go to " + city.title() + '!') """

#在循环中使用continue
""" current_number=0
while current_number <=10:
    current_number += 1
    if current_number % 2 ==0:
        continue

    print(current_number) """

#避免无限循环

#  使用while循环来处理字典和列表  #
#在列表之间移动元素
""" unconfirmed_users=['alice','brain','candance']
confirmed_users=[]

while unconfirmed_users:      #注意这个用法
    current_user=unconfirmed_users.pop()
    print('Verifying user:' + current_user.title())
    confirmed_users.append(current_user)

print('The following users has been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user) """

#删除包含特定值的所有列表元素
""" pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
pets.remove('cat')    #一次只能删除一个
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets) """

#使用用户输入来填充字典
responses={}
polling_active=True

while polling_active:
    name=input('What is your name?')
    response=input('Which mountain would you like to climb someday')
    responses[name]=response

    repeat=input('Would you like to let another to respond?(yes/no)')
    if repeat=='no':
        polling_active=False

print('---------polling results---------')
for name,response in responses.items():
    print(name + 'would you like to climb' + response + '.')












   