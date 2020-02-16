def staircase(data):
    for n in range(1, data+1):
        print(" "*(data-n), end="")
        print("#"*(n))


value = input("Staircase Length: ")
staircase(value)
