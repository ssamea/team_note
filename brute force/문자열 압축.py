def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):  # i개 만큼 잘랐을 때 문자열 길이를 비교
        arr = s[0:i]  # i 개의 단위 만큼 문자열을 자름
        cnt = 1
        res = ""

        # i개 단위 만큼 증가 시켜서 나머지 뒤 문자열을 비교
        for j in range(i, len(s), i):  # i=4 니까 4부터 s 끝까지
            if arr == s[j:j + i]:
                cnt += 1

            # 압축 못할 경우
            else:
                res += str(cnt) + arr if cnt >= 2 else arr
                arr = s[j:j + i]  # 초기화
                cnt = 1  # 초기화

        # 남아있는 문자열 처리
        res += str(cnt) + arr if cnt >= 2 else arr

        answer = min(answer, len(res))

    return answer