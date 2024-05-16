import heapq

def min_cost(cables):
    # Перетворення списку кабелів на min купу
    heapq.heapify(cables)
    total_cost = 0
    
    while len(cables) >1:
        #беремо 2 найменші кабелі
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)
        
        cost = a + b
        total_cost += cost

        heapq.heappush(cables, cost)
    
    return total_cost

cables = [6, 1, 2, 8]
print(min_cost(cables))