s = "Hello world"
news = ""
cur = 0
for i in range(len(s)):
  if s[i] == " ":
    cur = i
    ss = s[:i]
    news = news + ss[::-1] + " "
ss = s[cur:]
news = news + ss[::-1]

print(news)
