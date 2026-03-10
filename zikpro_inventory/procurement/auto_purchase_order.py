import frappe
from frappe.utils import nowdate


def auto_create_purchase_order():

    supplier = "Test Supplier"

    bins = frappe.get_all(
        "Bin",
        fields=["item_code", "warehouse", "actual_qty"]
    )

    reorder_level = 20
    reorder_qty = 50

    created_orders = []

    for b in bins:

        if b.actual_qty < reorder_level:

            warehouse_company = frappe.db.get_value(
                "Warehouse",
                b.warehouse,
                "company"
            )

            po = frappe.get_doc({
                "doctype": "Purchase Order",
                "supplier": supplier,
                "company": warehouse_company,
                "schedule_date": nowdate(),
                "items": [
                    {
                        "item_code": b.item_code,
                        "qty": reorder_qty,
                        "schedule_date": nowdate(),
                        "warehouse": b.warehouse
                    }
                ]
            })

            po.insert(ignore_permissions=True)

            created_orders.append(po.name)

    frappe.db.commit()

    return created_orders