#python program to find whether the number is palindrome or not\
n=int(input("ENTER ANY NUMBER"))
org=n
rev=0
while(n!=0):
    digit=n%10
    rev=digit+rev*10
    n=n//10
if (rev==org):
    print("IT IS A PALINDROME")
else:
    print("THE IS NOT A PALINDROME")

#python program to find sum and average of n numbers
print("PRINT VALUE FOR N=")
n=int(input())
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
avg=sum/n
print("The sum of n numbers=",sum)
print("The average of N numbers=",avg)


#python program to find whether the person is eligible for voting or no
n=int(input("ENTER AGE "))
if (n>=18):
    print("HE IS ELIGIBLE")
else:
    print("HE IS NOT ELIGIBLE")
    
