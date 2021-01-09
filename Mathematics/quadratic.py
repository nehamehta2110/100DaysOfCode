class Solution:
	def quadraticRoots(self, a, b, c):
            D = b**2 - 4*a*c
            if D < 0:
                return [-1]
            x1 = (-b + D**0.5)//2*a
            x2 = (-b - D**0.5)//2*a
            return [int(x1), int(x2)]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        ob = Solution()
        ans = ob.quadraticRoots(a,b,c)
        if len(ans)==1 and ans[0]==-1:
            print("Imaginary")
        else:
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print()

# } Driver Code Ends