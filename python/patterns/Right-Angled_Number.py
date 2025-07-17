#Given an integer N, print the following pattern :
'''
Input Format: N = 6
Result:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
'''

def pat3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
        
pat3(6)
