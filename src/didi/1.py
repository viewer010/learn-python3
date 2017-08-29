#coding = utf-8
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        line = sys.stdin.readline().strip()
        values=list(map(int, line.split()))
        print(values)
        sum=0
        tp=0
        for value in values:
            tp+=value
            if tp>sum:
                sum=tp
            elif tp < 0:
                tp=0
        print(sum)