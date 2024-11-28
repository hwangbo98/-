from collections import deque

def find_min_time(N, K):
    # 방문 여부를 체크하기 위한 set
    # (위치, 속도)를 저장
    visited = set()
    
    # BFS를 위한 큐
    # (위치, 속도, 시간)을 저장
    queue = deque([(1, 0, 0)])  # 시작 위치 1, 초기 속도 0, 시간 0
    visited.add((1, 0))
    
    while queue:
        pos, speed, time = queue.popleft()
        
        # 목표 위치에 도달했고 속도가 0이면 종료
        if pos == N and speed == 0:
            return time
            
        # 가능한 모든 속도 변화를 시도
        # K감소, K-1감소, 유지, K-1증가, K증가
        for speed_change in [-K, -(K-1), 0, K-1, K]:
            new_speed = speed + speed_change
            new_pos = pos + new_speed
            
            # 유효한 상태인지 확인
            # 1. 위치가 1과 N 사이여야 함
            # 2. 방문하지 않은 상태여야 함
            if 1 <= new_pos <= N and (new_pos, new_speed) not in visited:
                visited.add((new_pos, new_speed))
                queue.append((new_pos, new_speed, time + 1))
    
    return -1  # 불가능한 경우

# 예시 테스트
N, K = 9, 2
result = find_min_time(N, K)
print(f"최소 시간: {result-1}")