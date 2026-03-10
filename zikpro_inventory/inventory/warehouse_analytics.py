import frappe


def warehouse_analytics():

    bins = frappe.get_all(
        "Bin",
        fields=["warehouse", "actual_qty"]
    )

    warehouse_data = {}

    for b in bins:

        if b.warehouse not in warehouse_data:
            warehouse_data[b.warehouse] = {
                "items": 0,
                "stock": 0
            }

        warehouse_data[b.warehouse]["items"] += 1
        warehouse_data[b.warehouse]["stock"] += b.actual_qty

    return warehouse_data