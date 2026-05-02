print("Welcome to the Calculatoor 0.1")
# a simple x by y calculator
def calculate(x, y, operator):
    # for /, //: if x was 0, no issue. If y was 0, there will be an issue. Experimenting with exception handling
    try:
        if operator == "+":
            result = x + y
        elif operator == "-":
            result = x - y
        elif operator == "*":
            result = x * y
        elif operator == "**":
            result = x ** y
        elif operator == "/":
            result = x / y
        elif operator == "//":
            result = x // y
        else:
            result = "Invalid operator / not in operator list"
        return result
    except ZeroDivisionError:
        return "cannot divide by 0!"
def before_end():
    input("Input ENTER to end terminal")
    return
# seen people make a main function and calling it at the end. Seems to make it more readible
# it opens terminal for me if I open the .py file. before_end is a fix I see people do
def main():
    try:
        x = float(input("Input x: "))
        y = float(input("Input y: "))
    except ValueError:
        print("Not a number")
        before_end()
        return
    operator = input("Input operation (+, -, *, **, /, //): ").strip()
    print(calculate(x, y, operator))
    before_end()

main()
