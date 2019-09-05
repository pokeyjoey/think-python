def count_letter(word, letter):
    count = 0

    for character in word:
        if character == letter:
            count = count + 1
    
    return count
            

word = 'banana'
letter = 'n'
num = count_letter(word, letter)
print('{0} has {1} of the letter {2}'.format(word, num, letter))
