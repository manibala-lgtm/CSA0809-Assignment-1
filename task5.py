from decimal import Decimal, InvalidOperation

def read_decimal(prompt):
    while True:
        text = input(prompt).strip()

        try:
            value = Decimal(text)

            if not value.is_finite():
                raise ValueError

            return value

        except (InvalidOperation, ValueError):
            print("Invalid number. Example: 8.5")

amount = read_decimal("Enter payment amount: ")

print(f"Amount: Rs {amount:8.2f}")
