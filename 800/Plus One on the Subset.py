n = int(input())
i=0
while(i<n):
    count = int(input())
    l = list(map(int,input().split()))
    l.sort()
    ma= l[-1]
    mi =l[0]
    print(ma-mi)
    i+=1