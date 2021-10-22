def countwords(file):
    f = open(file, "r")
    print(f)
    words = 0
    for x in f:
        word = x.split()
        for x in word:
            words = words + 1
    print(words)

filename = input("Enter file name: ")
countwords(filename)
