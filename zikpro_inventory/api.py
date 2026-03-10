import frappe

# Inventory Module
from zikpro_inventory.inventory.warehouse_analytics import warehouse_analytics
from zikpro_inventory.inventory.stock_movement import stock_movement_intelligence

# Procurement Module
from zikpro_inventory.procurement.reorder_engine import reorder_engine
from zikpro_inventory.procurement.auto_purchase_order import auto_create_purchase_order

# ai 
from zikpro_inventory.ai.smart_reorder import ai_smart_reorder
from zikpro_inventory.ai.supplier_recommendation import supplier_recommendation
from zikpro_inventory.ai.procurement_agent import autonomous_procurement

#==============================
#   AI Dashboard
#===============================
@frappe.whitelist()
def ai_dashboard(item):

    from zikpro_inventory.ai.smart_reorder import ai_smart_reorder

    return ai_smart_reorder(item)


@frappe.whitelist()
def ai_prediction_summary(item):

    from zikpro_inventory.ai.smart_reorder import ai_smart_reorder
    from zikpro_inventory.ai.supplier_recommendation import supplier_recommendation

    forecast = ai_smart_reorder(item)
    supplier = supplier_recommendation(item)

    return {
        "item": item,
        "current_stock": forecast["current_stock"],
        "predicted_demand": forecast["predicted_demand"],
        "suggested_reorder": forecast["suggested_reorder"],
        "supplier": supplier["recommended_supplier"]["supplier"]
    }



#================================
#    AI API
#================================

@frappe.whitelist()
def get_ai_reorder(item):
    return ai_smart_reorder(item)


@frappe.whitelist()
def get_supplier_recommendation(item):
    return supplier_recommendation(item)

@frappe.whitelist()
def run_ai_procurement(item):
    return autonomous_procurement(item)

# ================================
# Inventory APIs
# ================================

@frappe.whitelist()
def get_warehouse_analytics():
    return warehouse_analytics()


@frappe.whitelist()
def get_stock_movement():
    return stock_movement_intelligence()


# ================================
# Procurement APIs
# ================================

@frappe.whitelist()
def get_reorder_suggestions():
    return reorder_engine()


@frappe.whitelist()
def run_auto_purchase():
    return auto_create_purchase_order()


# ================================
# Dashboard API
# ================================

@frappe.whitelist()
def inventory_dashboard():

    bins = frappe.get_all("Bin", fields=["actual_qty"])

    total_items = len(bins)
    total_stock = sum([b.actual_qty for b in bins])

    low_stock = reorder_engine()

    return {
        "total_items": total_items,
        "total_stock": total_stock,
        "low_stock_items": len(low_stock)
    }

#======================================
@frappe.whitelist()
def get_inventory_alerts():

    bins = frappe.get_all(
        "Bin",
        fields=["item_code","warehouse","actual_qty"]
    )

    alerts = []

    for b in bins:

        if b.actual_qty < 20:

            alerts.append({
                "item": b.item_code,
                "warehouse": b.warehouse,
                "stock": b.actual_qty
            })

    return alerts

#=====================================
@frappe.whitelist()
def supplier_performance():

    suppliers = frappe.get_all("Supplier", fields=["name"])

    import random

    scores = []

    for s in suppliers:

        scores.append({
            "supplier": s.name,
            "score": random.randint(70,95)
        })

    return scores

#=================================
@frappe.whitelist()
def restocking_plan():

    items = frappe.get_all("Item", fields=["name"])

    import random

    plan = []

    for i in items:

        plan.append({
            "item": i.name,
            "reorder_in_days": random.randint(3,10)
        })

    return plan