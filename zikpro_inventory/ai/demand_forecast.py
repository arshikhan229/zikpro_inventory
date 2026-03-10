import frappe
import random


def demand_forecast(item):

    # current stock
    current_stock = frappe.db.get_value(
        "Bin",
        {"item_code": item},
        "actual_qty"
    )

    # simulated AI prediction
    predicted_demand = random.randint(200, 400)

    return {
        "item": item,
        "current_stock": current_stock,
        "predicted_demand": predicted_demand
    }