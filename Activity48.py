#Write a program to find the factorial using recursive function

def factorial(num1):
    if num1==0 or num1==1:
        return 1
    else:
        return num1*factorial(num1-1)
a = int(input('Enter a number please'))

if a<0:
    print('A factorial factor does not exist for a negative number.')
else:
    print(f"The factorial of {a} is {factorial(a)}")
