#문자열 뒤집기
#투포인터를 이용한 방법

def reverseString(str):
    start, end = 0, len(str)-1 # 시작, 끝점의 위치 초기화
    while start < end:
        str[start], str[end] = str[end], str[start]
        start += 1
        end -= 1
    print(str)


a = ['a', 'b', 'c', 'd', 'e']
reverseString(a)