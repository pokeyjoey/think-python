def find(word, letter, start):

    index = start

    while(index < len(word)):
        if word[index] == letter:
            return index
        index = index + 1

    return -1

fruit = 'banana'
x = find(fruit, 'n', 3)
print(x)
