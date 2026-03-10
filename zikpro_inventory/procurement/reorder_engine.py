import frappe


def reorder_engine():

    bins = frappe.get_all(
        "Bin",
        fields=["item_code", "warehouse", "actual_qty"]
    )

    reorder_level = 20
    reorder_qty = 50

    suggestions = []

    for b in bins:

        if b.actual_qty < reorder_level:

            suggestions.append({
                "item_code": b.item_code,
                "warehouse": b.warehouse,
                "current_stock": b.actual_qty,
                "suggested_purchase_qty": reorder_qty
            })

    return suggestions