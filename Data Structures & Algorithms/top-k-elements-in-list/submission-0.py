class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        return [tuple[0] for tuple in counts.most_common(k)]
        
        