
## 유용한 함수들 정리

1) zip() 으로 앞 뒤값 비교하기
 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 tuple 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환

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

3) for 반복문에 enumerate()
- 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
- 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.
```
t = [1, 5, 7, 33, 39, 52]
 for p in enumerate(t):
     print(p)
... 
(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)
```

-tuple형태 반환을 이용하여 아래처럼 활용 가능
```
for i, v in enumerate(t):
     print("index : {}, value: {}".format(i,v))
... 
index : 0, value: 1
index : 1, value: 5
index : 2, value: 7
index : 3, value: 33
index : 4, value: 39
index : 5, value: 52
```
