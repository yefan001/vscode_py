###字典###
#  一个简单的字典  #
""" aline_0={'color':'green','points':5}
print(aline_0['color'])      #列表，元组，字典都是[]
print(aline_0['points']) """

#  使用字典  #
""" #访问字典中的值
new_points=aline_0['points']
print('You just earned ' + str(new_points) + ' points.')
#添加键值对
aline_0['x_position']=0
aline_0['y_position']=25
aline_0['speed']='fast'
print(aline_0)
#修改字典中的值
aline_0['color']='yellow'
#删除键值对
del aline_0['speed']
print(aline_0) """
#由类似对象组成的字典
""" favorite_languages={   #每个人喜欢的编程语言
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    } """

#  遍历字典  #
""" user_0={
        'username':'efermi',
        'first':'enrico',
        'last':'fermi'
    }
for k,v in user_0.items():     #加s
    print('\nkey: ' + k)
    print('value: ' + v) """

#遍历字典中所有键值
""" favorite_languages={   #每个人喜欢的编程语言
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    } 
friends=['sarah','phil']
for name in favorite_languages.keys():   #加s
    print(name.title())
    if name in friends:
        print('Hi ' + name.title() + ',I see your favorite language is' + favorite_languages[name].title() + '!')

#按顺序遍历字典中所有键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ',thank you for talking the poll.')

#遍历字典之中所有值
print('The following languages are mentioned:')
for language in favorite_languages.values():
    print(language)

#去除重复项 for language in set(favorite_languages.values()): """

#  嵌套  #
#字典列表
""" aline_0={'color':'green','points':5}
aline_1={'color':'yellow','points':10}
aline_2={'color':'red','points':15}

aliens=[aline_0,aline_1,aline_2]
for alien in aliens:
    print(alien) """
""" #创建一个用于存储外星人的列表
aliens = []
#创建30个绿色外星人
for alien_number in range(30):     #for前面别有空格
    new_alien={'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)      #aliens单词别打错了

for alien in aliens[0:3]:
    if alien['color']=='green':     #别忘加冒号'green'
        alien['color']='yellow'
        alien['speed']='medium'
        alien['point']=10
    
 #显示前五个外星人
for alien in aliens[:5]:
    print(alien)

print('......')
print('Total number of aliens:' + str(len(aliens))) """

#在字典中存储列表
""" #存储所点pizz信息
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
    }
print('You order a' + pizza['crust'] + '-crust pizza' + 
      'with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping) """

#在字典中存储字典
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
        },             #别忘了逗号
    'mcurie':{
        'first':'marice',
        'last':'curie',
        'location':'paris'        
        }
    }
for username,user_info in users.items():
    print("Username:" + username)
    full_name=user_info['first'] + ' ' + user_info['last']
    location=user_info['location']
    print('\tFull name: ' + full_name)
    print('\tLocation: ' + location)
