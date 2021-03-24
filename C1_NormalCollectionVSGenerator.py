#Python generator function--> Generate a sequence of value
#keyword --> yield --> resposible to generate seq of value
#Normal Collection:
l = [x*x for x in range(10)]	#incase of 10, 1000000000000000000 (heap memory, memory error)
print(l)
print(l[0])

#Generator:
g = (x*x for x in range(1000000))	#generator object, comprehension not supported in tuple
print(type(g))	#Generator object
while True:
 print(next(g))	#No memory error, genates next element but does not store

