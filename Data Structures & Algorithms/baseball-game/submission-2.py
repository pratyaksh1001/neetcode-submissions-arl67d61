class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        c=[]
        t=0


        for i in operations:
            if i.isdigit() or '-' in i:
                s.append(int(i))
                print(s)
            elif i=='+':
                s.append(s[-1]+s[-2])
            elif i=='D':
                s.append(s[-1]*2)
            else:
                s.pop()
        
        return sum(s)

