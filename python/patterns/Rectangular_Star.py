#Given an integer N, print the following pattern.
'''
Input: N = 6
Output:
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
'''

def pat1(n):
    for i in range(n):
        for j in range(n):
            print("* ",end="")
        print()
      
pat1(6)
