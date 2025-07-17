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
'''

def pat7(n):
    for i in range(n):
        for j in range(n-i-1): #give space at the begining 
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()
        
pat7(6)

#or can use concatination method
def pat7(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    print()
        
pat7(6)
