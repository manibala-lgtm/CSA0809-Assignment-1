from decimal import Decimal
import task7milkrate as mr

payment = mr.payout(
    Decimal("8.5"),
    Decimal("4.2"),
    Decimal("8.7")
)

print("Payment: Rs", payment)
