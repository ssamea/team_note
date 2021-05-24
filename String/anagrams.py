# 애너그램: 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
import collections
data = ["eat","tea","tan","ate","nat","bat"]
sort_data = collections.defaultdict(list)
for word in data:
    sort_data[''.join(sorted(word))].append(word)
print(sort_data.values())