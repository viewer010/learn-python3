#coding=utf-8
import sys
if __name__=="__main__":
    line1=sys.stdin.readline().strip()
    values1=list(map(int,line1.split()))
    line2=sys.stdin.readline().strip()
    value2=int(line2)
    # print(values1,value2)
    values1.sort()
    print(values1)
    print(values1[value2])

    