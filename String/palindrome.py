# String 유형 : 회문 (Palindrome)
from collections import deque
def isPalindrome(a):
    q = deque()
    # 1. 전처리 과정: 입력 받은 문자열을 모두 소문자로 변환
    for i in s:
        if i.isalnum(): # 영문자, 숫자 여부를 판별하여, 영문자와 숫자가 아니면 False를 리턴
            q.append(i.lower())

    #회문 판별
    while len(q)>1:
        if q.popleft() != q.pop():
            print("회문이 아닙니다")
            return
    print("회문입니다")

s = input().split()
isPalindrome(s)

"""
가장 긴 팰린드롬 찾기

def palindrome(n, left, right):
    while right <= len(data) and left >= 0 and data[left] == data[right-1]:
        right += 1
        left -= 1
    return data[left + 1 : right -1]

data = 'ewqpbewqbfjabcdefedcbaienqnfkndkl'
res = ''
if data == data[::-1] or len(data) < 2:
    print(data)
else:
    for i in range(len(data)-1):
        res = max(res, palindrome(len(data), i, i+1), palindrome(len(data), i, i+2), key=len)
    print(res)

"""