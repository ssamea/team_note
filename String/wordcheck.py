import functools
words = ["dog","dog","a","cat","cat","b"]
words_count={}

def comparator(x, y):
    return x[0] * x[1] - y[0] * y[1]

for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

sorted_words = sorted([(k, v) for k, v in words_count.items()], key=lambda word_count: -word_count[1]) # key = functools.cmp_to_key(comparator)
print([w[0] for w in sorted_words])
print(sorted_words[0]) # sorted_words[0][0] -> dog만 출력
