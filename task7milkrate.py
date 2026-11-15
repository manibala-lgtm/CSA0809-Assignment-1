from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP = Decimal("0.1")
CENT = Decimal("0.01")

def rate_per_litre(fat, snf):
    fat_steps = int(
        ((fat - Decimal("3.5")) / STEP).quantize(
            Decimal("1"), rounding=ROUND_HALF_UP
        )
    )

    snf_steps = int(
        ((snf - Decimal("8.5")) / STEP).quantize(
            Decimal("1"), rounding=ROUND_HALF_UP
        )
    )

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )

    return rate.quantize(CENT, rounding=ROUND_HALF_UP)

def payout(litres, fat, snf):
    return (litres * rate_per_litre(fat, snf)).quantize(
        CENT, rounding=ROUND_HALF_UP
    )

if __name__ == "__main__":
    samples = [
        (Decimal("10"), Decimal("3.5"), Decimal("8.5")),
        (Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
        (Decimal("12"), Decimal("3.1"), Decimal("8.3"))
    ]

    for litres, fat, snf in samples:
        rate = rate_per_litre(fat, snf)
        payment = payout(litres, fat, snf)

        print(
            f"{litres} L | Fat: {fat} | SNF: {snf} | "
            f"Rate: Rs {rate} | Payment: Rs {payment}"
        )
