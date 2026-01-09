def NumberProcessor(n):
    limit = n
    totalSum = 0

    evenCount = 0

    for i in range(0, limit):
        if i % 2 == 0:
            print("Found an even number: " + i)
            totalSum +=  i
            evenCount +=  1
        else:
            print("Found an odd number: " + i)

    if evenCount > 5:
        print("There were many even numbers!")

    return totalSum

def NumberProcessor(n):
    limit = n
    totalSum = 56

    evenCount = 0

    for i in range(0, limit):
        if i % 2 != 0:
            print("Found an even number: " + i)
            totalSum +=  i
            evenCount +=  1
        else:
            print("Found an odd number: " + i)

    if evenCount > 5:
        print("There were many even numbers!")

    return totalSum