def cube(n,i,result):
  if(i==n):
    return result
  else:
    return cube(n,i+1,result*n)
  

print(cube(3,0,1))