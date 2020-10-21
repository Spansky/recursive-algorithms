# Example 1 - For loop
res = 1
for i in range(1,5):
    res *= (i+1)
print(res) 

# Example 2 - While loop
res = 1
i = 5
while i>1:
    res = res * i
    i -= 1
print(res)

# Example 3 - Iterative Function
def factorial(number :int):
    res = 1
    for i in range(1,number):
        res *= (i+1)
    return res

print(factorial(5))

# Example 4 - Recursive Function
def factorial(number :int):
    if number < 2:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))
