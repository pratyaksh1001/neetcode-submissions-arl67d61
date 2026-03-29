class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m={1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        l=[]
        n=len(digits)
        def helper(r,curr):
            if curr==n:
                l.append(r)
                return
            for i in m[int(digits[curr])]:
                
                helper(r+i,curr+1)
        helper("",0)
        try:
            l.remove("")
        except:
            pass
        return l
