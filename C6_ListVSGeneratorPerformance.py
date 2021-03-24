import random
import time
names = ['sunny','bunny','chinny','vinny']
subjects =['python','java','data science']
def students_list(num):
 students =[]
 for i in range(num):
  student = {'id':i, 'name':random.choice(names),'subject':random.choice(subjects)}
  students.append(student)
 return students

def students_gen(num):
 for i in range(num):
  student = {'id':i, 'name':random.choice(names),'subject':random.choice(subjects)}
 yield student
  

t1 = time.process_time()
students = students_list(100000)
t2 = time.process_time()
print("Time required to create students list",t2-t1)

t1 = time.process_time()
g = students_gen(100000)
t2 = time.process_time()
print("The required to creare students generator",t2-t1)