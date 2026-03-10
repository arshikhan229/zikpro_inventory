# Zikpro Inventory – Mini SAP AI Supply Chain System

Zikpro Inventory is an AI-powered inventory and procurement automation system built on **Frappe Framework and ERPNext**.

The project demonstrates how Artificial Intelligence can be integrated with ERP systems to automate inventory management, demand forecasting, supplier selection, and purchase order creation.

This system acts as a **Mini SAP-style intelligent supply chain platform**.

---

# Features

## Inventory Analytics
- Inventory dashboard
- Warehouse stock distribution
- Stock movement intelligence
- Inventory alerts for low stock items

## AI Demand Forecast
- Predicts future demand (currently simulated using random data)
- Calculates smart reorder quantities

## Procurement Automation
- Reorder engine
- Automatic purchase order generation

## AI Supplier Intelligence
- Supplier recommendation
- Supplier performance scoring

## Autonomous Procurement Agent
- AI agent that:
  - detects low stock
  - predicts demand
  - selects supplier
  - creates purchase order automatically

## Scheduler Automation
The system can run automatically using the Frappe scheduler to perform daily AI procurement analysis.

---

# Technology Stack

- Python
- Frappe Framework
- ERPNext
- JavaScript
- MariaDB
- Redis
- Bench CLI

---

# System Architecture


Mini SAP Architecture

Inventory Layer
↓
Analytics Layer
↓
AI Forecast Engine
↓
Decision Engine
↓
Procurement Automation
↓
Scheduler Automation


---

# Dashboard

The system includes a **Mini SAP Analytics Dashboard** displaying:

- Total inventory items
- Total stock
- Low stock alerts
- Warehouse distribution chart
- AI smart reorder suggestions
- Demand forecast visualization

---

# Example API Usage

### AI Reorder Prediction

```python
frappe.call("zikpro_inventory.api.get_ai_reorder", item="MILK-001")


Example response:

{
 "item": "MILK-001",
 "current_stock": 200,
 "predicted_demand": 327,
 "suggested_reorder": 127
 
}

###Run Autonomous AI Procurement

frappe.call("zikpro_inventory.api.run_ai_procurement", item="MILK-001")

Example response:

{
 "item": "MILK-001",
 "supplier": "ALL001",
 "predicted_demand": 327,
 "reorder_qty": 127,
 "purchase_order": "PUR-ORD-2026-00005"
}

Installation

You can install this app using the bench CLI.

cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO
bench install-app zikpro_inventory


###Project Structure
zikpro_inventory
│
├ inventory
│   ├ warehouse_analytics.py
│   └ stock_movement.py
│
├ procurement
│   ├ reorder_engine.py
│   └ auto_purchase_order.py
│
├ ai
│   ├ demand_forecast.py
│   ├ smart_reorder.py
│   ├ supplier_recommendation.py
│   └ procurement_agent.py
│
├ scheduler.py
├ api.py
└ page
    └ mini_sap_dashboard


###Future Improvements

Machine learning demand forecasting using sales history

Multi-warehouse optimization

Supplier reliability scoring

Real-time inventory alerts

Advanced supply chain analytics

###Contributing

This app uses pre-commit for code formatting and linting.

Install pre-commit:

pip install pre-commit

Enable it:
cd apps/zikpro_inventory
pre-commit install

Tools used:

ruff

eslint

prettier

pyupgrade



###CI

GitHub Actions can be used for continuous integration.

Workflows include:

CI testing on push

Security checks using pip-audit

Code scanning using Frappe Semgrep rules


###License

MIT License
