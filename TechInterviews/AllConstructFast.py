# Program that returns all the ways the given list of strings can combine to make
# the target string


targetString2 = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
substrs2 = ['e', 'ee', 'eee', 'eeeee', 'eeeeeeee', 'eeeeeeeeee', 'eeeeeeeeeeeeeeeeeeeeeeee']

def AllConstruct(tgtStr, subStrs, memo):
  if tgtStr == '': return [[]]
  if tgtStr in memo: return memo[tgtStr]

  possibleWays = []

  for i in subStrs:
    indx = tgtStr.find(i)    
    if indx == 0:
      result = AllConstruct(tgtStr[indx+len(i):], subStrs, memo)
      for j in result:
        j.insert(0, i)
      possibleWays.extend(result)

  memo[tgtStr] = possibleWays
  return possibleWays

d = {}
x = AllConstruct(targetString2, substrs2, d)

print(x)



