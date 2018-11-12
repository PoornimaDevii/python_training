# Exception Handling

while True:
    try:
        x = int(input("Please enter a number:"))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again....")

print(dir(__builtins__))
print(__builtins__.ImportError.__doc__)