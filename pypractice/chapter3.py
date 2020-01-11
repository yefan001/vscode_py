###列表简介###

#  列表是什么  #
""" bicycles = ['trek','cannondale','redline','specialized']  ###加空格
print(bicycles)
print(bicycles[0])    #索引从0开始
message="My first bicycle was a " + bicycles[1].title() + '.'
print(message)

bicycles[0]='honda'  #修改列表的值
bicycles.append('ducati')  #添加至列表末尾
bicycles.insert(1,'yamaha')   #在某位置插入新元素
print(bicycles)

del bicycles[4]   #删除任意位置的元素        ###打完中文后习惯性恢复为英文
poped_bicycle=bicycles.pop()   #弹出末尾的值，并返回
print(poped_bicycle)
first_bicycle = bicycles.pop(0)  #弹出任意位置的元素
print("Pop " + first_bicycle.title())
bicycles.remove('cannondale')  #根据值删除元素
print(bicycles) """

#  组织列表  #
""" cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)    #对列表进行永久排序
cars.sort(reverse = True)
print(cars)

print('\nHere is a sorted list:')
print(sorted(cars))   #进行临时排序，原列表顺序不变
print(cars)
cars.reverse()    #倒转列表
print(cars)
print(len(cars))       #确定列表长度,有几个元素 """








