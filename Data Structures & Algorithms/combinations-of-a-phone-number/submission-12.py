class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m={1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        n=len(digits)

        result=[]
        def helper(res,curr):
            if curr==n:
                result.append(res)
                return
            for i in m[int(digits[curr])]:
                helper(res+i,curr+1)
        helper("",0)
        if "" in result:
            result.remove("")
        return result