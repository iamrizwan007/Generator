#Generate 3 values 'A','B','C'
def mygen():
 yield 'A'
 yield 'B'
 yield 'C'

g = mygen()	#generator object
for x in g:
 print(x) 