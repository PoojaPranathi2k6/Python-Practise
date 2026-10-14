n=153
original=n
sum=0
for i in "n":
    digit=n%10
    sum=sum+digit**3
    n=n//10
print(sum)
print(original)
if sum==original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

    
# ANOTHER METHOD

n=153
original=n
s=n
count=0
sum=0
for i in "s":
    digit=s%10
    count=count+1
    s=s//10
print(count)
for i in "n":
    digit=n%10
    sum=sum+digit**count
    n=n//10
print(sum)
print(original)
if sum==original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

