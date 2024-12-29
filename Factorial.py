Num = int(input("Enter a Number: "))

factorial = 1
for i in range(Num,0,-1):
    factorial *= i

print("Factorial of",Num,"is:",factorial)
