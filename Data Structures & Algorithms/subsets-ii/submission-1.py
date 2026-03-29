class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                     # Sort to group duplicates
        result = []

        def backtrack(start, path):
            result.append(path[:])      # Add current subset
            
            for i in range(start, len(nums)):
                # Skip duplicates at same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])    # Choose
                backtrack(i + 1, path)  # Explore
                path.pop()              # Backtrack
        
        backtrack(0, [])
        return result