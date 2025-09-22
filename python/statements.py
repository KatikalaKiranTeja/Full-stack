"""money = 250
ticket_cost = 295

if(money>ticket_cost):
    print("go and watch the movie in theater")
else:
    print("scrool instagram")


# if , else in function
def sample(money, ticket_cost, user):
    if(money>ticket_cost):
        print(f"{user}go and watch the movie in theater")
    else:
        print(f"{user}scrool instagram")
sample(250,295,"Kiran")
#--------------------------------------------------------

def decide_feature(eamcet_result,student):
    if (eamcet_result):
        print(f"{student} can join in btech college")
    else:
        print(f"{student} can join in degree college")
decide_feature(True,"Kiran")
decide_feature(False,"Vimal")
decide_feature(True,"Vamsi")

#--------------------------------------------------------
def checkEvenOdd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
checkEvenOdd(78)

#-------------------------------------------------------

num = 1547890
Id = num%10
if str(Id) in '04627':
    print("Even")
else:
    print("Odd")

#-------------------------------------------------------
def colleg(eamcet_rank):
    if (eamcet_rank < 25000):
        print("got seat in jntuh")
    elif(eamcet_rank < 50000):
        print("got seat in mallareddy ")
    elif(eamcet_rank < 75000):
        print("got seat in usha rama ")
    else:
        print("join in degree clg")
colleg(190000)"""
"""
def ipl():
    if (won_last_match or total_matches_won >=6):
        if (total_matches_woncccgcgcvccccccccccccccccccccccccgcggcg)
        if(net_run_rate >=0.75):

            print("team is entered into playoffs")
        else:
            print("team is disqualified due to low run rate")
    else:
        print("team should win more than 6 matches atleast to go to playoffs")
else:


"""

print("true statement") if not True else print("false statement")

username_matched=True
password_matched=True
print("login success")if username_matched and password_matched else print("login fail")

marks=45
grade='A' if marks>=55 else 'B'
print(grade)