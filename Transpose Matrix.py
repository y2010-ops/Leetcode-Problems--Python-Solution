class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [e for e in zip(*matrix)]