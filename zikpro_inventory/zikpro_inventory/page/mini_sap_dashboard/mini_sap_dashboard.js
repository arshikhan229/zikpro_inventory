frappe.pages['mini-sap-dashboard'].on_page_load = function(wrapper) {

    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Mini SAP Analytics Dashboard',
        single_column: true
    });

    let body = $(page.body);

    body.html(`
        <div style="display:flex; gap:20px; margin-bottom:20px">

            <div class="card" style="padding:20px">
                <h4>Total Items</h4>
                <h2 id="total_items">...</h2>
            </div>

            <div class="card" style="padding:20px">
                <h4>Total Stock</h4>
                <h2 id="total_stock">...</h2>
            </div>

            <div class="card" style="padding:20px">
                <h4>Low Stock Items</h4>
                <h2 id="low_stock">...</h2>
            </div>

        </div>

        <div>
            <h3>Warehouse Distribution</h3>
            <div id="warehouse_chart"></div>
        </div>

        <div style="margin-top:30px">
            <h3>AI Smart Reorder</h3>
            <div id="ai_reorder"></div>
        </div>

        <div style="margin-top:30px">
            <h3>Demand Forecast</h3>
            <div id="forecast_chart"></div>
        </div>

        <div style="margin-top:30px">
            <div id="ai_prediction"></div>
        </div>
    `);

    // Inventory summary
    frappe.call({
        method: "zikpro_inventory.api.inventory_dashboard",
        callback: function(r){

            $("#total_items").text(r.message.total_items);
            $("#total_stock").text(r.message.total_stock);
            $("#low_stock").text(r.message.low_stock_items);

        }
    });

    // Warehouse analytics
    frappe.call({
        method: "zikpro_inventory.api.get_warehouse_analytics",
        callback: function(r){

            let data = r.message;

            let labels = [];
            let values = [];

            for (let w in data){
                labels.push(w);
                values.push(data[w].stock);
            }

            new frappe.Chart("#warehouse_chart", {
                title: "Warehouse Stock",
                data: {
                    labels: labels,
                    datasets: [
                        {
                            name: "Stock",
                            values: values
                        }
                    ]
                },
                type: 'bar',
                height: 300
            });

        }
    });

    // AI reorder
    frappe.call({
        method: "zikpro_inventory.api.get_ai_reorder",
        args: { item: "MILK-001" },
        callback: function(r){

            let d = r.message;

            $("#ai_reorder").html(`
                Item: ${d.item} <br>
                Current Stock: ${d.current_stock} <br>
                Predicted Demand: ${d.predicted_demand} <br>
                Suggested Reorder: ${d.suggested_reorder}
            `);

        }
    });

    // AI prediction summary
    frappe.call({
        method: "zikpro_inventory.api.ai_prediction_summary",
        args: { item: "MILK-001" },
        callback: function(r){

            let d = r.message;

            $("#ai_prediction").html(`
                <h4>AI Prediction</h4>
                Item: ${d.item}<br>
                Current Stock: ${d.current_stock}<br>
                Predicted Demand: ${d.predicted_demand}<br>
                Suggested Reorder: ${d.suggested_reorder}<br>
                Recommended Supplier: ${d.supplier}
            `);

        }
    });

    // Forecast chart
    new frappe.Chart("#forecast_chart", {
        title: "Demand Forecast",
        data: {
            labels: ["Day1","Day2","Day3","Day4","Day5"],
            datasets: [
                {
                    name: "Demand",
                    values: [50,60,70,80,90]
                }
            ]
        },
        type: "line"
    });

};