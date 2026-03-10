import frappe
from frappe.utils import nowdate
from zikpro_inventory.ai.smart_reorder import ai_smart_reorder
from zikpro_inventory.ai.supplier_recommendation import supplier_recommendation


def autonomous_procurement(item):

    # AI forecast
    forecast = ai_smart_reorder(item)

    reorder_qty = forecast["suggested_reorder"]

    # If reorder not needed → stop
    if reorder_qty <= 0:
        return {
            "item": item,
            "message": "No reorder required"
        }

    # AI supplier selection
    supplier = supplier_recommendation(item)

    # Find warehouse from Bin
    warehouse = frappe.get_value(
        "Bin",
        {"item_code": item},
        "warehouse"
    )

    # If no warehouse found → fallback
    if not warehouse:
        warehouse = frappe.get_value(
            "Warehouse",
            {"is_group": 0},
            "name"
        )

    # Get company from warehouse
    company = frappe.get_value(
        "Warehouse",
        warehouse,
        "company"
    )

    # Create Purchase Order
    po = frappe.get_doc({
        "doctype": "Purchase Order",
        "supplier": supplier["recommended_supplier"]["supplier"],
        "company": company,
        "schedule_date": nowdate(),
        "items": [
            {
                "item_code": item,
                "qty": reorder_qty,
                "schedule_date": nowdate(),
                "warehouse": warehouse
            }
        ]
    })

    po.insert(ignore_permissions=True)

    frappe.db.commit()

    return {
        "item": item,
        "supplier": supplier["recommended_supplier"],
        "predicted_demand": forecast["predicted_demand"],
        "reorder_qty": reorder_qty,
        "warehouse": warehouse,
        "purchase_order": po.name
    }