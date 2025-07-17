#Given an integer N, print the following pattern : 
'''
Input Format: N = 6
Result:     
***********
 *********
  *******
   ***** 
    ***    
     *
'''

def pat8(n):
    for i in range(n,-1,-1):  #loop from 6 to 1
        for j in range(n-i-1):  #add a space 
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()
        
pat8(6)

'''
how loop runs

| i | n - i - 1 | Explanation                                    | print("*")
| - | --------- | ---------------------------------------------- |
| 6 | -1        | ❌ **Invalid range** —`range(-1)` does nothing |
| 5 | 0         | `range(0)` → no spaces                         |  2*5+1=11
| 4 | 1         | `range(1)` → 1 space                           |  2*4+1=9
| 3 | 2         | `range(2)` → 2 spaces                          |  2*3+1=7
| 2 | 3         | `range(3)` → 3 spaces                          |  2*2+1=5
| 1 | 4         | `range(4)` → 4 spaces                          |  2*1+1=3
| 0 | 5         | `range(5)` → 5 spaces                          |  2*0+1=1

'''
