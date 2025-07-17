#Given an integer N, print the following pattern : 
'''
Input Format: N = 6
Result:
* 
* * 
* * *
* * * *
* * * * *
* * * * * *
'''

def pat2(n):
    for i in range(n):
        for j in range(i+1):
            print("* ",end="")
        print()
        
pat2(6)
