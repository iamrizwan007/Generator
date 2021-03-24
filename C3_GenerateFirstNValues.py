def mygen(n):
 i=1
 while i<=n:
  yield i
  i=i+1

val = int(input("Enter number to generate value"))
g = mygen(val)
for x in g:
 print(x)