import frappe
import random


def supplier_recommendation(item):

    suppliers = frappe.get_all(
        "Supplier",
        fields=["name"]
    )

    ranking = []

    for s in suppliers:

        score = random.randint(70,95)

        ranking.append({
            "supplier": s.name,
            "score": score
        })

    ranking.sort(key=lambda x: x["score"], reverse=True)

    return {
        "item": item,
        "recommended_supplier": ranking[0],
        "ranking": ranking
    }