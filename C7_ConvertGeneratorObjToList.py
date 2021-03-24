def firstval_gen(n):
 i = 1
 while i<=n:
  yield i
  i=i+1

g = firstval_gen(5)
l = list(g)
print(l)