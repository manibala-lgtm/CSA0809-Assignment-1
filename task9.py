from decimal import Decimal, ROUND_HALF_UP
from collections import defaultdict

BASE = Decimal("30.00")
FAT_VALUE = Decimal("0.40")
SNF_VALUE = Decimal("0.30")
STEP = Decimal("0.1")
CENT = Decimal("0.01")

MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
MIN_SNF = Decimal("6.0")
MAX_SNF = Decimal("10.0")

def to_decimal(value):
    number = Decimal(str(value).strip())

    if not number.is_finite():
        raise ValueError("Number must be finite")

    return number

def validate_entry(farmer, litres, fat, snf, shift):
    if not str(farmer).strip() or not str(shift).strip():
        raise ValueError("ID and shift are required")

    litres = to_decimal(litres)
    fat = to_decimal(fat)
    snf = to_decimal(snf)

    if litres <= 0:
        raise ValueError("Litres must be positive")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Invalid fat")

    if not MIN_SNF <= snf <= MAX_SNF:
        raise ValueError("Invalid SNF")

    return litres, fat, snf

def steps(value, standard):
    return int(
        ((value - standard) / STEP).quantize(
            Decimal("1"), rounding=ROUND_HALF_UP
        )
    )

def rate_per_litre(fat, snf):
    rate = (
        BASE
        + steps(fat, Decimal("3.5")) * FAT_VALUE
        + steps(snf, Decimal("8.5")) * SNF_VALUE
    )

    return rate.quantize(CENT, rounding=ROUND_HALF_UP)

def payout(litres, fat, snf):
    return (litres * rate_per_litre(fat, snf)).quantize(
        CENT, rounding=ROUND_HALF_UP
    )

def calculate_totals(entries):
    totals = defaultdict(lambda: Decimal("0.00"))

    for farmer, litres, fat, snf, shift in entries:
        litres, fat, snf = validate_entry(
            farmer, litres, fat, snf, shift
        )

        totals[farmer] += payout(litres, fat, snf)

    return dict(totals)

if __name__ == "__main__":
    rows = [
        ("F001", "10", "3.5", "8.5", "Morning"),
        ("F001", "8.5", "4.2", "8.7", "Evening"),
        ("F002", "12", "3.1", "8.3", "Morning")
    ]

    for farmer, total in calculate_totals(rows).items():
        print(f"{farmer}: Rs {total:.2f}")

    assert rate_per_litre(Decimal("3.5"), Decimal("8.5")) == Decimal("30.00")
    assert rate_per_litre(Decimal("4.2"), Decimal("8.7")) == Decimal("33.40")
    assert rate_per_litre(Decimal("3.1"), Decimal("8.3")) == Decimal("27.80")

    assert payout(Decimal("10"), Decimal("3.5"), Decimal("8.5")) == Decimal("300.00")

    print("All tests passed")
