class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        h = sum(weights)

        while l < h:

            mid = (l + h) // 2

            days_used = 1
            current = 0

            for w in weights:

                if current + w <= mid:
                    current += w
                else:
                    days_used += 1
                    current = w

            if days_used <= days:
                h = mid
            else:
                l = mid + 1

        return l