import time
def countdown_gen(num):
 while num>=1:
  yield num
  num = num - 1

g=countdown_gen(10)
for x in g:
 print(x)
 time.sleep(1)