# PERFECT NUMBER

n=6
i=1
sum=0
while i < n:
    if n%i == 0:
        sum=sum+i
    i=i+1
if sum == n:
    print("Perfect number")
else:
    print("Not  a  Perfect number")


# NOT A PERFECT NUMBER

n=21
i=1
sum=0
while i < n:
    if n%i == 0:
        sum=sum+i
    i=i+1
if sum == n:
    print("Perfect number")
else:
    print("Not  a  Perfect number")




