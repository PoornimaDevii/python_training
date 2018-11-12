# MCQ
''' model.csv contains right answers
answers.csv contains real answers'''

import functools

a, b = [],[]
marks = 0

f = open('model.csv')
#a = [a.append(line[2].strip('\n')) for line in f.readlines()]
f_list1 = f.readlines()
#print(f_list1)
for line in f_list1:
    a.append(line[2].strip('\n'))
a.remove(',')
#print(a)

f = open('answers.csv')
#b = [b.append(line[2].strip('\n')) for line in f.readlines()]
f_list2 = f.readlines()
#print(f_list2)
for line in f_list2:
    b.append(line[2].strip('\n'))
b.remove(',')
#print(b)

# for i in range(0,9):
#     if a[i]==b[i]:
#         marks += 2
#
# print(marks)

marks = [marks+1 for i in range(0,9) if a[i]==b[i]]
#marks = functools.reduce(lambda x,y:x+y, marks)
marks = sum(marks)
for i in range(0,9):
    if (a[i] != b[i]) and (b[i] != ''):
        marks = marks - 1  #mark deducted for every wrong answer
print("The total number of marks obtained",marks)

# marks1 = list(map(lambda x,y: int(x == y),a,b))
# marks = (sum(marks1) - 1)
# print("The total marks obtained is", 2*marks)

# a1 = set(a)
# b1 = set(b)
# co_ans = set(a.intersection(b))
# print(co_ans)
# marks = 2*(len(co_ans)+1)
# print(marks)

