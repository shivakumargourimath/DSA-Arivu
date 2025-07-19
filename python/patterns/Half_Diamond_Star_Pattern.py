#Given an integer N, print the following pattern : 
'''
Input Format: N = 6
Result:   
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *
'''

def pat_10(n):
    for i in range(1,n+1):  #loop from 1 to 6 where n+1=6+1=7 is exclusive 
        print((i)*"*"+"\n",end="")  #print i times *
    for i in range(n-1,-1,-1):   #loop reverse from n-1=5 to 1
        print((i)*"*"+"\n",end="")   #print i times *
        
pat_10(6)
