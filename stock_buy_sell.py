# Reference link for the problem
# https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0
strg="6764 3645 5181 5893 4542 6753 3996 5483 585 9895 2657 777 1343 4605 261 2225 959 9884 563 4131 6687 7528 6224 436 3333 110 2037 7007 4710 2310 7596 7827 2307 9129 72 3202 2234 4069 5037 2819 3964 7694 9948 5307 8652 6561 7532 9611 6445 8095 94 9484 1975 6319 9920 5308 6429 1958 8668 7491 620 6264 5318 2927 1745 5391 6129 3979 5812 1167 3150 9776 8861 3098 5083 3865 9659 8968 3476 6104 3415 9923 1940 1743 6242 1861 3403 9023 3819"
s = strg.split(" ")
a= []
for e in s:
    a.append(int(e))
start = 0
cur = start
nxt = start+1
ln = len(a)-1
out=[]
class stock:
    # created the objects to store the buy and sell values
    buy=0
    sell=0
    def __init__(self,buy,sell):
        # constructer used to store the object properties[buy,sell] when object is created
        # It can only be called by once when object is created
        self.buy = buy
        self.sell = sell
# solutin -1
def checkForProfit(start,cur,nxt):
    if(nxt>ln):
        if(a[start]<a[cur]):
            out.append(stock(start, cur))
        return
    if a[cur]<a[nxt]:
        cur=cur+1
        nxt=cur+1
        # recursive method to call checkForProfit
        checkForProfit(start,cur,nxt)
    else:
        if start!=cur:
            out.append(stock(start,cur))
        start=nxt
        cur = start
        nxt = start + 1
        checkForProfit(start,cur,nxt)
    return

checkForProfit(start,cur,nxt)
for st in out:
    print ("("+str(st.buy)+","+str(st.sell)+")")



#  optimal solution-2
for index in range(1,ln):
    if a[index]>a[index-1]:
        pass
    else:
        if start!=index-1:
            out.append(stock(start,index-1))
        start=index
for st in out:
    print ("("+str(st.buy)+","+str(st.sell)+")")
