def FindIntersection(strArr):
    n = input('Nhập số lượng cần nhập ở dãy 1')
    m = input('Nhập số lượng cần nhập ở dãy 2')
    for i 
    a = input('nhập dãy thứ 1') 
    b = input('nhập dãy thứ 2')
  a = strArr[0].split(',')
  b = strArr[1].split(',')
  c = 'false'
  for i in a:
    if i in b:
      if(c == 'false'):
        c = i
      else:
        c = c + ',' + i
  # code goes here
  return c

# keep this function call here 
print FindIntersection(raw_input())