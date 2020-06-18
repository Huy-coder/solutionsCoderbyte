def QuestionsMarks(str):

    a = 0
    b = 0
    for i in range(len(str) - 1):
        for j in range(i, len(str)):
            if str[i].isdigit() and str[j].isdigit() and int(str[i]) + int(str[j]) == 10: #check xem có phải số hay không và + lại có bằng 10 hay không
                a, b = i, j
    new = str[a+1:b+1] 
    if new.count('?') == 3:
        return 'true'
    else:
        return 'false'
    
    return str

str = "arrb6???4xxbl5???eee5"
print(QuestionsMarks(str)) 