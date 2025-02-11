words = ['apple', 'banana', 'kiwi', 'orange', 'grape']
n = 5
long_words = []
for word in words:
    if len(word) > n:
        long_words.append(word)
print(long_words)
