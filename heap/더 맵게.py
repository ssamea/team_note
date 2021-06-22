# 힙
# 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < k:
        new_s = heapq.heappop(scoville) + (2*heapq.heappop(scoville))
        #print(new_s)
        heapq.heappush(scoville,new_s)
        answer += 1

        if scoville[0] < k and len(scoville)==1:
            return -1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville,k))