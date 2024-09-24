if __name__ == '__main__':
    print("Enter elements of 1st array:")
    arr_one = list(map(int,input().split()))
    print("Enter elements of 2nd array:")
    arr_two = list(map(int,input().split()))
    a = arr_one + arr_two
    print("Merged list is:")
    a.sort()
    print(*a)