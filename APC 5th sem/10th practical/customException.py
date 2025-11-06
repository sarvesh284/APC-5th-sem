class MyCustomError(Exception):

    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
a=int(input("Enter a:"))
b=int(input("Enter b:"))
def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed", 400)
    else:
        print(a/b)
    return a / b


try:
    result = divide(a,b)
except MyCustomError as e:
    print(e)
    print(f"Error code: {e.error_code}")