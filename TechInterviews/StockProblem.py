def stock_buy_sell(array):

  buy = [i for i in range(len(array))]

  for i in range(1,len(array)):
    if array[i] < array[buy[i-1]]:
      buy[i] = i
    else:
      buy[i] = buy[i-1]

  print(buy)
  b,s = 0,0
  sell = [i for i in range(len(array))]
  sell[0] = -1000
  for i in range(1,len(array)):
    if sell[i-1] > array[i] - array[buy[i-1]]:
      sell[i] = sell[i-1]
    else:
      sell[i] = array[i] - array[buy[i-1]]
      b = array[buy[i-1]]
      s = array[i]

  #print(sell)
  #sellspot = sell[len(sell)-1]
  #buyspot = buy[sellspot-1]
  return b,s


arr = [8,5,12,9,19,1]

buy, sell = stock_buy_sell(arr)
print(buy, sell)


arr2 = [21,12,11,9,6,3]
buy2, sell2 = stock_buy_sell(arr2)
print(buy2,sell2)


