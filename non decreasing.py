import heapq

def smallest_range(nums):
    heap = [(row[0], i, 0) for i, row in enumerate(nums)]
    heapq.heapify(heap)
    
    max_num = max(row[0] for row in nums)
    min_range = float('inf')
    min_start, min_end = -1, -1
    
    while True:
        min_val, row_idx, col_idx = heapq.heappop(heap)
        if max_num - min_val < min_range:
            min_range = max_num - min_val
            min_start, min_end = min_val, max_num
        
        if col_idx == len(nums[row_idx]) - 1:
            break
        
        next_val = nums[row_idx][col_idx + 1]
        max_num = max(max_num, next_val)
        heapq.heappush(heap, (next_val, row_idx, col_idx + 1))
    
    return [min_start, min_end]
nums = [
    [4, 10, 15, 24, 26],
    [0, 9, 12, 20],
    [5, 18, 22, 30]
]

print("Smallest range:", smallest_range(nums))
