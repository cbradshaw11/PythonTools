def Swap(s1, s2):
   s3 = s1
   s1 = s2
   s2 = s3
   return s1, s2

def CheckOneEdit(s1, s2):
   if len(s1) > len(s2):
      s1,s2 = Swap(s1,s2)
      if len(s1) - len(s2) > 1:
         return False
   else:
      if len(s2) - len(s1) > 1:
         return False

   numDiffs = 0
   i = 0
   for i in range(len(s1)):
      if s1[i] != s2[i]:
         if numDiffs:
            return 0
         numDiffs = numDiffs + 1
         if i == len(s2)-1:
            if(numDiffs > 1):
               return 0
            else:
               return 1   
         else:
            if s1[i] != s2[i+1]:
               return 0
   if numDiffs < 2:
      return 1

import sys
s15 = sys.argv[1]
s25 = sys.argv[2]

if CheckOneEdit(s15, s25):
   print("One Dif!")
else:
   print("NOT ONE DIF :(")

   
