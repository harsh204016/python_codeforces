


if __name__=="__main__":
    n = int(input())
    for _ in range(n):
        s = input()
        if s.count("N")==1:print("NO")
        #elif len(s)==2 : print("YES") if s[0]==s[-1] else print("NO")
        #elif len(s)%2!=0 : print("YES") if s[0]=="N" and s[-1]=="N" or s[0]=="E" and s[-1]=="E" else print("NO")
        else: print("YES")
