# 문자열을 split()을 이용하여 알파벳 순으로 저장
data = ['1 A', '1 B', '6 A', '2 D', '4 B']

data.sort(key=lambda x: (x.split()[1], x.split()[0]))
print(data)