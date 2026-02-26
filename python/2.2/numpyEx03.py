import numpy as np
data=[0,1,2,3,4,5,6,7,8,9]
answer=[]
for di in data:
    answer.append(2*di)
print(answer)


x=np.array(data)               #리스트를 배열로만듬
x = x * 2              #리스트를 하나씩 계산해서 배열 for문 안써도됨
print(x)

a=np.array([1,2,3])
b=np.array([10,20,30])
print(a + b)          # 각 리스트끼리 더하기
print(a == 2)
print(b > 10)         
print((a == 2) & (b > 10))    #and, &, &&  numpy는 &사용(한개라도 포함되면 true)


#a=np.array([1,2,3])
print(a.ndim)
print(a.shape)          #튜플로 줌
#c=np.array([[0,1,2], [3,4,5]])
c=np.array([[0,1,2], [3,4,5]])
print(c.ndim)
print(c.shape)
d=np.array([[[1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]],
 [[11,12,13,14],
 [15,16,17,18],
 [19,20,21,22]]]) #2x3x4array
print(d.ndim)
print(d.shape)

a=np.array([0,1,2,3,4,5,6,7,8,9])
idx=np.array([True,False,True,False,True,
False,True,False,True,False])   #True인것만 출력, 논리값으로도 가능
idx2 = np.array([0,2,4,6,8])    # 인덱스 번호 대로 가져옴
idx3 = np.array(a%2 == 0)       #몫이 0인거만 가져옴
print(a[idx])
print(a[idx2])
print(a[idx3])    