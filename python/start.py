#print("hello world ?")
#a = int(input())
#b = int(input())
#print(a+b)
#print(a-b)
#print(a*b)

#n=int(input())
#for i in range(n):
 #   print( i**2)

#kiran=frozenset()
#print(type(kiran))

#memory Check: - 
# Assign the same value to 2 variables. 
#  Print their id() — are they same? 

#a=25
#b=25
#print(a!=b)

"""

class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if flag is False and ((a >= 0 and b < 0) or (a < 0 and b >= 0)):
            return True
        if flag is True and a < 0 and b < 0:    
            return True
        else:
            return False
            
            
sol=Solution()
print(sol.checkStatus(a=1,b=-1,flag=False))

def utility(a, b, opr):
    #code here
    if opr == 1:
        print(str(a + b), end=" ")
    elif opr == 2:
        print(str(a - b), end=" ")
    elif opr == 3:
        print(str(a * b), end=" ")
    else:
        print("Invalid Input", end=" ")

utility(2, 2, 2)"""
            
      
K=9      
room_num = [1,3,5,6,7,8,8,7,5,4,5,4,5,58,85,8,5,5]
unique_rooms=set(room_num)
total_sum_rooms=sum(room_num)
total_all_items=sum(unique_rooms)*K
captain_room=(total_all_items-total_sum_rooms)//(K-1)

print(captain_room)

