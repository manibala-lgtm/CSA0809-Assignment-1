from decimal import Decimal

entries = [
    ("F001", Decimal("10"), Decimal("3.5"), Decimal("8.5"), "Morning"),
    ("F002", Decimal("8.5"), Decimal("4.2"), Decimal("8.7"), "Evening"),
]

print("Farmer Delivery Records")
print("-----------------------")

for entry in entries:
    farmer_id, litres, fat, snf, shift = entry

    print("Farmer ID:", farmer_id)
    print("Litres:", litres)
    print("Fat:", fat)
    print("SNF:", snf)
    print("Shift:", shift)
    print()
