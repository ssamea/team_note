# 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작
# 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당

def distance(a,b):
    # 키패드는 1부터 시작하지만 여기서는 리스트 이기떄문에 인덱스가 0부터 시작한다 그래서 키패드 1 의 인덱스는 0 이므로
    # 아래 숫자들의 인덱스를 따로 저장하는거임
    if a == '*':
        num1 = 9
    elif a == 0:
        num1 = 10
    elif a == '#':
        num1 = 11
    else: num1 = a-1


    if b == 0:
        num2 = 10
    else: num2 = b-1

    return abs(num1//3-num2//3)+abs(num1%3-num2%3)

def solution(numbers, hand):
    answer = ''
    if hand == "left":
        h = 'L'
    else:
        h = 'R'
    left = "*"
    right = "#"

    for i in numbers:
        # 1, 4, 7 은 왼손만 사용
        if i % 3 == 1:
            answer += "L"
            left = i

        # 3, 6, 9는 오른손만 사용
        elif i != 0 and i % 3 == 0:
            answer += "R"
            right = i

        # 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용
        else:
            # 왼쪽이 더 가깝다면
            if distance(left, i) < distance(right, i):
                answer += "L"
                left = i

            # 오른쪽이 가깝다면
            elif distance(left, i) > distance(right, i):
                answer += "R"
                right = i

            # 거리가 같다면 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용
            else:
                answer += h
                if h == "L":
                    left = i

                else:
                    right = i


    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))