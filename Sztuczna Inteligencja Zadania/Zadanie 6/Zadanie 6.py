def checkrows(colnum,rownum,operator1,operator2,not_check,check):
    while (colnum>-1 and colnum<(len(check))):
            if not_check == False:
                return not_check
            colnum +=operator1
            if(operator2!=0):
                rownum +=operator2
            else:
                rownum = rownum
            if colnum>-1 and colnum < (len(check)):
                if check[colnum] == rownum and rownum!=0:
                    not_check = False
                    return not_check
    return not_check
                
def search_queens():
    check = []
    for i in range(0,8):
        check.append(0)
    col = 0
    while(col<8):
        colnum = col
        check[col] = check[col]+1
        not_check = checkrows(colnum,check[col],1,1,True,check)
        colnum = col
        not_check = checkrows(colnum,check[col],1,-1,not_check,check)
        colnum = col
        not_check = checkrows(colnum,check[col],-1,1,not_check,check)
        colnum = col
        not_check = checkrows(colnum,check[col],-1,-1,not_check,check)
        colnum = col
        not_check = checkrows(colnum,check[col],1,0,not_check,check)
        colnum = col
        not_check = checkrows(colnum,check[col],-1,0,not_check,check)
        if not_check == False:    
            if check[col]==8:
                check[col]=0
                col-=1
                while(check[col]==8):
                    check[col]=0
                    col-=1
        else:
            col+=1
    return check

print(search_queens())
#https://lichess.org/editor/2Q5/5Q2/3Q4/1Q6/7Q/4Q3/6Q1/Q7_w_-_-_0_1