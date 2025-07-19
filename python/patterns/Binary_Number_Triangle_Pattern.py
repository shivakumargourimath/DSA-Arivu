'''
Given an integer N, print the following pattern : 
Input Format: N = 6
Result:   
1
01
101
0101
10101
010101
'''

def pat_11(n):
    for i in range(1,n+1):
        if i%2==1: start=1
        else: start=0
        for j in range(i):
            print(start,end="")
            start=1-start    #flip 0 & 1
        print()
        
pat_11(6)
