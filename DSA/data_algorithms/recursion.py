# Recursion  = Function that calls itself from within (creates it's own loops)
#              Helps to visualise a complex problem into basic steps
#              Which can be solved more easily iteratively or recursively
#              iterative = faster, complex
#              recursive = slower, simpler


# ITERATIVE
def walk(steps):
    for step in range(1,steps+1):
        print(f"You take step #{step}")

# RECURSIVE
def walk(steps):
    if steps == 0:          # Prevent program from running forever
        return
    walk(steps - 1)
    print(f"You take step #{steps}")

#walk(100)


# FINDING FACTORIAL OF A NUMBER (Iterative & Recursive Methods)

# ITERATIVE
#def factorial(x):
#    result = 1
#    if x > 0:
#        for y in range(1,x+1):
#            result = result * y
#        return result

#print(factorial(10))


# RECURSIVE
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)       # Recursion calls it's own function, so it creates its own loop

print(factorial(10))