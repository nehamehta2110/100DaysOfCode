def check_balance(x, Y):
    if Y>=0 and Y<2000 and x!=0 and x<Y: 
        if x%5==0 and Y>x+0.50:
                return round(Y-x-0.50, 2)
    return Y
    
if __name__=='__main__':
    x = int(input())
    Y = float(input())
    print(check_balance(x,Y))