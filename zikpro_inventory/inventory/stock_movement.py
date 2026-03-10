import frappe


def stock_movement_intelligence():

    bins = frappe.get_all(
        "Bin",
        fields=["item_code", "actual_qty"]
    )

    fast = []
    slow = []
    dead = []

    for b in bins:

        if b.actual_qty > 150:
            fast.append(b.item_code)

        elif b.actual_qty < 20:
            slow.append(b.item_code)

        elif b.actual_qty == 0:
            dead.append(b.item_code)

    return {
        "fast_moving": fast,
        "slow_moving": slow,
        "dead_stock": dead
    }