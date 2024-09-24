import math
if __name__ == '__main__':
    print("Enter two natural numbers:")
    x,y = map(int,input().split())
    print("HCF : ", math.gcd(x,y))