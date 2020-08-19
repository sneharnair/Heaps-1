# APPROACH 1: MIN HEAP (OPTIMAL)
# Time Complexity : O(n lg k), n: len(nums), k: size of heap - lg k for heapify op
# Space Complexity : O(k), size of min heap
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. Use min heap of size k
# 2. For each element in nums, add to heap. If size exceeds, pop out (least element gets removed)
# 3. Thus, we store k largest elements in heap. Return the root of heap (k th largest)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums is None:
            return None
        
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        return min_heap[0]
        

# APPROACH 2:  MIN HEAP
# Time Complexity : O(n lg k), n: len(nums), k: size of heap - lg k for heapify op
# Space Complexity : O(k), size of min heap
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. Use min heap of size k
# 2. Keep adding elements of num to heap till size of heap becomes k.
# 3. When size of heap is k, if the new element is less than the root of heap -> IGNORE
#                             if the new element is greater than the root of the heap -> pop from the heap and push this new element to heap

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums is None:
            return None
        
        min_heap = []
        for num in nums:
            
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
                continue
            
            elif num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
                
        return min_heap[0]
        

# APPROACH 3: MAX HEAP
# Time Complexity : O(n lg (n - k)), n: len(nums), k: size of heap - lg n - k for heapify op
# Space Complexity : O(k), size of min heap
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None ( To use max heap in python, negate all the elements then call heapq as heapq by default only implements min heap).
#
#
# Your code here along with comments explaining your approach
# 1. Use max heap of size n - k. Here we store n - k smallest elements in max heap
# 2. For each element of nums, push to heap. If size of heap exceeds n - k, then pop and keep track of the minimum of popped elements. 
# 3. At the end, we return this minimum we kept trackof. (again negate to get the original value). 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums is None:
            return None
        
        min_heap, result = [], float('inf')
        for num in nums:
            
            heapq.heappush(min_heap, -1 * num)
            
            if len(min_heap) > len(nums) - k:
                pop = heapq.heappop(min_heap)
                result = min(result, -1 * pop)
                
                
        return result
        
