from decimal import Decimal, ROUND_HALF_UP
from collections import defaultdict

CENT = Decimal("0.01")
STEP = Decimal("0.1")
BONUS = Decimal("0.50")

CARDS = {
    "season": {
        "base": Decimal("32.00"),
        "fat": Decimal("0.45"),
        "snf": Decimal("0.30")
    },
    "regular": {
        "base": Decimal("30.00"),
        "fat": Decimal("0.40"),
        "snf": Decimal("0.30")
    }
}

def steps(value, standard):
    return int(
        ((value - standard) / STEP).quantize(
            Decimal("1"), rounding=ROUND_HALF_UP
        )
    )

def select_card(month):
    if month in (4, 5, 6):
        return CARDS["season"]

    return CARDS["regular"]

def rate_per_litre(fat, snf, month):
    card = select_card(month)

    rate = (
        card["base"]
        + steps(fat, Decimal("3.5")) * card["fat"]
        + steps(snf, Decimal("8.5")) * card["snf"]
    )

    return rate.quantize(CENT, rounding=ROUND_HALF_UP)

def ten_day_total(rows, month):
    totals = defaultdict(lambda: Decimal("0.00"))
    litres = defaultdict(lambda: Decimal("0.00"))

    for farmer, l, f, s in rows:
        l = Decimal(str(l))
        f = Decimal(str(f))
        s = Decimal(str(s))

        if not all(x.is_finite() for x in (l, f, s)):
            raise ValueError("Values must be finite")

        if l <= 0:
            raise ValueError("Invalid litres")

        if not Decimal("2.0") <= f <= Decimal("7.0"):
            raise ValueError("Invalid fat")

        if not Decimal("6.0") <= s <= Decimal("10.0"):
            raise ValueError("Invalid SNF")

        payment = (
            l * rate_per_litre(f, s, month)
        ).quantize(CENT, rounding=ROUND_HALF_UP)

        totals[farmer] += payment
        litres[farmer] += l

    for farmer, quantity in litres.items():
        if quantity > Decimal("500"):
            totals[farmer] += (
                quantity * BONUS
            ).quantize(CENT, rounding=ROUND_HALF_UP)

    return dict(totals)

if __name__ == "__main__":
    data = [
        ("F100", "300", "4.25", "8.63"),
        ("F100", "210", "4.25", "8.63"),
        ("F200", "500", "4.25", "8.63")
    ]

    print("May:", ten_day_total(data, 5))
    print("January:", ten_day_total(data, 1))

    assert rate_per_litre(
        Decimal("4.25"), Decimal("8.63"), 5
    ) == Decimal("35.90")

    assert rate_per_litre(
        Decimal("4.25"), Decimal("8.63"), 1
    ) == Decimal("33.50")

    print("Seasonal rate tests passed")
