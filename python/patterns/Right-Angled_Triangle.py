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
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("* ",end="")
        print()
      
pat1(6)
