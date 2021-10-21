def fibo(n):
  a=6
  b=1
  for i in range(3,n+1):
    c=a+b
    a=b
    b=c
  return(c)
print(fibo(35))