#dfs
# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다.
# 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.

def solution(begin, target, words):
    answer = 0  # Depth
    stacks = [begin]
    visited = {i: 0 for i in words}  # 이미 검사했던 단어를 다시 검사하지 않도록 하기 위한 딕셔너리
    if target not in words:
        return 0
    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer

        for word in words:
            for i in range(len(word)):
                copy = list(word)
                copy_front = list(stack)
                copy[i] = 0
                copy_front[i] = 0
                if copy == copy_front:
                    if visited[word] != 0:  # visited가 1이라면 이미 검사했던 단어므로 그냥 넘어간다.
                        continue
                    visited[word] = 1  # visited가 0이면 해당 단어의 visited 값을 1로 바꾼다.
                    stacks.append(word)
                    break
        answer += 1  # Depth 1추가

    return answer