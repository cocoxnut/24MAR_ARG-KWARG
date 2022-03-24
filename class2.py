sentence = 'Simple is better than complex'
def count_letters(sentence):
    count = 0
    for letters in sentence:
        count += 1
    return count
print(count_letters(sentence))