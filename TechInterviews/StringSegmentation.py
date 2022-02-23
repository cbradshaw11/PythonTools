d = {"apple", "pear", "pie"}

def StringSegmentation(s):
  cur = 0
  done = False
  for i in range(len(s)):
    done = False
    if s[cur:i] in d:
      cur = i
      done = True
  if done:
    print("YES!")
  else:
    if s[cur:] in d:
      print("YES")
    else:
      print("NO")

StringSegmentation("applepear")
StringSegmentation("applepeer")


