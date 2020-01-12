###操作列表###

#  遍历整个列表  #
""" magicians = ['alice','david','carolina']
for magician in magicians:    #加冒号   #理论上magician可以为任何单词
    print(magician.title() + ',that was a great trick!')
    print("I can't wait to see you next trick," + magician.title() + "\n" )

print('Thank you,everyonr.That was a great magic show!') """

#  避免缩进错误  #
#忘记缩进
#忘记缩进额外的代码行
#不必要的缩进
#循环后不必要的缩进
#遗漏了冒号

#  创建数值列表  #
""" for range_1 in range(1,5):
    print(range_1)      #输出1-4，不是5

numbers = list(range(2,11,2))    #初值。终值，步长
print(numbers)

squares=[]
for value in range(1,11):
    squares.append(value**2)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares=[value**2 for value in range(1,11)]   #列表解析
print(squares) """

#  使用列表一部分  #
""" players=['charles','martina','michael','florence','eli']
print(players[1:3])    #切片,第1，2个
print(players[:3])
print(players[2:])
print(players[-3:])   #从0开始倒数

print('Here are the first three players in my team:')
for player in players[0:3]:
    print(player.title())

my_foods=['pizza','falafel','carrot cake'] #复制列表
friend_foods=my_foods[:]   #若使用friend_foods=my_foods，则共用一个内存，不是两个列表
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are:')
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods) """

#  元组  #
dimiensions=(200,50)     #不可修改
print(dimiensions[0])
print(dimiensions[1])

print('Origoinal dimiensions:')
for dimiension in dimiensions:
    print(dimiension)

dimiensions=(400,100,300)   #修改元组变量
print('\nModified dimiendions:')
for dimiension in dimiensions:
    print(dimiension)
#  设置代码格式  #
#缩进，行长，空行


