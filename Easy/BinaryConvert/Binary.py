def BinaryReversal(s): 
    b = bin(int(s))[2:] # chuyển đối số nhị phân
    n = 8
    while n < len(b):
        n *= 2
    return str(int((b.zfill(n))[::-1], 2)) # không hiểu cái dòng này này 
# keep this function call here
a = int(input("nhap so can chuyen doi nhi phan : "))
print (BinaryReversal(a))