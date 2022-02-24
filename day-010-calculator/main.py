from art import logo


def clear_console():
    print("\n" * 50)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def show_operations():
    list_of_symbols = ""
    for symbol in operations:
        list_of_symbols += f"{symbol} "
    list_of_symbols.rstrip()
    print(list_of_symbols)


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    show_operations()
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = round(calculation_function(num1, num2), 3)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear_console()
            calculator()


calculator()
