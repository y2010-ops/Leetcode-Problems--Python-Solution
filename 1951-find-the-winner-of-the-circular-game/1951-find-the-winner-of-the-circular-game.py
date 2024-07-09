class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Queue solution
        q = deque(range(1, n+1))

        while len(q) > 1:
            for i in range(k-1):
                q.append(q.popleft())
            
            q.popleft()
        
        return q[0]
        # # TC : O(N*K) which can be reduced as it is not good
        # # SC : O(N)
        # # without using queue
        # arr = [i for i in range(1,n+1)]
        # count = 1
        # index = 0
        # while len(arr) > 1:
        #     if count == k:
        #         arr.pop(index)
        #         count = 1
        #     else:
        #         index += 1
        #         count += 1
        #     if index >= len(arr):
        #         index = 0
        # return arr[0]
        