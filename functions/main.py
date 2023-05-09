# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))

def add(a, b, c):
    return a + b + c

print(add(5, 3, 2))

def positive(n):
    if n > 0:
        return True
    elif n <= 0:
        return False
    
print(positive(50))
print(positive(-50))
print(positive(0))

def negative(n):
    if n >= 0:
        return False
    elif n < 0:
        return True

print(negative(50))
print(negative(-50))
print(negative(0))