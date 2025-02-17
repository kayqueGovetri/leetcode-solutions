from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Initialize the dictionary as a default int
        d = defaultdict(int)
        # Iterate over each number, retrieving the index and value
        for index, value in enumerate(nums):
            # If the value is in the dictionary and the absolute difference is less than or equal to k, return True
            if value in d and abs(value - d[value]) <= k:
                return True

            # Store the last index where this value was found in the dictionary
            d[value] = index

        return False
