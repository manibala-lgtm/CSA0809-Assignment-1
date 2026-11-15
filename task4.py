from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")

FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

litres = Decimal("10")
fat = Decimal("4.2")
snf = Decimal("8.5")

fat_steps = int(
    ((fat - STANDARD_FAT) / Decimal("0.1")).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )
)

snf_steps = int(
    ((snf - STANDARD_SNF) / Decimal("0.1")).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )
)

rate = (
    BASE_RATE
    + fat_steps * FAT_STEP_VALUE
    + snf_steps * SNF_STEP_VALUE
)

amount = (litres * rate).quantize(Decimal("0.01"))

print("Fat Steps:", fat_steps)
print("SNF Steps:", snf_steps)
print("Rate per Litre: Rs", rate)
print("Total Payment: Rs", amount)

print("4.2 - 3.5 divided by 0.1:",
      (4.2 - 3.5) / 0.1)

print("Rounded Steps:", round((4.2 - 3.5) / 0.1))
print("-7 // 2 =", -7 // 2)
print("-2 ** 2 =", -2 ** 2)
print("(-2) ** 2 =", (-2) ** 2)
