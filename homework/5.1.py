#程序占用空间较大，只考虑了两个数相组合的情况，如果需要进行更多组合，可做以下更改,更多同理。
#考虑三数组合：
#list=[1,-1,10,-10,100,-100]
#for x in range(0,8):
    #if ans[x]=100:
        #ans[x+1]=10
        #ans[x+2]=1
    #if ans[x]=-100:
        #ans[x+1]=-10
        #ans[x+2]=-1
#for x in range(0,9)
    #if ans[x]=10:
        #ans[x+1]=1
    #if ans[x]=-10:
        #ans[x]=-1
def find_expression(k):
    #k=input("input the number between 1 and 100:")
    list=(1,-1,10,-10)
    list_1=(1,-1)
    for a in list:
        for b in list:
            for c in list:
                for d in list:
                    for e in list:
                        for f in list:
                            for g in list:
                                for h in list:
                                    for i in list_1:
                                        ans=[a,b,c,d,e,f,g,h,i]#a到i分别是9-1的系数
                                        #print(ans)
                                        for x in range(0,9):#保证前一项系数为+-10时，后一项系数为+-1，这样就将两个相邻数字组合成两位数。
                                                if ans[x]==10:
                                                    ans[x+1]=1
                                                if ans[x]==-10:
                                                    ans[x+1]=-1
                                        #print(ans)
                                        if ans[0]*9+ans[1]*8+ans[2]*7+ans[3]*6+ans[4]*5+ans[5]*4+ans[6]*3+ans[7]*2+ans[8]*1==k:
                                                print(ans)
k=int(input("input the number between 1 and 100:"))
print("the coeffcients are:")                                               
find_expression(k)   