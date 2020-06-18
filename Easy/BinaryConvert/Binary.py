def BinaryReversal(s): 
    b = bin(int(s))[2:] # chuyển đối số nhị phân
    n = 8
    while n < len(b):
        n *= 2
    return str(int((b.zfill(n))[::-1], 3)) # không hiểu cái dòng này này 
# keep this function call here
a = '213'
print (BinaryReversal(a))