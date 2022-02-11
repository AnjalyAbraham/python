n=int(input("Enter the number:"))

 rev = 0
 temp = n
 while(temp>0):
 dig=temp%10
 rev=rev*10+dig
temp=temp//10
if(n==rev):
print("The number is palindrome")
else:
print("The number is not palindrome")

