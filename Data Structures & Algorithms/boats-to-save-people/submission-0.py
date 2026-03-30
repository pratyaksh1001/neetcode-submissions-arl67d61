class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people=sorted(people)

        n=len(people)

        i=0
        j=n-1
        c=0
        while i<=j:
            if people[i]+people[j]<=limit:
                c+=1
                i+=1
                j-=1
            elif people[j]<=limit:
                j-=1
                c+=1
        return c