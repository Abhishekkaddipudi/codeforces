import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

def Result(confidence):
    co=0
    for i in confidence:
       if i.count(1)>1:
        co+=1
    return co





if __name__=="__main__":
    n=int(input())
    confidence=[]
    first,second,third=0,0,0
    for i in range(n):
        confidence.append(list(map(int,input().split())))
    res=Result(confidence)
    print(res)
    
