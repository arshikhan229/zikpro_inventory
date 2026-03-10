import frappe

def run_inventory_scan():

    print("Inventory Scanner Started")

    bins = frappe.get_all(
        "Bin",
        fields=["item_code", "warehouse", "actual_qty"]
    )

    print("Total bins:", len(bins))

    for b in bins:

        stock = b.actual_qty or 0

        status = "Normal"
        suggestion = "Stock healthy"

        if stock <= 10:
            status = "Low Stock"
            suggestion = "Reorder immediately"

        if stock == 0:
            status = "Dead Stock"
            suggestion = "Item out of stock"

        # avoid duplicate alerts
        existing = frappe.get_all(
            "Inventory Alert",
            filters={
                "item": b.item_code,
                "warehouse": b.warehouse
            }
        )

        if not existing:

            frappe.get_doc({
                "doctype": "Inventory Alert",
                "item": b.item_code,
                "warehouse": b.warehouse,
                "current_stock": stock,
                "status": status,
                "suggestion": suggestion
            }).insert(ignore_permissions=True)

            print("Alert created:", b.item_code)

    print("Inventory scan finished")