# Code to generate dictionary summary reports


def generate_report(orders:dict, products:dict, customers:dict, currency_symbol) -> dict:
    """
    generate a report dictionary with:
    - total products sold
    - most popular product
    - revenue per customer
    """
    
    sales_per_product = {}
    revenue_per_customer = {}
    
    #total products sold
    total_products_sold = sum(order["quantity"] for order in orders.values())
    
    
    for order in orders.values():
        customer_id = order["customer_id"]
        product_id = order["product_id"]
        quantity = order["quantity"]
        sales = order.get("final_price", 0)* quantity

        # Update sales per product
        if product_id not in sales_per_product:
            sales_per_product[product_id] = 0
        sales_per_product[product_id] += quantity

        # Update revenue per customer
        if customer_id not in revenue_per_customer:
            revenue_per_customer[customer_id] = 0
        revenue_per_customer[customer_id] += sales
        
    #update customer names in revenue report
    revenue_per_customer = {
        customers[customer_id]["name"]: revenue for customer_id, revenue 
        in revenue_per_customer.items()
        }

    #most popular product
    if sales_per_product:
        most_popular_id = max(sales_per_product, key=sales_per_product.get)
        most_popular_product = products[most_popular_id]["product_name"] if most_popular_id else None

    
    
    # Generate report
    report = {
        "total_products_sold": total_products_sold,
        "most_popular_product": most_popular_product,
        "revenue_per_customer": revenue_per_customer
    }

    return report
