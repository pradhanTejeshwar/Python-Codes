def apple_share(N,appls):
    goal = sum(appls)/N
    rounds=0
    while len(set(appls)) > 1 :
        rounds += 1
        i=0
        for i,x in enumerate(appls):
            if x <= goal:
                continue
            elif i not in [0,N-1]:
                if appls[i+1] <= goal:
                    appls[i+1] += 1
                    appls[i] -= 1
                elif appls[i-1] <= goal:
                    appls[i-1] += 1
                    appls[i] -= 1
                break
                    
            elif i == 0:
                if appls[i+1] <= goal:
                    appls[i+1] += 1
                    appls[i] -= 1
                elif appls[N-1] <= goal:
                    appls[N-1] += 1
                    appls[i] -= 1
                break
                    
            elif i == N-1:
                if appls[0] <= goal:
                    appls[0] += 1
                    appls[i] -= 1
                elif appls[i-1] <= goal:
                    appls[i-1] += 1
                    appls[i] -= 1 
                break
        print(appls)
            
    print(f"Number of Rounds : {rounds}")

if __name__ == '__main__':
    N=0 
    while N < 2:
        N = int(input('Enter No. of boys :'))
    appls={}
    while len(appls) != N:
        appls= [int(x) for x in (input("Enter number of apples each boys have (Separated by space) : ").split())]
    if sum(appls) % N  != 0:
        print("Number of Total apples should be equaly divisable by no of boys")
    else:
        apple_share(N,appls)