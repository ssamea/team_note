# 특정 단어 추출: 어떤 단어를 제외한 문자열 중에서 특정 단어 추출하기
# 단, 대소문자는 구분하지 않고 구두점은 무시한다.
# Counter 객체는 아이템에 대한 개수를 딕셔너리로 리턴하여 준다. 개수를 자동으로 계산해 주기 때문에 매우 편리하다.
# most_common()을 사용하면 빈도 수가 가장 높은 요소를 추출 가능
import re
import collections

banned = 'hit'
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
# [^\w] 은 모든 문자와 숫자를 제외하고는 공백으로 바꾼다.
# 만약 제외할 단어 없이 한다면 if문 지우면 됨
words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
counts = collections.Counter(words)
print(counts.most_common()[0][0]) # 답