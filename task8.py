from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_VALUE = Decimal("0.40")
SNF_VALUE = Decimal("0.30")

def calculate_payment(farmer_id, litres, fat, snf, shift):
    if not farmer_id.strip() or not shift.strip():
        raise ValueError("Invalid identity")

    litres = Decimal(litres)
    fat = Decimal(fat)
    snf = Decimal(snf)

    if not all(x.is_finite() for x in (litres, fat, snf)):
        raise ValueError("Invalid numeric value")

    if litres <= 0:
        raise ValueError("Invalid quantity")

    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Invalid fat")

    if not Decimal("6.0") <= snf <= Decimal("10.0"):
        raise ValueError("Invalid SNF")

    fat_steps = int(
        ((fat - Decimal("3.5")) / Decimal("0.1")).quantize(
            Decimal("1"), rounding=ROUND_HALF_UP
        )
    )

    snf_steps = int(
        ((snf - Decimal("8.5")) / Decimal("0.1")).quantize(
            Decimal("1"), rounding=ROUND_HALF_UP
        )
    )

    rate = BASE_RATE + fat_steps * FAT_VALUE + snf_steps * SNF_VALUE
    payment = (litres * rate).quantize(Decimal("0.01"))

    return rate, payment

try:
    rate, payment = calculate_payment(
        "F001", "10", "3.5", "8.5", "Morning"
    )

    print("Rate per Litre: Rs", rate)
    print("Payment: Rs", payment)

except ValueError as error:
    print("Error:", error)
