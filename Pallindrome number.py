n=121
original=n
rev=0
for i in str(n):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if rev==original:
    print("Pallindrome number")
else:
    print("Not a Pallindrome number")
