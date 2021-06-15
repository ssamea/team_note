# 실패율
def solution(n, stages):
    fail_rate = {}
    answer = []
    stages.sort()  # [1, 2, 2, 2, 3, 3, 4, 6] => 현재 도전 중인 스테이지의 번호
    people = len(stages) # 사람 수

    # 스테이지별 실패율을 구한 후 answer에 삽입.
    for i in range(1, n+1):  # 스테이지는 1부터 있음
        if people!=0:
            fail_people = stages.count(i)  # 인원수 초기화
            fail_rate[i] = (stages.count(i) / people)  # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
            people -= fail_people  # 인원수 초기화
        else:
            fail_rate[i]=0

    return sorted(fail_rate, key=lambda x : fail_rate[x], reverse=True)


n = 4  # 전체 스테이지의 개수
stages =[4,4,4,4,4]  # 사용자가 현재 멈춰있는 스테이지의 번호(현재 도전 중인 스테이지의 번호)

print(solution(n, stages))