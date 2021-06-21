# 어떤 과학자가 발표한 논문 n편 중,
# h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다

def solution(citations):
    answer = 0
    citations.sort(reverse=True) # 먼저 f 값을 가장 큰 값에서 가장 낮은 값으로 정렬

    citations.insert(0,0)
 #   print(citations)

    for i in range(1, len(citations)):
        if i == citations[i]:
            answer = i
            break

        if i >= citations[i]:
            answer = i-1
            break

        else:
            answer=i

    #print(h_index)
    return answer


citations = [10,50,100]
print(solution(citations))