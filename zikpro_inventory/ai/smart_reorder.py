import frappe
from zikpro_inventory.ai.demand_forecast import demand_forecast


def ai_smart_reorder(item):

    forecast = demand_forecast(item)

    # Ensure stock is not None
    current_stock = forecast.get("current_stock") or 0

    reorder_qty = max(
        forecast["predicted_demand"] - current_stock, 0
    )

    return {
        "item": item,
        "current_stock": current_stock,
        "predicted_demand": forecast["predicted_demand"],
        "suggested_reorder": reorder_qty
    }