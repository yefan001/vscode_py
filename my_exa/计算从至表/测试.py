import numpy as np
import pandas as pd

""" def permutation(nums, p, q):
    if p == q:
        s.append(list(nums))
    else:
        for i in range(p, q):
            nums[i], nums[p] = nums[p], nums[i]
            permutation(nums, p+1, q)
            nums[i], nums[p] = nums[p], nums[i]
s= []
nums = [i for i in range(1, 7)]
permutation(nums, 0, len(nums))
print(s) """

""" def permutation(nums, p, q):
    s= []         #行不通，每次递归都会将其更新为0
    if p == q:
        s.append(list(nums))
    else:
        for i in range(p, q):
            nums[i], nums[p] = nums[p], nums[i]
            permutation(nums, p+1, q)
            nums[i], nums[p] = nums[p], nums[i]

    return s

nums = [i for i in range(1, 7)]
s=permutation(nums, 0, len(nums))
print(s) """

""" obj=pd.Series(['A','B','C','D','E','F'],index=[1,2,3,4,5,6])
print(obj[1])
print(obj[obj.values=='A'].index)


a=[9,['A','D','C','F']]
print(a[1])
print(a[1][2])
print(a[1].index('C'))

b=[1,2,3,4,5]
print(b.index(2)) """

#---------------------------------------------------------------

#原材料库A  铸造车间B  热处理车间C   机加工车间D   精密车间E    标准件半成品库F
#仓库组成的序列
obj=pd.Series(['A','B','C','D','E','F'],index=[1,2,3,4,5,6])
#print(obj)
#零件组成的字典。零件名：权重，[加工顺序]
parts={'s1':[9,['A','D','C','F']],           
      's2':[90,['A','B','D','E','F']],
      's3':[3,['A','B','D','F']],
      's4':[3,['A','D','E','F']],
      's5':[27,['A','D','E','F']],
      's6':[700,['A','B','D','E','F']],
      's7':[60,['A','D','C','E','F']],
      's8':[56,['A','D','E','F']],
      's9':[32,['A','D','F']],
      's10':[1,['A','D','C','E','F']],
      's11':[120,['A','C','D','C','E','F']],
      's12':[60,['A','C','D','C','E','F']],
      's13':[80,['A','D','C','F']]
      }

#print(part)


def one_part_folw(info,now_range):  #计算一个零件在某排序下的流量
    #s1：[9,['A','D','C','F']]
    #目前排序124356-ABDCEF
    print(info) ##
    print(now_range) ##
    p_flow=0    #不加权重的流量
    n=len(info[1])
    print(n)
    for i in range(n-1):   #工序A对应的数字1，在新排序中的先后位置
        #info[1][i]
        print(i)
        index_f = obj[obj.values==info[1][i]].index  #工序对应的标签
        index_l=obj[obj.values==info[1][i+1]].index   ###别忘了加一
        f=now_range.index(index_f)    
        l=now_range.index(index_l)
        print('f:' + str(f))
        print('l:' + str(l))
        if f > l:
            p_flow += (f-l)*2
        else:
            p_flow += (l-f)

    total_flow=p_flow*info[0]
    print('total:'+ str(total_flow)) ##
    return total_flow

a=[1,2,3,4,5,6]
now_flow=0
for part in parts.values():
        part_flow=one_part_folw(part,a)
        now_flow += part_flow

print(now_flow)


