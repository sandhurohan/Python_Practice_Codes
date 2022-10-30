# Decorators are used to modify functionality of function.

def decorator(message):
    def nowexecute():
        print("Executing Function Now")
        message()
        print("Executed")
    return nowexecute

def message():
    print("I Love Decorator")

message=decorator(message)

message()