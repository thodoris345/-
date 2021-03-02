import random
n = int(input("Enter the Fibonacci term: "))


def Fibo(n):
    if n<0:
        print("Error:negative value")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fibo(n-1)+Fibo(n-2)

d = Fibo(n)

print("The value of the term is: ", d)
l = 0
if n == 0 or n == 1 or n == 2 or n == 3:
    print("ΤΟ",d, "ΔΕΝ ΕΙΝΑΙ ΠΡΩΤΟΣ")
else:
    for i in range(0, 20):

        c = random.randint(1, d-1)

        if (c ** (d-1) - 1) % d == 0:
            l += 1
    if l == 20:
        print("ΤΟ",d, "ΕΙΝΑΙ ΠΡΩΤΟΣ")
    else:
        print("ΤΟ",d, "ΔΕΝ ΕΙΝΑΙ ΠΡΩΤΟΣ")
