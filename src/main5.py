import numpy as np

a=3
b=[[3,6,9],[1,2,3],[2,4,8]]

def matrix_per_scalar(matrix, scalar):
  result=[]
  for i in range(len(matrix)):
    tmp=[]
    for j in range(len(matrix[i])):
      tmp.append(matrix[i][j]*scalar)
    result.append(tmp)
  return result

def print_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      print(str((matrix[i][j]))+"\t", end='')
    print("\n")

print("Input:")
print("Scalar=" + str(a))
print("Matrix=")
print_matrix(b)
print("Matrix x scalar multiplication result:")
print_matrix(matrix_per_scalar(b,a))


def matrix_per_matrix(matrix1, matrix2):
  result=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  for i in range(len(matrix1)):
    for k in range(len(matrix2[0])):
      for j in range(len(matrix1[i])):
        result[i][k]+=matrix1[i][j]*matrix2[j][k]
  return result

A = [[12,7,3],[4,5,6],[7,8,9]]
B = [[5,8,1,2],[6,7,3,0],[4,5,9,1]]

C = matrix_per_matrix(A,B)
print('A=')
print_matrix(A)
print('B=')
print_matrix(B)
print('product=')
print_matrix(C)