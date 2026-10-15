n=9
s=n*n
sum=0
for i in str(s) :
        digit=s%10
        sum=sum+digit
        s=s//10
print(sum)    
print(n)
if sum==n:
    print("Neon number")
else:
    print("Not a Neon number")




