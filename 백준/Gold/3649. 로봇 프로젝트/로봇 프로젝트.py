import sys
input=sys.stdin.readline


while True:
    try:
        x=int(input())
        T=int(input())
        L=[]

        for i in range(T):
            L.append(int(input()))
        L.sort()

        start=0 ; end=T-1 ; answer=-1 ; answer_list=[]

        while start<end:
            if L[start]+L[end]==x*10000000:

                if answer<abs(L[end]-L[start]):
                    answer_list=[L[start] , L[end]]
                    answer=abs(L[end]-L[start])
                start+=1

            elif L[start]+L[end]>x*10000000:
                end-=1
            else:
                start+=1

        if len(answer_list)!=0:
            print("yes %d %d"%(answer_list[0] , answer_list[1]))
        else:
            print('danger')
    except:
        break