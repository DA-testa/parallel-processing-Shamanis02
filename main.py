# python3

def parallel_processing(n, m, data):
    output = []
    arr = [0] * n

    for i in range(0, m):
        arr.index(min(arr))
        output.append([arr.index(min(arr)),arr[arr.index(min(arr))]])
        arr[arr.index(min(arr))]+=data[i]

    return output

def main():

    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
