import math
# s="*"
# N=20
# i=1
# for i in range (N):
#     if(i<=(N/2)): print(f"{i}:\t {s*(i)}")
#     else: print(f"{i}:\t {s*(N-i)}")
#     
# print("\nend")

def stars(N,s):
    """Print arrow of symbols
        bla bla"""
    for i in range (N):
        if(i<=(N/2)): print(f"{i}:\t {s*(i)}")
        else: print(f"{i}:\t {s*(N-i)}")
        
#printing some symbol arrows
stars(20,">")
stars(15,"<")

#Solving quadratic equation
def quadrat_solve(a,b,c):
    return ((b**2)-math.sqrt(4*a*c))/2,((b**2)+math.sqrt(4*a*c))/2


x1,x2=quadrat_solve(1,4,4)
print(f"x1: {x1} \nx2: {x2}")

#calculating factorial
def fact(num):
    sum=1
    for i in range (num):
        sum*=(i+1)
    return sum

print(fact(5))
    