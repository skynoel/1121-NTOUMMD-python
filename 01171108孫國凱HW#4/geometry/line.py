def lengthOfPoints(x1,y1,x2,y2): # 回傳兩點間之距離
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def slope(x1,y1,x2,y2): # 計算並回傳兩點斜率
    return(y2-y1)/(x2-x1)