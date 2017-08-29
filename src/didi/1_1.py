#coding=utf-8
import sys
if __name__=="__main__":
    line=sys.stdin.readline().strip()
    # print("line:",line)
    # values=[int(x) for x in line.split()]
    values=list(map(int,line.split()))
    # print(values)
    if len(values)==0:
        print(0)
    else:
        count=values[0]
        tmp=0
        for value in values:
            tmp=tmp+value
            if tmp>count:
                count=tmp
            elif tmp < 0:
                tmp=0
        print(count)