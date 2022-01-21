input1 = input("input List 1: ").split(',')
input2 = input("input list 2: ").split(',')

input1.sort()
input2.sort()
 
len_1 = len(input1)
len_2 = len(input2)
 
if len_1 >= len_2:
   limit = len_1
   schema = 'A'
else:
   limit = len_2
   schema = 'B'
# for i in range(limit):
res = {}
for i in range(limit):
   if schema == 'A':
       if i < len_2:   
           res[input1[i]] = input2[i]
       elif i >= len_2:
           res[input1[i]] = "NULL"
   elif schema == 'B':
       if i < len_1:   
           res[input1[i]] = input2[i]
       elif i >= len_1:
           res[''] = input2[i]
print(res)