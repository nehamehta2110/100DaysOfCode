#User function Template for python3

class Solution:
	def quadraticRoots(self, a, b, c):
        x1 = (-b + (b**2 - 4*a*c)**0.5)//2*a*c
        x2 = (-b - (b**2 - 4*a*c)**0.5)//2*a*c
        return [x1, x2]


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