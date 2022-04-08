class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = {}
        for pos in range(len(numbers)):
            if target-numbers[pos] in hash:
                return [hash[target-numbers[pos]]+1, pos+1]
            else:
                hash[numbers[pos]] = pos