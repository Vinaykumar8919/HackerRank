if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=sorted(arr)
    arr=list(set(arr))
    arr=sorted(arr)
    print(arr[-2])