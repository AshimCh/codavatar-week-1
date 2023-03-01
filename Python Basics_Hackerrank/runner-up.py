if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    largest = max(arr)
    for i in range(arr.count(largest)):
        arr.remove(largest)
    secondmax = max(arr)
    print(secondmax)