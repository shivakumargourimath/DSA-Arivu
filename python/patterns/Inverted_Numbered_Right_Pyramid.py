#Given an integer N, print the following pattern : 
'''
Input Format: N = 6
Result:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1
'''

def pat6(n):
    for i in range(n,-1,-1):
        for j in range(1,i+1):
            print(j,end="")
        print()
        
pat6(6)
