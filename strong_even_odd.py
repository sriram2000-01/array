n=int(input())
odd_count=0
even_count=0
digit_count=0
while n:
    r=n%10
    n=n//10
    digit_count+=1
    if(r%2==0):
        even_count+=1
    else:
        odd_count+=1
if(even_count==digit_count):
    print("strong even")
elif(odd_count==digit_count):
    print("strong odd")
else:
    print("mixed")
