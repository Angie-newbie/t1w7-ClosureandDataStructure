#  Closure
#  A function that returns another function

# 

def greet(name):
    print("Hello")

    def display_name():
        print(name)
    return display_name

spam = greet("John")
print(type(spam))

spam()