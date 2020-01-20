#计算从至表
import numpy as np
import pandas as pd

#————————————————————————————修改的内容————————————————————————————————#

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

#—————————————————————————场地数组的全排列——————————————————————————————#

m=len(obj)    #加工场地的个数
obj_sort=[i for i in range(1, m+1)]  #需要排列的列表

def AllRange(listx,p,q):      #递归生成全排列列表sorts  
    if p == q:
        all_sorts.append(list(listx)) 
    else:
        for i in range(p,q):
            listx[i],listx[p]=listx[p],listx[i]
            AllRange(listx,p+1,q)
            listx[i],listx[p]=listx[p],listx[i]
        
all_sorts=[]                 #所有全排列可能的列表
AllRange(obj_sort,0,len(obj_sort))

#—————————————————————————计算流量最小时的排列——————————————————————————#

min_flow=100000000     #最小流量，根据情况设置一个比较大的值
best_sort=[]           #最小流量下的排序

#计算一个零件在某排序下的流量
def one_part_folw(info,now_range):  
    p_flow=0    #不加权重的流量
    n=len(info[1])
    for i in range(n-1):   #工序A对应的数字1，在新排序中的先后位置
        index_f=obj[obj.values==info[1][i]].index  #工序对应的标签
        index_l=obj[obj.values==info[1][i+1]].index
        f=now_range.index(index_f)    
        l=now_range.index(index_l)
        if f > l:
            p_flow += (f-l)*2
        else:
            p_flow += (l-f)

    total_flow=p_flow*info[0]
    return total_flow

#找出所有序列流量最小值及对应序列
for all_sort in all_sorts[:]:     
    now_flow=0    #本次排列的流量
    for part in parts.values():
        part_flow=one_part_folw(part,all_sort)  #每个零件的流量
        now_flow += part_flow

    if now_flow <= min_flow:
        min_flow=now_flow
        best_sort=all_sort[:]

#—————————————————————————————输出结果——————————————————————————————————#        

print('min flow:')
print(min_flow)
print('best sort:')
for i in range(m):
    print(obj[best_sort[i]])



    




            



















