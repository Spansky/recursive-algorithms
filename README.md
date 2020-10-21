# Recursive Algorithms

This repository introduces the concept of recursion & recursive algorithms.

## Iterative Algorithms

Let's get started easily:
This algorithm uses a for loop to calculate the factorial of the number 5 --> 5! = 120

```python
res = 1
for i in range(1,5):
    res *= (i+1)
print(res) 
```

The algorithm can be broken down to:
5! = 1*2*3*4*5 = 120

But there are many different algorithms that lead to the same result:

```python
res = 1
i = 5
while i>1:
    res = res * i
    i -= 1
print(res)
```

For the purpose of reusing the factorial function we can define a function for it:

```python
def factorial(number :int):
    res = 1
    for i in range(1,5):
        res *= (i+1)
    return res

print(factorial(5))
```

However you realized this function. The approach that we have used was so far is called iterative. We use loops to go trough a certain method again and again.

## Recursive Algorithm

Another approach that I want to show you is using a different concept called recursion.

```python
def factorial(number :int):
    if number < 2:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))
```