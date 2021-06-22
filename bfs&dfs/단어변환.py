# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다.
# 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
global answer


def dfs(begin, target, words, visit):
    answer = 0
    stacks = [begin]
    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer

        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != stack[j]]) == 1:
                if visit[i] != 0:
                    continue
                visit[i] = 1
                stacks.append(words[i])
        answer += 1
    return answer


def solution(begin, target, words):
    if target not in words:
        return 0
    visit = [0 for i in words]
    answer = dfs(begin, target, words, visit)
    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin,target,words))