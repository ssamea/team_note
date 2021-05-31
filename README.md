
## 유용한 함수들 정리
1) zip() 으로 앞 뒤값 비교하기
그동안은 c언어에서 하던 것 처럼 인덱스 값을 받아서 비교를 했는데, zip()을 이용해 다른 방법으로 표현할 수 있다는 것을 배웠다. 흠, 어떤 방법이 더 빠르고 효과적인지 비교해보고 싶은데, 어떻게 하면 좋을 지 고민해봐야 겠음

```
phone_book = [12,23,22] # phone_book[1:] = [23,22]

for p1, p2 in zip(phone_book, phone_book[1:]) :
	print(p1,p2)  
    
    # (12,23), (23,22)
 ```
 
2) str.startswith() : str[beg:end]에서 원하는 문자열 찾기

```
B.startswith(A,beg=0,end=len(string))
# B[beg:end]에서 strA 문자열 찾기!
 ```

startswith()은 내가 찾고자 하는 문자열A가 문자열B의 맨 앞에 있는지의 여부를 알려준다! 기본적으로는 문자열 B에 문자열 A 가 맨 앞 있다면 True를 반환하고, 아니라면 False를 반환한다.
```
B = 'abcdefg'
print(B.startswith('ab'))  # True
print(B.startswith('bcd')) # False 
# 찾고자 하는 문자열 'bcd'가 strB의 앞에 없음
 ```

(optional) 이때 beg과 end에 값을 줘서, B의 범위를 조절할 수 있다. 즉 strB[beg:end] 로 슬라이싱한 문자열의 맨 앞과 strA가 같은지 비교하면 된다!
```
strB = 'abcdefg'
print(strB.startswith('ab', 1))  # False
print(strB.startswith('bcd', 1)) # True
# strB[beg:end]
# strB[1:]은 'bcdefg'가 된다
```
