def FindIntersection():
  strArr = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
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
  print (c)
  return c

# keep this function call here 
#print FindIntersection(raw_input())

FindIntersection()