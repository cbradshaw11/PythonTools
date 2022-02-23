def one_edit_apart(s1, s2):
   if len(s1) > len(s2):
      swap(s1, s2)
   if len(s2) - len(s1) > 1:
      return False

   saw_diff = False
   i=0
   j=0
   while(i<len(s1) and j<len(s1)):
      if s1[i] != s2[j]:
         if saw_diff:
            return False
         saw_diff = True
         if len(s2) > len(s1):
            i = i-1
      i = i+1
      j = j+1
   return saw_diff or (len(s2) != len(s1))

import sys
s = sys.argv[1]
ss = sys.argv[2]
if not one_edit_apart(s,ss):
   print("ONE EDIT!")
else:
   print("NOT ONE EDIT :(")
