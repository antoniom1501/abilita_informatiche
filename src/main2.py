l=[]
print(l)
a=[1,2,'ciao']
print(a[0],a[2])
print('Lunghezza=',len(a))
b=[3,4]
print(a+b)
print(['Hi!']*4)
print(3 in [1,2,3])
for x in [1,2,3]: print(x)
lis=[0,1,2,3,4,5,6,7]
print(lis[0:6])
print(lis[1:5:2])
print(lis[1::2])
print(lis[::2])
print(lis[6:0:-2])

#--------------------------------

l1=range(6)
l2=[e1*2 for e1 in l1]
print("l1=",l1)
print("l2=",l2)
l3=[1,2]
l4=[3,4]
l5=[5,6]
f=[(e1,e2,e3) for e1 in l3 for e2 in l4 for e3 in l5]
print(f)
for e1 in l3:
  for e2 in l4:
    for e3 in l5:
      f.append((l3,l4,l5))

#--------------------------------------

lista=[1,3,4,-5,-2,3]
print("max=",max(lista),"min=",min(lista))
print(lista.count(3))
lista.insert(3,2)
print(lista)

#--------------------------------------
import time
l=list(range(10000))
v=list(range(100000))
T1=time.perf_counter()
s=l+v
T2=time.perf_counter()
print('+ execution time:', T2-T1, 's')
T3=time.perf_counter()
l.extend(v)
T4=time.perf_counter()
print('extend execution time:', T4-T3 , 's')

#--------------------------------------

stack=[1, 2, 3, 4]
print('stack iniziale:', stack)
for i in list(range(5,7)):
  stack.append(i)
print ('Append:', stack)
stack.pop()
print ('Pop:', stack)
queue=['a','b','c','d' ]
print('Initial Queue :', queue)
queue.append('e')
queue.append('f')
print('Append queue :', queue)
queue.pop(0)
print('Pop queue :', queue)

#-----------------------------------

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("elemento 0 di tup1: ", tup1[0]) 
print("elementi dall'1 al 5(escluso) di tup2: ", tup2[1:5])
print('lunghezza tup1=',len(tup1))

#---------------------------------------

my_dict = {}
my_dict = {1: 'apple', 2: 'ball'}
my_dict = {'name': 'John', 1: [2, 4, 3]}
my_dict = dict({1:'apple', 2:'ball'})
print(my_dict)
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict) #ok, stesso output

#---------------------------------------

squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares.pop(4))
print(squares)
print(squares.popitem())
print(squares)
print(len(squares))
print(sorted(squares))
squares.clear()
print(squares)
del squares

#-------------------------------------

marks = {}.fromkeys(['Math','English','Science'], 0)
print(marks)

for item in marks.items():
  print(item)
print(list(sorted(marks.keys())))

#-------------------------------------
s = {'abc','def',1,2,3,'ghi'}
s.add(4)
print(s)
s.update(('lmn',5))
print(s)