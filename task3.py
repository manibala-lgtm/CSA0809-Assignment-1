from decimal import Decimal

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

litres = Decimal("10.0")
farmer_id = "F001"

print("Farmer ID:", farmer_id)
print("Litres:", litres)
print("Base Rate:", BASE_RATE)
print("Fat Step Value:", FAT_STEP_VALUE)
print("SNF Step Value:", SNF_STEP_VALUE)

value = 10
value = "ten"

print("Changed Value:", value)

a, b = 5, 9
a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)

RATE_CARD = {
    "base": Decimal("30.00"),
    "fat": Decimal("0.40"),
    "snf": Decimal("0.30")
}

print("Rate Card:", RATE_CARD)
