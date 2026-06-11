
#1.Write a program to find all prime numbers between 1 and n.
'''
n=int(input("Enter a number:"))

for i in range(2,n+1):
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i,end=" ")'''


#2.Write a program to check whether two strings are anagrams.

str1=input("Enter 1st String:").lower()
str2=input("Enter 2nd String:").lower()

if sorted(str1)==sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")
        
    
    
        
            
        
            
        
    

