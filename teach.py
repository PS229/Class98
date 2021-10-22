def countwords():
    file = input("Enter file name: ")
    words = 0
    f = open(file)
    for line in f:
        word = line.split()
        words = words + len(word)
    print(words)

countwords()