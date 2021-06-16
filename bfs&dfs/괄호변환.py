# '(' 의 개수와 ')' 의 개수가 같다면 => 균형잡힌 괄호 문자열
#  '('와 ')'의 괄호의 짝도 모두 맞을 경우 => 이를 올바른 괄호 문자열


def balanced_index(p):  # 균형잡힌 괄호의 인덱스를 반환하는 함수
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            return i


# 올바른 괄호인지 판단
def check(p):
    cnt = 0  #왼쪽 괄호 개수
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True


def solution(p):
    answer = ''
    if p == '':  # 빈 문자열인 경우
        return answer  # 빈 문자열을 반환

    idx = balanced_index(p)
    # 빈 문자열이 아니면 u, v로 분리한다.
    u = p[:idx + 1]
    v = p[idx+1:]

    #  u가 "올바른 괄호 문자열"이면 v에 대해 함수를 수행
    if check(u):
        answer = u+solution(v)  # 수행한 결과 문자열을 u에 이어 붙인 후 반환

    # 문자열 u가 "올바른 괄호 문자열"이 아니라면
    else:
        answer += '('  # 빈 문자열에 첫 번째 문자로 '('를 붙임
        answer += solution(v)  # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        answer += ')'  # ')'를 다시 붙입니다.
        u = list(u[1:-1])  # u의 첫 번째와 마지막 문자를 제거하고

        # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)

    return answer


p = "(()())()"
print(solution(p))