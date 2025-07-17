#Given an integer N, print the following pattern : 
'''
Input Format: N = 6
Result:
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 
'''

def pat5(n):
    for i in range(n,-1,-1):
        for j in range(i):
            print("*",end="")
        print()
        
pat5(6)
