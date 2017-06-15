
" n is F(n) "
n = int(input("Please enter some number : "))


def prime(n):
    if(n == 2):
        return True
    else:
        for x in range(2,n):
            if (n%x != 0):
                return True
            
if n % 3 == 0:
    print("Buzz")
elif n % 5 == 0:
    print("Fizz")
elif n % 15 == 0:
    print("Fizzbuzz")
elif prime(n):
    print("BuzzFizz")
else:
    print("%d",n)
    
