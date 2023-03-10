import sys, time
start_time = time.time()
sys.stdin = open("input.txt", "r")

import heapq, sys
heap = []
heapq.heapify(heap)
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    i = int(input())
    if i == 0:
        if len(heap) < 1:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -i)


end_time = time.time()
print("\nTime:", round(end_time - start_time, 5))