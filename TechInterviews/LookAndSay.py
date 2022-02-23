
iterations = 5

def LookAndSay(l):
   newlist = []
   b = 1
   num_same = 0
   current_num = 1
   for index, val in enumerate(l):
      if index == 0:
         current_num = val
         num_same = 1
      else:
         if val == current_num:
            num_same = num_same + 1
         else:
            newlist.append(num_same)
            newlist.append(current_num)
            current_num = val
            num_same = 1
   newlist.append(num_same)
   newlist.append(current_num)   
   return newlist

list = [1] 
i = 0
while(i < iterations):
   list = LookAndSay(list)
   print(list)
   i = i+1
