class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        n=len(position)
        cars = sorted(zip(position, speed))
        for i in range(n):
            position[i]=cars[i][0]
            speed[i]=cars[i][1]
        c=1
        curr=(target-position[-1])/speed[-1]
        for i in range(n-2,-1,-1):
            d=target-position[i]
            t=d/speed[i]
            if t<=curr:
                continue
            else:
                c+=1
                curr=(target-position[i])/speed[i]
        return c
            