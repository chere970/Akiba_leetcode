class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        n=int(input("Enter your number: "))
        
        if n%2==0:
         multiple=n
        else:
            multiple=n*2
        return multiple
sol=Solution()

result=sol.smallestEvenMultiple(3)
print(f"smallest even multiple={result}")
        
        