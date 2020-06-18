def FindIntersection():
  strArr = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"] #chuỗi số 
  a = strArr[0].split(',')  #chuỗi số thứ 1 gồm 1,3,4,7,13
  b = strArr[1].split(',')  #chuỗi số thứ 1 gồm 1,2,4,13,15
  c = 'false'
  for i in a:
    if i in b:
      if(c == 'false'):
        c = i
      else:
        c = c + ',' + i
  print (c)
  return c

FindIntersection()