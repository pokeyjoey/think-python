def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2)-1

    while j > 0:
        if word1[i] != word2[j]:
            return False

        i = i + 1
        j = j -1

    return True

w1 = 'pots'
w2 = 'stop'

x = is_reverse(w1, w2)
if x:
    print('{0} is the reverse of {1}'.format(w1, w2))
else:
    print('{0} is not the reverse of {1}'.format(w1, w2))
