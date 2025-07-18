#Given an integer N, print the following pattern : 
'''
Input Format: N = 6
Result:   
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *
'''

def pat9(n):
    for i in range(n):
        print(" "*(n-i-1) + "*"*(2*i+1))
    for i in range(n,-1,-1):
        print(" "*(n-i-1) + "*"*(2*i+1))
        
pat9(6)
