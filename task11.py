import json
from decimal import Decimal

with open("rates.json", "r", encoding="utf-8") as file:
    raw = json.load(file)

rate_card = {
    key: Decimal(value)
    for key, value in raw.items()
}

print("Loaded Rate Card")
print("----------------")
print("Base Rate:", rate_card["base_rate"])
print("Fat Step Value:", rate_card["fat_step_value"])
print("SNF Step Value:", rate_card["snf_step_value"])

litres = Decimal("10")
fat_steps = 7
snf_steps = 2

rate = (
    rate_card["base_rate"]
    + fat_steps * rate_card["fat_step_value"]
    + snf_steps * rate_card["snf_step_value"]
)

payment = litres * rate

print("Rate per Litre: Rs", rate)
print("Total Payment: Rs", payment)
