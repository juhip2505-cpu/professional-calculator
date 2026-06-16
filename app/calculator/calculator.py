from app.calculation.calculation import CalculationFactory


class Calculator:
    def __init__(self):
        self.history = []

    def show_help(self):
        print("\nAvailable commands:")
        print("add")
        print("subtract")
        print("multiply")
        print("divide")
        print("history")
        print("help")
        print("exit")

    def show_history(self):
        if not self.history:
            print("No calculations yet.")
            return

        for item in self.history:
            print(item)

    def run(self):
        print("Professional Calculator")
        print("Type 'help' for commands.")

        while True:
            command = input("\nEnter command: ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break

            if command == "help":
                self.show_help()
                continue

            if command == "history":
                self.show_history()
                continue

            # LBYL
            if command not in ["add", "subtract", "multiply", "divide"]:
                print("Invalid command.")
                continue

            try:
                # EAFP
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                calculation = CalculationFactory.create_calculation(
                    command,
                    a,
                    b
                )

                result = calculation.perform()

                entry = f"{command}({a}, {b}) = {result}"
                self.history.append(entry)

                print(f"Result: {result}")

            except ValueError:
                print("Invalid number entered.")

            except ZeroDivisionError:
                print("Cannot divide by zero.") 