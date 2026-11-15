from decimal import Decimal
from time import perf_counter

def run_test(n):
    items = ["33.40"] * n

    start = perf_counter()

    float_total = 0.0
    for value in items:
        float_total += float(value)

    float_time = perf_counter() - start

    start = perf_counter()

    decimal_total = Decimal("0.00")
    for value in items:
        decimal_total += Decimal(value)

    decimal_time = perf_counter() - start

    print("\nNumber of Entries:", n)
    print("Float Total:", float_total)
    print("Decimal Total:", decimal_total)
    print("Float Time:", float_time, "seconds")
    print("Decimal Time:", decimal_time, "seconds")

for count in (300, 6000, 150000):
    run_test(count)
