def divide(x,y):
  try:
    result = x/y
  except ZeroDivisionError:
    print('Divisione per zero')
  else:
    print("il risultato è",result)
  finally:
    print("executing finally clause")

divide(2,0)
divide(2,1)


x = range(3, 20, 2)
for n in x:
  print(n)

a = ("Marco", "Luca", "Claudio")
b = ("Giovanna", "Maria", "Anna", "Francesca")
x = zip(a, b)
print(tuple(x))

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)
result_list = list(result)
print(result_list)
c, v = zip(*result_list)
print('c =', c)
print('v =', v)