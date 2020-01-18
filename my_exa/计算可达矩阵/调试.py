import numpy as np

def change(a):                 #乘自身并归一
	b=np.dot(a,a)
	m=a.shape
	for i in range(m[0]):      #range(6)---0-5
	    for j in range(m[1]):
		    if b[i,j]!=0:
			    b[i,j]=1
	return b

def unit(n):                   #生成n维单位矩阵
	a=np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			if i==j:
				a[i,j]=1
	return a

def keda(b):                   #生成可达矩阵
	m=b.shape
	unit_b=unit(m[0])
	K1=b+unit_b

	for i in range(15):
		KN=change(K1)
		print('---------------')
		print(KN)
		print('---------------')
		
		if np.array_equal(KN,K1)==True:
			print('YUNXINGKSNDVJSNDK')
			break

		K1=KN

	print(KN)

	return KN

######################################

A=np.array([[0,0,0,0,0,0,0,0,0,0],
	        [1,0,1,1,0,0,0,0,0,1],
	        [0,0,0,0,0,0,0,0,0,0],
	        [0,0,0,0,0,0,0,0,0,1],
	        [1,0,0,0,0,1,0,0,0,0],
	        [1,0,0,0,1,0,0,0,0,0],
	        [1,1,0,0,0,0,0,1,0,0],
	        [1,0,1,1,0,0,0,0,0,1],
	        [1,1,0,0,1,1,0,1,0,0],
	        [1,0,1,0,0,0,0,1,0,0]],dtype=int)

#print(A)

B=keda(A)

'''
ss=[0,2,3,4,5,9,7,1,6,8]
C=np.zeros((n,n))
for m in range(10)
for i in ss:
		for j in ss:
			C[i,j]=

A=np.array([[0,0,1,0,1,0],
	 		[0,0,0,1,0,0],
	 		[0,0,0,0,0,0],
	 		[0,1,0,0,0,1],
	 		[1,1,0,0,0,0],
	 		[0,0,0,0,0,0]],dtype=int)

B=keda(A)
'''