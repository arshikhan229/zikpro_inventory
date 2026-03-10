import frappe


def run_ai_procurement_job():

    items = frappe.get_all("Item", fields=["name"])

    for i in items:

        try:
            frappe.call(
                "zikpro_inventory.api.run_ai_procurement",
                item=i.name
            )

        except Exception:
            frappe.log_error(frappe.get_traceback())